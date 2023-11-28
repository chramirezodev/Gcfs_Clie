from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Cliente

class SignUpForm(UserCreationForm):
	email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Correo electrónico'}))
	first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre'}))
	last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Apellido'}))


	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].widget.attrs['placeholder'] = 'Nombre de usuario'
		self.fields['username'].label = ''
		self.fields['username'].help_text = '<span class="form-text text-muted"><small>Requerido: 150 caracteres o menos. Letras, dígitos y @/./+/-/_ únicamente.</small></span>'

		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['placeholder'] = 'Contraseña'
		self.fields['password1'].label = ''
		self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Su contraseña no puede ser similar a su información personal.</li><li>Su contraseña debe contener al menos 8 caracteres.</li><li>Su contraseña no puede ser una contraseña de uso común.</li><li>Tu contraseña no puede ser completamente numérica.</li></ul>'

		self.fields['password2'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['placeholder'] = 'Confirmar Contraseña'
		self.fields['password2'].label = ''
		self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Ingrese la misma contraseña, para verificación.</small></span>'	




# Crear formulario para agregar cliente
class AddClienteForm(forms.ModelForm):
	nombres = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Nombres/Razón Social", "class":"form-control"}), label="")
	apellido1 = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Primer Apellido", "class":"form-control"}), label="")
	apellido2 = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Segundo Apellido", "class":"form-control"}), label="")
	sexo = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Sexo", "class":"form-control"}), label="")
	fecha_nac = forms.DateField(required=True, widget=forms.widgets.DateInput (attrs={"placeholder":"Fecha de nacimiento", "class":"form-control"}), label="")
	pais_nac = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"País de nacimiento", "class":"form-control"}), label="")
	dpto_nac = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Departamento de nacimiento", "class":"form-control"}), label="")
	ciudad_nac = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Ciudad de nacimiento", "class":"form-control"}), label="")
	tipo_ident = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Tipo de identificación", "class":"form-control"}), label="")
	num_ident = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Número de identificación", "class":"form-control"}), label="")
	fecha_exp_cc = forms.DateField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Fecha de expedición de la cédula", "class":"form-control"}), label="")
	esta_civil = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Estado civil", "class":"form-control"}), label="")
	nivel_estudio = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Nivel de estudios", "class":"form-control"}), label="")
	titulo_estudio = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Título", "class":"form-control"}), label="")
	pcd = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"¿Es usted una Persona con Discapacidad (PcD)?", "class":"form-control"}), label="")
	email1 = forms.EmailField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Correo electrónico principal", "class":"form-control"}), label="")
	email2 = forms.EmailField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Correo electrónico secundario", "class":"form-control"}), label="")
	direccion_resi = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Dirección residencia", "class":"form-control"}), label="")
	pais_resi = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"País de residencia", "class":"form-control"}), label="")
	dpto_resi = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Departamento de residencia", "class":"form-control"}), label="")
	ciudad_resi = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Ciudad de residencia", "class":"form-control"}), label="")
	estrato_resi = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Estrato", "class":"form-control"}), label="")
	tel_resi = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Teléfono residencia", "class":"form-control"}), label="")
	celular1 = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Teléfono celular principal", "class":"form-control"}), label="")
	celular2 = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Teléfono celular secundario", "class":"form-control"}), label="")
	persona_acargo = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"No. de personas a cargo", "class":"form-control"}), label="")
	antiguedad = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Antigüedad en la ciudad", "class":"form-control"}), label="")
	tipo_vivienda = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Tipo de vivienda y relación con el domicilio", "class":"form-control"}), label="")
	valor_vivienda = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Valor de la vivienda propia", "class":"form-control"}), label="")
	direccion_of = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Dirección oficina", "class":"form-control"}), label="")
	pais_of = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"País de oficina", "class":"form-control"}), label="")
	dpto_of = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Departamento de oficina", "class":"form-control"}), label="")
	ciudad_of = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Ciudad de oficina", "class":"form-control"}), label="")
	tel_of = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Teléfono oficina", "class":"form-control"}), label="")
	ext_of = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Extensión", "class":"form-control"}), label="")
	celular1_of = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Celular oficina", "class":"form-control"}), label="")
	reside_colombia = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"¿Reside en Colombia?", "class":"form-control"}), label="")
	nacionalidad1 = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Nacionalidad 1", "class":"form-control"}), label="")
	nacionalidad2 = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Nacionalidad 2", "class":"form-control"}), label="")
	info_comercial = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"¿Por cuál medio le gustaría recibir información comercial de G.C.F.S. S.A.S.?", "class":"form-control"}), label="")
	nombres_conyuge = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Nombres y apellidos conyuge", "class":"form-control"}), label="")
	tipo_ident_conyuge = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Tipo de identificación", "class":"form-control"}), label="")
	num_ident_conyuge = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Número de identificación", "class":"form-control"}), label="")
	tel_resi_conyuge = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Teléfono conyuge", "class":"form-control"}), label="")
	celular1_conyuge = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Celular principal conyuge", "class":"form-control"}), label="")
	celular2_conyuge = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Celular secundario conyuge", "class":"form-control"}), label="")
	situacion_laboral = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Situación laboral", "class":"form-control"}), label="")
	empresa_actual = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Nombre de empresa donde trabaja/del negocio", "class":"form-control"}), label="")
	socio = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"¿Es socio de la empresa donde trabaja?", "class":"form-control"}), label="")
	cargo = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Cargo/Ocupación/Oficio", "class":"form-control"}), label="")
	fecha_ingreso = forms.DateField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Fecha de ingreso o inicio de actividad", "class":"form-control"}), label="")
	actividad_economica = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Actividad económica de la empresa", "class":"form-control"}), label="")
	ppe = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"¿Persona públicamente expuesta?", "class":"form-control"}), label="")
	ingresos_mensuales = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Ingresos mensuales", "class":"form-control"}), label="")
	otros_ingresos = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Otros ingresos", "class":"form-control"}), label="")
	egresos_mensuales = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Egresos mensuales", "class":"form-control"}), label="")
	total_activos = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Total activos", "class":"form-control"}), label="")
	total_pasivo = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Total pasivos", "class":"form-control"}), label="")
	concepto_otro_ingreso = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Indique a qué corresponden los otros ingresos", "class":"form-control"}), label="")
	procedencia_recursos = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Procedencia de los recursos que relaciona", "class":"form-control"}), label="")
	declara_renta = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"¿Declara renta?", "class":"form-control"}), label="")
	nombres_ref_fam1 = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Nombres y Apellidos Referencia Familiar 1", "class":"form-control"}), label="")
	parentesco_ref_fam1 = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Parentesco Referencia Familiar 1", "class":"form-control"}), label="")
	ciudad_ref_fam1 = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Ciudad Referencia Familiar 1", "class":"form-control"}), label="")
	tel_ref_fam1 = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Teléfono Referencia Familiar 1", "class":"form-control"}), label="")
	cel_ref_fam1 = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Celular Referencia Familiar 1", "class":"form-control"}), label="")
	nombres_ref_fam2 = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Nombres y Apellidos Referencia Familiar 2", "class":"form-control"}), label="")
	parentesco_ref_fam2 = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Parentesco Referencia Familiar 2", "class":"form-control"}), label="")
	ciudad_ref_fam2 = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Ciudad Referencia Familiar 2", "class":"form-control"}), label="")
	tel_ref_fam2 = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Teléfono Referencia Familiar 2", "class":"form-control"}), label="")
	cel_ref_fam2 = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Celular Referencia Familiar 2", "class":"form-control"}), label="")
	nombres_ref_per1 = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Nombres y Apellidos Referencia Personal 1", "class":"form-control"}), label="")
	parentesco_ref_per1 = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Parentesco Referencia Personal 1", "class":"form-control"}), label="")
	ciudad_ref_per1 = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Ciudad Referencia Personal 1", "class":"form-control"}), label="")
	tel_ref_per1 = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Teléfono Referencia Personal 1", "class":"form-control"}), label="")
	cel_ref_per1 = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Celular Referencia Personal 1", "class":"form-control"}), label="")
	nombres_ref_per2 = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Nombres y Apellidos Referencia Personal 2", "class":"form-control"}), label="")
	parentesco_ref_per2 = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Parentesco Referencia Personal 2", "class":"form-control"}), label="")
	ciudad_ref_per2 = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Ciudad Referencia Personal 2", "class":"form-control"}), label="")
	tel_ref_per2 = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Teléfono Referencia Personal 2", "class":"form-control"}), label="")
	cel_ref_per2 = forms.CharField(required=False, widget=forms.widgets.TextInput(attrs={"placeholder":"Celular Referencia Personal 2", "class":"form-control"}), label="")

	class Meta:
		model = Cliente
		exclude = ("user",)