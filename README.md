# 📝 Task Manager

**Task Manager** es una aplicación web desarrollada con **Django**, diseñada para la gestión eficiente de tareas por parte de usuarios autenticados. Ofrece un sistema completo de autenticación, autorización y control de tareas personalizadas, con interfaces limpias y funcionalidades clave como panel de control, filtros y CRUD.

---

## 🚀 Funcionalidades Principales

- 🔐 **Autenticación y Autorización**  
  Registro, inicio y cierre de sesión de usuarios. Se asegura que cada usuario sólo pueda ver o modificar sus propias tareas.  
  > ⚠️ Si ves un error `403` tras iniciar sesión, intenta actualizar la página o reingresar.

- 👤 **Gestión de Usuarios**  
  Cada usuario puede gestionar únicamente sus tareas, protegiendo la privacidad y seguridad de los datos.

- 📋 **CRUD de Tareas**  
  Crear, editar y eliminar tareas propias. Cada tarea contiene título, descripción, estado, fechas y categoría.

- 🔍 **Listado y Filtro de Tareas**  
  Visualiza tareas en una lista filtrable por categoría y buscable por título. Ordenadas por fecha de creación.

- 📊 **Panel de Control (Dashboard)**  
  Página de inicio que muestra:
  - Tareas por estado: **Pendientes**, **En Proceso**, **Completadas**
  - Total de tareas
  - Tareas próximas a vencer en los siguientes 3 días

---

## ⚙️ Requisitos Previos

- [Python 3.13.1](https://www.python.org/downloads/)
- `pip` (gestor de paquetes de Python)
- Entorno virtual: `venv` o `pipenv` (opcional pero recomendado)
- `Git` (opcional para clonar el repositorio)

---

## 🛠️ Instalación y Configuración

### 1. Clonar el repositorio

```bash
git clone https://github.com/maleniadude/task_manager.git
cd task_manager/sistem
```

### 2. Crear y activar entorno virtual (opcional pero recomendado)

```bash
# En Windows
python -m venv env
.\env\Scriptsctivate

# En Linux/Mac
python3 -m venv env
source env/bin/activate
```

### 3. Instalar dependencias necesarias

```bash
pip install django pillow
```

### 4. Confirmar instalación

```bash
pip freeze
```

Debes ver algo como:

```
asgiref==3.8.1  
Django==5.1.4  
pillow==11.0.0  
sqlparse==0.5.3  
tzdata==2024.2  
```

### 5. Realizar migraciones

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Crear superusuario (opcional)

```bash
python manage.py createsuperuser
```

### 7. Iniciar el servidor de desarrollo

```bash
python manage.py runserver
```

El servidor estará disponible en:  
👉 http://127.0.0.1:8000/

---

## 📌 Notas Finales

- El panel de administración está disponible en `/admin` (requiere superusuario).
- La aplicación está pensada para expandirse con API REST (usando Django REST Framework) si se desea conectar con frontend en React, Flutter, etc.
- Si usas `django-widget-tweaks`, recuerda instalarlo y declararlo en `settings.py`.

---

¿Necesitas soporte o sugerencias?  
No dudes en abrir un **issue** o contactar al autor del proyecto. 💬
