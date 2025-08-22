import inquirer
from colorama import init, Fore
from tareas import agregar_tarea, mostrar_tareas, completar_tarea, eliminar_tarea

# Inicializar colorama
init(autoreset=True)

def menu():
    while True:
        opciones = [
            "Agregar tarea",
            "Ver tareas",
            "Completar tarea",
            "Eliminar tarea",
            "Salir"
        ]

        respuesta = inquirer.prompt([
            inquirer.List("opcion",
                          message="¿Qué querés hacer?",
                          choices=opciones)
        ])

        if not respuesta:
            print(Fore.RED + "No se seleccionó ninguna opción. Saliendo del programa.")
            break

        eleccion = respuesta["opcion"]

        if eleccion == "Agregar tarea":
            titulo = input("Título: ")
            descripcion = input("Descripción: ")

            respuesta_prioridad = inquirer.prompt([
                inquirer.List("prioridad",
                              message="Seleccioná la prioridad:",
                              choices=["alta", "media", "baja"])
            ])

            if not respuesta_prioridad:
                print(Fore.RED + "No seleccionaste una prioridad.")
                continue

            prioridad = respuesta_prioridad["prioridad"]
            agregar_tarea(titulo, descripcion, prioridad)

        elif eleccion == "Ver tareas":
            mostrar_tareas()

        elif eleccion == "Completar tarea":
            try:
                id_tarea = int(input("ID de la tarea a completar: "))
                completar_tarea(id_tarea)
            except ValueError:
                print(Fore.RED + "ID inválido. Debe ser un número.")

        elif eleccion == "Eliminar tarea":
            try:
                id_tarea = int(input("ID de la tarea a eliminar: "))
                eliminar_tarea(id_tarea)
            except ValueError:
                print(Fore.RED + "ID inválido. Debe ser un número.")

        elif eleccion == "Salir":
            print(Fore.CYAN + "¡Hasta luego!")
            break

if __name__ == "__main__":
    menu()
