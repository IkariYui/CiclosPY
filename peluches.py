peluches = ["roshi", "conejito", "aguacatico"]

opcion = 0
print("Peluchería")
print(".............")
print(" 1. Agregar producto a la bodega")
print(" 2. Ver productos en bodega")
print(" 3. Obtener valor del inventario")
print(" 4. Ver productos más vendidos")
print(" 5. Salir")

while(opcion!=5):
    opcion=int(input("Digita un número "))
    
    if(opcion==1):
        nombre=input("Digita el nombre del producto")
        #Add data to a list
        peluches.append(nombre)
       
    elif (opcion==2):
        print("Usted está en la opción 2")    
    elif (opcion==3):
        print("Está en la opción 3")
    elif (opcion==4):
        print("Está en la opción 4")
    else: 
        print("Opción inválida")    
            
print("Salí del bucle")
    
    