# task_manager
Este proyecto es el desarrollo de una aplicación web con django;
partiendo con el objetivo de gestionar tareas de usuarios, implementando relaciones entre modelos, autenticación y autorización, validaciones personalizadas, y manejo de vistas basadas en clases.
basándonos en un panel de control, una lista de tareas y un CRUD.

## Características Principales

- **Autenticación y Autorizacion**: Registro, login y logout de usuarios, obtención de tokens de acceso y refresco.
(de a ver error 403 al iniciar sesion, refrescar e intentar ingreso de nuevo)
- **Usuarios**: Creación, gestión unicamente de las tareas relacionadas con el usuario.
- **Tareas (tasks)**: Un usuario puede crear tareas, editarlas y eliminarlas; mientras sean suyas.
- **Lista de tareas (task_list)**: Cada tarea se puede visualizar en lista de tareas, buscar por titulo y filtrar por categoria, ordenadas por fecha de creacion.
- **panel de control (dashboard)**: tambien pagina de inicio, muestra el conteo de las tareas del usuario clasificadas por pendientes, en proceso, completadas; tambien el total de tareas y las que estan proximas a llegar a su fecha de vencimiento.

## Requisitos Previos

- **Python 3.13.1** (idealmente)
- Pipenv o venv (opcional, pero recomendado)
- Git (opcional)

## Instalación y Configuración

1. **Clonar el repositorio**:
   ```bash
   git clone https://github.com/maleniadude/task_manager.git

   cd task_manager

3. **Crear y activar entorno virtual (opcional)**:
   ```bash
    python -m venv env   # Windows
    python3 -m venv env   # Linux/Mac

    source env/bin/activate  # Linux/Mac
    .env\Scripts\activate    # Windows

4. **Instalar dependencias**:
    -necesitamos intalar django y pillow:
    ```bash
    pip install django

    pip installl pillow
    
    -confirmamos los paquetes:

    pip freeze

    -se tiene que ver algo asi:
    - asgiref==3.8.1
    - Django==5.1.4
    - pillow==11.0.0
    - sqlparse==0.5.3
    - tzdata==2024.2

5. **Asegurarnos de que no faltan migraciones por hacer**:
   ```bash
    python manage.py makemigrations

    python manage.py migrate

6. **Crear un superusuario (opcional)**:
   ```bash
    python manage.py createsuperuser

7. **Iniciar el servidor de desarrollo**:
   ```bash
    python manage.py runserver

- El servidor estará disponible en http://127.0.0.1:8000/
