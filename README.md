# 📘 Student Enrollment System

A Django-based web application to manage **students** and their **course enrollments**, demonstrating the use of **relational databases** with **Primary and Foreign Keys**, full **CRUD operations**, and a clean **admin panel**.

---

## 🚀 Features

- 📚 Add, edit, delete students
- 📝 Enroll students into courses
- 🔗 Relational database using Foreign Keys
- 🧑‍💼 Django Admin panel for full control
- 🎨 Bootstrap-based UI
- ✅ Validation and feedback messages

---

## 🛠️ Tech Stack

- **Framework**: Django (Python)
- **Database**: SQLite3 (Default Django DB)
- **Frontend**: HTML, Bootstrap 5
- **Admin**: Django Admin Panel

---

## 🔄 Flow Summary

1. `Student` model – contains student info (name, age, email, etc.)
2. `Enrollment` model – links students to course names using a Foreign Key
3. Forms built with `ModelForm`
4. Templates render forms and lists using Bootstrap
5. Admin login allows backend management

---

## 🧪 How to Run Locally

```bash
# Clone the repository
git clone https://github.com/yourusername/student-enrollment.git
cd student-enrollment

# Create virtual environment
python -m venv env
source env/bin/activate  # On Windows: env\\Scripts\\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py makemigrations
python manage.py migrate

# Create superuser (for admin login)
python manage.py createsuperuser

# Start the server
python manage.py runserver
