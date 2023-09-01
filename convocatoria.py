import uuid

print("-*- Fiesta -*-")
print("****-****")
print("0. SALIR")
print("1. Registrar invitados")
print("2. Ver lista de invitados")
print("3. Ver invitados VIP")
print("4. Cobranza")
print("5. Editar información")
print("6. Retirar invitados")
print("****-****")

opcion=99

invitados=[]
while opcion!=0:
    invitado={}
    
    opcion=int(input("Digita una opción: "))
    if opcion==1:
        invitado["nombre"]=input("Digite su nombre: ")
        invitado["id"]= str(uuid.uuid4())
        invitado["cedula"]=input("Digite su cédula: ")
        invitado["eps"]=input("Digite su EPS: ")
        estado_input = input("Pago (True/False): ")
        if estado_input.lower() == 'true':
            invitado["estado"] = True
        else:
            invitado["estado"] = False
        invitado["valorcuota"]=float(input("Ingrese el valor de la cuota: "))
        invitado["edad"]=input("Ingrese su edad: ")
        
        """invitado = {
            'Nombre': nombre,
            'ID': id,
            'Cédula': cedula,
            'EPS': eps,
            'Pago': estado,
            'Valor de la Cuota': valorcuota,
            'Edad': edad
        }"""
        invitados.append(invitado)
        print("Invitado agregado correctamente.")
    elif opcion==2:
        #Iterating the list
        for persona in invitados:
            print(f"persona:{persona['nombre']}")
            print(f"persona:{persona['id']}")
    elif opcion==3:
        for persona in invitados:
            if persona["estado"]==True:
                print(persona)
    elif opcion==4:
        pass
    elif opcion==5:
        pass
    elif opcion==6:
        pass
    else:
        print("Opción inválida")