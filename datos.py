import json

data = {}

RUTA_ARCHIVO = "gestioncamper.json"

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

def registrar_camper():
    global data 
    doc = int( input("Ingrese el documento: "))
    camper = {}
    camper["Nombre"] = input("Ingrese el nombre del camper: ")
    camper["apellido"] = input("Ingrese los apellidos del camper: ")
    camper["direccion"] = input("Ingrese la dirección del camper: ")
    camper["acudiente"] = input("Ingrese el nombre del acudiente del camper: ")
    try:
        camper["telefono"] = int(input("Ingrese el número de contacto: "))
    except ValueError:
        print("Ingrese un valor válido para el número de contacto!")
        return
    camper["estado"] = ("")
    camper["riesgo"] = ("")
    camper["ruta"] = ("")
    
    data[doc] = camper
    
    guardar_datos()
    
    
def estado_camper():
    global data
    doc = input("Ingrese el documento del camper al que se le asignara el estado: ")
    if doc in data:
        estado_del_camper = input("Ingrese el nuevo apellido: ")
        data[doc]["estado"] = estado_del_camper
        print("estado actualizado")
        guardar_datos()
    else:
        print("El documento ingresado no corresponde a ningún camper registrado.")
        
def riesgo_camper():
    global data
    doc = input("Ingrese el documento del camper al que se le asignara el estado: ")
    if doc in data:
        riesgocamper = input("Ingrese el nuevo apellido: ")
        data[doc]["riesgo"] = riesgocamper
        print("estado actualizado")
        guardar_datos()
    else:
        print("El documento ingresado no corresponde a ningún camper registrado.")
        
def ruta_camper():
    global data
    doc = input("Ingrese el documento del camper al que se le asignara el estado: ")
    if doc in data:
        rutacamper = input("Ingrese el nuevo apellido: ")
        data[doc]["riesgo"] = rutacamper
        print("estado actualizado")
        guardar_datos()
    else:
        print("El documento ingresado no corresponde a ningún camper registrado.")
        
        
def eliminar_camper():
    global data
    doc = input("Ingrese el documento del camper que desea eliminar: ")
    if doc in data:
        del data[doc]
        print("Camper eliminado exitosamente!!")
        guardar_datos()
    else:
        print("El documento ingresado no corresponde a ningún camper registrado.")
        
        
