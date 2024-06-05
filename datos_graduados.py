import json

data = []

RUTA_ARCHIVO = "graduados.json"

def guardar_datos():
    global data
    global RUTA_ARCHIVO
    try:
        contenido = json.dumps(data, indent=4)
        with open(RUTA_ARCHIVO, "w") as file:
            file.write(contenido)
        print("Datos guardados exitosamente!!")
    except Exception:
        print("Error al guardar datos")

def cargar_datos():
    global data
    global RUTA_ARCHIVO
    try:
        with open(RUTA_ARCHIVO, "r") as file:
            data = json.load(file)
        print("Datos cargados exitosamente!!")
    except Exception:
        print("Error al cargar datos")


import datos_graduados

def campers_graduadoss ():
    graduadoo={}
    graduadoo["nombre"]=input("Ingrese el nombre del campers graduado para guardarlo en la base de tatos graduados")
    
    datos_graduados.data.append(graduadoo)
    datos_graduados.guardar_datos()
    


def mostrar_camper_graduados():
    print("Los campers graduados son: ")
    for graduadoo in datos_graduados.data:
        print("Los campers son:" , graduadoo["nombre"])