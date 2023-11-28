from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddClienteForm
from .models import Cliente


def home(request):
	clientes = Cliente.objects.all()
	# Comprueba si estás iniciando sesión
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		# Autenticar
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, "¡Has iniciado sesión!")
			return redirect('home')
		else:
			messages.success(request, "Se produjo un error al iniciar sesión, inténtelo de nuevo...")
			return redirect('home')
	else:
		return render(request, 'home.html', {'clientes':clientes})



def logout_user(request):
	logout(request)
	messages.success(request, "Has sido desconectado...")
	return redirect('home')


def register_user(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			# Authenticate and login
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, "¡Se ha registrado exitosamente! ¡Bienvenido!")
			return redirect('home')
	else:
		form = SignUpForm()
		return render(request, 'register.html', {'form':form})

	return render(request, 'register.html', {'form':form})



def customer_cliente(request, pk):
	if request.user.is_authenticated:
		# Buscar registros
		customer_cliente = Cliente.objects.get(id=pk)
		return render(request, 'cliente.html', {'customer_cliente':customer_cliente})
	else:
		messages.success(request, "Debes iniciar sesión para ver esa página...")
		return redirect('home')



def delete_cliente(request, pk):
	if request.user.is_authenticated:
		delete_it = Cliente.objects.get(id=pk)
		delete_it.delete()
		messages.success(request, "Cliente eliminado exitosamente...")
		return redirect('home')
	else:
		messages.success(request, "Debe iniciar sesión para hacer eso...")
		return redirect('home')


def add_cliente(request):
	form = AddClienteForm(request.POST or None)
	if request.user.is_authenticated:
		if request.method == "POST":
			if form.is_valid():
				add_cliente = form.save()
				messages.success(request, "Cliente agregado...")
				return redirect('home')
		return render(request, 'add_cliente.html', {'form':form})
	else:
		messages.success(request, "Usted debe estar conectado...")
		return redirect('home')


def update_cliente(request, pk):
	if request.user.is_authenticated:
		current_cliente = Cliente.objects.get(id=pk)	
		form = AddClienteForm(request.POST or None, instance=current_cliente)
		if form.is_valid():
			form.save()
			messages.success(request, "¡El cliente ha sido actualizado!")
			return redirect('home')
		return render(request, 'update_cliente.html', {'form':form})
	else:
		messages.success(request, "Usted debe estar conectado...")
		return redirect('home')