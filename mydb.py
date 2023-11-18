import mysql.connector

dataBase = mysql.connector.connect(
    
    host='localhost', 
    user='root', 
    passwd='', 

)

# Preparando objeto cursor
cursorObject = dataBase.cursor()

# Creando base de datos
cursorObject.execute("CREATE DATABASE gcfs_clie")

print("All done!")