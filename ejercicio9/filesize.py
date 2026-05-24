(archivo)=open("test.txt", "a", encoding="utf-8") # Abrir el archivo en modo añadir

for i in range(1048576):
    # Aquí es donde pones la "a" entre comillas
    archivo.write("a") 

archivo.close() # Cerrar el archivo