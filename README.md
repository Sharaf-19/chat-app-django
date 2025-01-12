# Django Chat App

A simple and efficient chat application built with Django, designed to demonstrate real-time communication functionality.

## Features

- Real-time chat messaging
- User authentication system


## Getting Started

Follow these steps to set up and run the project locally.

### Prerequisites

Ensure you have the following installed on your system:

- Python
- pip (Python package installer)
- A database (SQLite is supported by default)
- Virtualenv (optional, but recommended)

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/Sharaf-19/chat-app-django.git
   cd chat-app-django 
   ```
2. **Create a virtual environment (optional but recommended):**:
   
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```
3. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **setup the database**:
   Run the following commands to apply migrations and initialize the database:
   ```bash
   python manage.py migrate

5. **Create a superuser (optional, for admin access)**:
   ```bash
   python manage.py createsuperuser
   ```
   -Follow the prompt steps by giving your username, password and confirm password
6. **Run the development server**:
   ```bash
   python manage.py runserver
   ```
   The application will be accessible at http://127.0.0.1:8000/.
