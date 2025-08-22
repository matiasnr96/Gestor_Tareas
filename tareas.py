import json
import logging
from colorama import init, Fore

# Inicializar colorama
init(autoreset=True)

# Archivo de tareas
ARCHIVO_TAREAS = 'tareas.json'

# Configuración de logging
logging.basicConfig(filename='registro.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def cargar_tareas():
    """Carga las tareas desde el archivo JSON."""
    try:
        with open(ARCHIVO_TAREAS, 'r') as file:
            tareas = json.load(file)
        return tareas
    except FileNotFoundError:
        # Si el archivo no existe, devolvemos una lista vacía
        return []
    except json.JSONDecodeError:
        # Si hay un error en el formato del JSON, devolvemos una lista vacía
        return []

def guardar_tareas(tareas):
    """Guarda las tareas en el archivo JSON."""
    with open(ARCHIVO_TAREAS, 'w') as file:
        json.dump(tareas, file, indent=4)

def agregar_tarea(titulo, descripcion, prioridad):
    """Agrega una nueva tarea a la lista."""
    tareas = cargar_tareas()
    nueva_tarea = {
        "id": generar_id_unico(tareas),
        "titulo": titulo,
        "descripcion": descripcion,
        "prioridad": prioridad,
        "estado": "pendiente"
    }
    tareas.append(nueva_tarea)
    guardar_tareas(tareas)
    logging.info(f"Tarea agregada: {nueva_tarea}")
    print(Fore.GREEN + "Tarea agregada con éxito!")

def generar_id_unico(tareas):
    """Genera un ID único para una nueva tarea."""
    if not tareas:
        return 1
    else:
        return max(tarea["id"] for tarea in tareas) + 1

def mostrar_tareas():
    """Muestra todas las tareas con sus detalles."""
    tareas = cargar_tareas()
    if not tareas:
        print(Fore.YELLOW + "No hay tareas registradas.")
        return

    for tarea in tareas:
        color = Fore.RED if tarea["prioridad"] == "alta" else Fore.YELLOW if tarea["prioridad"] == "media" else Fore.GREEN
        estado = Fore.CYAN + tarea["estado"].upper()
        print(color + f'ID: {tarea["id"]} | Título: {tarea["titulo"]} | Prioridad: {tarea["prioridad"].capitalize()} | Estado: {estado}')

def completar_tarea(id_tarea):
    """Marca una tarea como completada."""
    tareas = cargar_tareas()
    for tarea in tareas:
        if tarea["id"] == id_tarea:
            tarea["estado"] = "completada"
            guardar_tareas(tareas)
            logging.info(f"Tarea completada: {tarea}")
            print(Fore.BLUE + "Tarea completada con éxito!")
            return
    print(Fore.RED + "No se encontró una tarea con ese ID.")

def eliminar_tarea(id_tarea):
    """Elimina una tarea de la lista."""
    tareas = cargar_tareas()
    tareas = [tarea for tarea in tareas if tarea["id"] != id_tarea]
    guardar_tareas(tareas)
    logging.info(f"Tarea eliminada con ID: {id_tarea}")
    print(Fore.GREEN + "Tarea eliminada con éxito!")