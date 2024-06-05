import json

data = []

RUTA_ARCHIVO = "matriculass.json"

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


def matricula_camper ():
    matriculas={}
    print("Bienvenido a matriculas")
    print("Aqui ingresara a los camper que pasaron la prueba inicial ")
    matriculas["nom_matricula"]= input("nombre_del_camper")
    matriculas["Estado"]= "En proceso de inscricion"
 
    matriculas.data.append(matriculas)
    matriculas.guardar_datos()
   
    
def mostrar_camper_admitidos():
    print("Los Campers registrados son:")
    for matriculas in matriculas.data: 
        print("Camper que paso la prueba", matriculas["nom_matricula"], "En Estado" , matriculas ["Estado"])
