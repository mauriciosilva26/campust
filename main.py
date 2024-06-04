import datos
import datostrainers
import letreros
def menu_principal():
    datos.cargar_datos()
    while True:
        
        
        print("ingres su rol\n 1. coordinador\n 2. trainer")
        rol = 0
        try:
            rol = int(input("Ingrese la opción de su rol: "))
        except Exception:
            print("Valor incorrecto!!")            
        if rol == 1:
            letreros.letrero1()
            print("1. trainers\n 2.campers")
            opcion=int(input("ingrese la opcion que desea realizar: "))
            if opcion == 1:
                print("1. registar trainer\n 2. modificar trainer")
                opct=int(input("ingrese la opcion a realizar: "))
                if opct == 1:
                    datostrainers.cargar_datos()
                    datostrainers.registrar_trainer()
                elif opct ==2:
                    datostrainers.cargar_datos()
                    print("que opccion desea modificar del trainer:\n 1. horario\n 2. area de entrenamiento\n 3.agregar grupo al trainer")
                    
                    opctm=int(input("ingrese la opcion que desea modificar: "))
                    if opctm ==1:
                        datostrainers.cargar_datos()
                        datostrainers.horario_del_trainer()
                    elif opctm ==2:
                        datostrainers.cargar_datos()
                        datostrainers.area_del_trainer()
                    elif opctm == 3:
                        datostrainers.cargar_datos()
                        datostrainers.grupo_del_trainer()
            elif opcion==2:
                print("1. registrar camper \n 2.modificar camper")
                opcc=int(input("ingrese la opcion a la que dea acceder: "))
                if opcc == 1:
                    datos.cargar_datos()
                    datos.registrar_camper()
                elif opcc == 2: 
                    print("1.estado del camper\n 2.riesgo \n 3.ruta\n 4. eliminar camper\n 5.asignar grupo al camper")
                    opccm=int(input("ingrese a la opcion del camper que desea modificar: "))
                    if opccm == 1:
                        datos.cargar_datos()
                        datos.estado_camper()
                    elif opccm == 2:
                        datos.cargar_datos()
                        datos.riesgo_camper()
                    elif opccm == 3:
                        print("rutas:\n nodaJS\n java\n javaScrip")
                        datos.cargar_datos()
                        datos.ruta_camper()
                    elif opccm == 4:
                        datos.cargar_datos()
                        datos.eliminar_camper()
                    elif opccm == 5:
                        datos.cargar_datos()
                        datos.grupo_camper()
                    
        elif rol == 2:
            print("1.dar notas a un camper\n 2.salir") 
            opctn= int(input("ingrese la opcion que desea realizar"))    
            if opctn == 1:
                datos.cargar_datos
                datos.nota_camper
            elif opctn == 2:
                print ("saliendo")

        elif rol == 3:
            print("1. ver notas\n 2. salir")

                            
                        
                    
                    