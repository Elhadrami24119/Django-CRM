Django-CRM
A robust Customer Relationship Management (CRM) system built with Django. This application allows users to manage customer records, handle authentication, and perform CRUD (Create, Read, Update, Delete) operations through a clean web interface.

🚀 Features
User Authentication: Secure registration, login, and logout functionality.

Customer Management: Add, view, update, and delete customer records.

Responsive UI: Styled for use on both desktop and mobile devices.

Database Integration: Backend powered by MySQL/PostgreSQL (as configured in mydb.py).

🛠️ Tech Stack
Framework: Django (Python)

Database: MySQL / SQLite

Frontend: HTML5, CSS3, Bootstrap

📋 Prerequisites
Before running this project, ensure you have the following installed:

Python 3.x

pip (Python package manager)

Virtualenv

🔧 Installation & Setup
Clone the repository:

Bash
git clone https://github.com/Elhadrami24119/Django-CRM.git
cd Django-CRM
Create a virtual environment:

Bash
python -m venv venv
# Activate on Windows:
venv\Scripts\activate
# Activate on Mac/Linux:
source venv/bin/activate
Install dependencies:
(Note: Create a requirements.txt if you haven't yet, or install Django manually)

Bash
pip install django mysql-connector-python
Database Configuration:
Run the mydb.py script to initialize your database (if applicable):

Bash
python mydb.py
Run Migrations:

Bash
python manage.py migrate
Start the Server:

Bash
python manage.py runserver
Access the app at http://127.0.0.1:8000/.
