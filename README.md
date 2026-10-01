# TaskFlow

## Django + PostgreSQL + Tailwind CSS Task Management Application

---

# 1. Overview

TaskFlow is a modern task management web application built with Django, PostgreSQL, and Tailwind CSS. It allows users to securely manage their daily tasks through a clean dashboard with complete CRUD functionality.

The application provides user authentication, task creation, task viewing, task editing, task deletion, task priorities, task statuses, due dates, and a responsive dashboard.

---

# 2. Features

## Authentication

* User registration
* User login
* User logout
* Password validation
* User-specific tasks
* Authentication-protected dashboard

## Task Management

* Create new tasks
* View all personal tasks
* Edit existing tasks
* Delete tasks
* Task priority management
* Task status management
* Due-date management
* Task descriptions

## Dashboard

* Total task count
* Completed task count
* Pending task count
* Tasks due today
* Recent task listing
* Personalized welcome message

## User Interface

* Responsive design
* Tailwind CSS
* Modern dashboard
* Responsive navigation bar
* Priority badges
* Status badges
* Flash messages
* Font Awesome icons
* Google Poppins font

---

# 3. Tech Stack

* **Python** — Backend programming
* **Django 5.2** — Web framework
* **PostgreSQL** — Database
* **Django ORM** — Database interaction
* **HTML5** — Frontend structure
* **Tailwind CSS** — UI styling
* **JavaScript** — Frontend interactions
* **python-dotenv** — Environment variables
* **psycopg2-binary** — PostgreSQL database driver
* **Font Awesome** — Icons
* **Google Fonts** — Typography

---

# 4. Project Structure

```text
TaskFlow/
│
├── config/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── todo/
│   ├── migrations/
│   │   ├── __init__.py
│   │   └── 0001_initial.py
│   │
│   ├── templates/
│   │   └── todo/
│   │       ├── dashboard.html
│   │       ├── add_task.html
│   │       ├── edit_task.html
│   │       └── delete_task.html
│   │
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   └── tests.py
│
├── templates/
│   ├── base.html
│   └── registration/
│       ├── login.html
│       └── register.html
│
├── static/
│   └── css/
│       ├── input.css
│       └── output.css
│
├── manage.py
├── requirements.txt
├── package.json
├── package-lock.json
├── .env
├── .gitignore
└── README.md
```

---

# 5. Application Architecture

```text
User
  ↓
HTML + Tailwind CSS Frontend
  ↓
Django Views
  ↓
Django ORM
  ↓
PostgreSQL Database
```

The user interacts with the frontend through HTML and Tailwind CSS.

Django views process the user's requests.

Django ORM communicates with the PostgreSQL database.

PostgreSQL stores the application's persistent data.

---

# 6. Database Model

The main model used in TaskFlow is the `Task` model.

```text
Task
│
├── id
├── user
├── title
├── description
├── priority
├── status
├── due_date
├── created_at
└── updated_at
```

### Priority Values

* High
* Medium
* Low

### Status Values

* Pending
* Completed

Each task is associated with a Django user so that users can access and manage only their own tasks.

---

# 7. CRUD Operations

TaskFlow implements complete CRUD functionality.

CRUD stands for:

* **C — Create**
* **R — Read**
* **U — Update**
* **D — Delete**

---

## 7.1 Create

Users can create a task by providing:

* Title
* Description
* Priority
* Status
* Due date

Flow:

```text
User
 ↓
Add Task
 ↓
Django Form
 ↓
Django View
 ↓
Django ORM
 ↓
PostgreSQL
```

---

## 7.2 Read

The dashboard retrieves tasks belonging to the logged-in user.

Flow:

```text
PostgreSQL
 ↓
Django ORM
 ↓
View
 ↓
dashboard.html
 ↓
User
```

---

## 7.3 Update

Users can select the **Edit** button to modify an existing task.

Flow:

```text
Dashboard
 ↓
Edit
 ↓
Edit Task Form
 ↓
Django View
 ↓
Database Updated
 ↓
Dashboard
```

---

## 7.4 Delete

Users can select the **Delete** button and confirm the operation.

Flow:

```text
Dashboard
 ↓
Delete
 ↓
Confirmation
 ↓
Django View
 ↓
Database
 ↓
Task Removed
```

---

# 8. Authentication Flow

TaskFlow uses Django's authentication system.

## 8.1 Registration

```text
Register
   ↓
Username + Email + Password
   ↓
Django UserCreationForm
   ↓
User Created
   ↓
Login
```

A new user provides their username, email address, and password.

Django validates the registration details and creates the user account.

---

## 8.2 Login

```text
Login Form
   ↓
Username + Password
   ↓
authenticate()
   ↓
login()
   ↓
Dashboard
```

The user enters their username and password.

Django checks the credentials.

If authentication is successful, the user is redirected to the dashboard.

---

## 8.3 Logout

```text
Logout
   ↓
logout()
   ↓
Login Page
```

When the user logs out, their authentication session is terminated and they are redirected to the login page.

Protected pages use Django's:

```python
@login_required
```

decorator.

---

# 9. Installation

## 9.1 Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/TaskFlow.git
cd TaskFlow
```

---

## 9.2 Create a Virtual Environment

```bash
python -m venv venv
```

---

## 9.3 Activate the Virtual Environment

### PowerShell

```powershell
venv\Scripts\Activate.ps1
```

### Command Prompt

```cmd
venv\Scripts\activate
```

After activation, the terminal should show something similar to:

```text
(venv) C:\Users\Admin\Downloads\TaskFlow>
```

---

# 10. Install Python Dependencies

If `requirements.txt` already exists:

```bash
pip install -r requirements.txt
```

If `requirements.txt` does not exist yet:

```bash
pip install django psycopg2-binary python-dotenv djangorestframework
```

Then generate the requirements file:

```bash
pip freeze > requirements.txt
```

---

# 11. PostgreSQL Setup

Create a PostgreSQL database named:

```text
taskflow_db
```

This can be done using pgAdmin or the PostgreSQL command line.

SQL command:

```sql
CREATE DATABASE taskflow_db;
```

The PostgreSQL server should be running before starting the Django application.

---

# 12. Environment Variables

Create a `.env` file in the project root.

Example:

```env
SECRET_KEY=your-django-secret-key
DEBUG=True

DB_NAME=taskflow_db
DB_USER=postgres
DB_PASSWORD=your_postgresql_password
DB_HOST=localhost
DB_PORT=5432
```

The `.env` file should not be uploaded to GitHub because it contains sensitive configuration such as the database password.

---

# 13. Django Database Configuration

In `config/settings.py`, load the environment variables:

```python
import os
from dotenv import load_dotenv

load_dotenv()
```

Then configure PostgreSQL:

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("DB_NAME"),
        "USER": os.getenv("DB_USER"),
        "PASSWORD": os.getenv("DB_PASSWORD"),
        "HOST": os.getenv("DB_HOST"),
        "PORT": os.getenv("DB_PORT"),
    }
}
```

This allows Django to connect to PostgreSQL using the values stored in `.env`.

---

# 14. Run Migrations

After configuring the database, run:

```bash
python manage.py makemigrations
```

Then:

```bash
python manage.py migrate
```

The migration system creates the required database tables.

---

# 15. Create Admin User

Create a Django administrator account:

```bash
python manage.py createsuperuser
```

Django will ask for:

```text
Username:
Email address:
Password:
Password (again):
```

After creating the account, the Django admin panel will be available at:

```text
http://127.0.0.1:8000/admin/
```

---

# 16. Tailwind CSS

Install the frontend dependencies:

```bash
npm install
```

Run Tailwind CSS in watch mode:

```bash
npx tailwindcss -i ./static/css/input.css -o ./static/css/output.css --watch
```

Keep the Tailwind terminal running while developing the frontend.

Tailwind watches the input CSS file and automatically generates the output CSS file when changes are made.

---

# 17. Run the Application

Open a terminal and navigate to the project directory:

```powershell
cd C:\Users\Admin\Downloads\TaskFlow
```

Activate the virtual environment:

```powershell
venv\Scripts\Activate.ps1
```

Start Django:

```bash
python manage.py runserver
```

You should see something similar to:

```text
Starting development server at http://127.0.0.1:8000/
```

Open the following address in your browser:

```text
http://127.0.0.1:8000/
```

---

# 18. Application Pages

## Dashboard

```text
http://127.0.0.1:8000/
```

The dashboard displays the user's tasks and task statistics.

---

## Registration

```text
http://127.0.0.1:8000/register/
```

Users can create a new account.

---

## Login

```text
http://127.0.0.1:8000/login/
```

Users can log into their TaskFlow account.

---

## Add Task

```text
http://127.0.0.1:8000/add-task/
```

Users can create a new task.

---

## Admin

```text
http://127.0.0.1:8000/admin/
```

Administrators can manage Django data through the Django admin interface.

---

# 19. Dashboard

The TaskFlow dashboard provides a personalized overview of the user's tasks.

It displays:

* Total Tasks
* Completed Tasks
* Pending Tasks
* Tasks Due Today

The dashboard also displays the user's task list.

Each task provides:

* Task title
* Priority
* Status
* Due date
* Edit button
* Delete button

The dashboard also contains an **Add Task** button for creating new tasks.

---

# 20. Security

TaskFlow uses several Django security features.

### CSRF Protection

Django CSRF tokens protect POST forms from Cross-Site Request Forgery attacks.

Example:

```html
{% csrf_token %}
```

---

### Password Hashing

Django does not store user passwords as plain text.

Passwords are securely hashed using Django's authentication system.

---

### Login Required

Protected pages use:

```python
@login_required
```

This prevents unauthenticated users from accessing protected functionality.

---

### User-Specific Tasks

Tasks are associated with users.

For example:

```python
task = get_object_or_404(
    Task,
    pk=pk,
    user=request.user
)
```

This ensures that the task belongs to the currently logged-in user.

It prevents a logged-in user from editing or deleting another user's task simply by changing the task ID.

---

### Environment Variables

Database credentials are stored in `.env` instead of directly inside the source code.

---

### Git Protection

The `.env` file should be included in `.gitignore`.

Example:

```gitignore
.env
venv/
__pycache__/
*.pyc
node_modules/
staticfiles/
```

---

# 21. Testing

Run Django's automated tests:

```bash
python manage.py test
```

You can also run Django's deployment configuration checks:

```bash
python manage.py check --deploy
```

---

# 22. Future Enhancements

The following features can be added to TaskFlow in future versions:

* Task search
* Priority filters
* Status filters
* Calendar view
* Task analytics
* Productivity charts
* Dark mode
* User profile
* Improved mobile navigation
* Task reminders
* Task export
* Pagination
* Task categories
* Task tags

---

# 23. Project Objective

The main objective of TaskFlow is to demonstrate how a complete web application can be developed using HTML and Tailwind CSS for the frontend, Django for the application layer, Django ORM for database interaction, and PostgreSQL for persistent data storage.

The project demonstrates:

* User authentication
* Database integration
* ORM-based CRUD operations
* Form handling
* Server-side validation
* User-specific data management
* PostgreSQL integration
* Responsive frontend design
* Tailwind CSS styling
* Django application architecture

TaskFlow combines these technologies to create a complete and practical task management web application.

---


