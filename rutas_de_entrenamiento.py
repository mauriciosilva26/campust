import datos_ruta

def ruta_entreno ():
    ruta={}
    ruta["ruta_nueva"]=input("Ingrese una nueva Area de entrenamiento")
    
    datos_ruta.data.append(ruta)
    datos_ruta.guardar_datos()
    


def mostrar_rutas():
    print("Las Area de entrenamineto registradas son:")
    for ruta in datos_ruta.data:
        print("Ruta:", ruta["ruta_nueva"])
        print("Area de entrenamineto Registradas por defecto:")
        ruta["ruta1"]=print("Fundamentos de programación (Introducción a la algoritmia, PSeInt y Python)")
        ruta["ruta2"]= print("Programación Web (HTML, CSS y Bootstrap).")
        ruta["ruta3"]= print("Programación formal (Java, JavaScript, C#).")
        ruta["ruta4"] = print("Bases de datos (Mysql, MongoDb y Postgresql). Cada ruta tiene un SGDB principal y un alternativo.")
        ruta["ruta5"] = print ("Backend (NetCore, Spring Boot, NodeJS y Express).")


    datos_ruta.data.append(ruta)
    datos_ruta.guardar_datos()