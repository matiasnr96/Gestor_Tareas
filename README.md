#  Gestor de Tareas con Prioridad

Este proyecto es un programa en Python que permite gestionar tareas con diferentes niveles de prioridad (**alta, media o baja**) desde una interfaz de consola interactiva. El usuario puede agregar nuevas tareas, ver todas las tareas, marcarlas como completadas y eliminarlas. Las tareas se guardan en un archivo `.json` y las acciones importantes se registran en un archivo de log.

---

##  Funcionalidades

- Agregar nuevas tareas con título, descripción y prioridad.
- Visualizar todas las tareas con colores según la prioridad.
- Marcar tareas como completadas.
- Eliminar tareas existentes.
- Persistencia de datos en archivo `tareas.json`.
- Registro de acciones (agregar, completar, eliminar) en `registro.log`.

---

##  Tecnologías y Librerías

- Python 3
- [`colorama`](https://pypi.org/project/colorama/): Para mostrar mensajes en colores en la consola.
- [`inquirer`](https://pypi.org/project/inquirer/): Para crear un menú interactivo usando flechas.
- [`logging`](https://docs.python.org/3/library/logging.html): Para registrar las acciones importantes del sistema (módulo estándar de Python).

---

## Estructura del Proyecto

```
gestor_tareas/
├── main.py             # Menú interactivo por consola
├── tareas.py           # Lógica para manipular las tareas
├── tareas.json         # Archivo donde se guardan las tareas (creado automáticamente)
├── registro.log        # Registro de acciones (creado automáticamente)
├── requirements.txt    # Librerías necesarias
└── README.md           # Este archivo
```

---

## Cómo ejecutar el programa

1. Cloná o descargá este repositorio.
2. Asegurate de tener Python 3 instalado.
3. Instalá las dependencias ejecutando:

```bash
pip install -r requirements.txt
```

4. Ejecutá el programa con:

```bash
python main.py
```

---

## Notas

- Si `tareas.json` o `registro.log` no existen, el programa los creará automáticamente.
- El menú funciona con flechas gracias a `inquirer`.
- El archivo de log (`registro.log`) incluye fecha, hora y acción realizada.

---

## Autor

Matías Rodríguez – Estudiante de la Tecnicatura en Análisis de Datos e IA – ISTEA

---
