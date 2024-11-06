# Library Management System

A comprehensive Library Management System built using the Django web framework and MySQL database. This project allows libraries to manage books, members, and borrowing/returning transactions with a user-friendly interface and robust backend. It also includes user authentication, search functionality, and enhanced reporting features.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Project Structure](#project-structure)
---

## Project Overview

The Library Management System provides an efficient way for libraries to manage books and members, and track book borrowing and returning. This application is built using the Django framework and connected to a MySQL database to store book, member, and transaction data. The app includes a powerful user authentication system and a variety of management tools to enhance library operations.

## Features

1. **Book Management**: Add, update, delete, and search books.
2. **Member Management**: Add, update, delete, and search library members.
3. **Borrowing & Returning**: Track borrowing and return dates with real-time stock management.
4. **User Authentication**: Secure login and registration for librarians.
5. **Reporting & Analytics**: Generate reports on overdue books, current loans, and book availability.
6. **Search Functionality**: Search books and members by multiple fields.
7. **Stock Management**: Automatically updates book availability based on transactions.
8. **Responsive UI**: Built with Bootstrap for responsive design.

## Technologies Used

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, Bootstrap
- **Database**: MySQL
- **Authentication**: Django’s built-in authentication system

---

## Getting Started

### Prerequisites
To run this project, ensure you have the following installed:
- Python 3.7 or higher
- Django 4.x
- MySQL server
- Git (for version control)

---

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/library-management-system.git
   cd library-management-system

2. **Install Dependencies Use the requirements.txt file to install dependencies.**

    ```bash
    pip install -r requirements.txt

3. **Set Up MySQL Database**
    - Create a MySQL database named library_db.**
    - Update the DATABASES setting in settings.py with your MySQL credentials.
    ```python

      DATABASES = {
          'default': {
              'ENGINE': 'django.db.backends.mysql',
              'NAME': 'library_db',
              'USER': 'your_mysql_username',
              'PASSWORD': 'your_mysql_password',
              'HOST': 'localhost',
              'PORT': '3306',
          }
      }

4. **Run Migrations Initialize the database tables using Django migrations.**

    ```bash
    
    python manage.py makemigrations
    python manage.py migrate
    
5. **Create a Superuser Create an admin account to access the Django admin panel.**

    ```bash
    python manage.py createsuperuser

6. **Run the Server Start the Django development server.**

    ```bash
    python manage.py runserver

7. **Access the Application**  Open your browser and go to http://127.0.0.1:8000/ to start using the Library Management System.

## Usage
1. **Login as Admin**: Use your superuser credentials to log in.
2. **Navigate through Side Menu**: Access modules for managing books, members, and transactions.
3. **Add/Edit/Delete Books and Members**: Use the forms available in each module to manage records.
4. **Borrow and Return Books**: Track borrowing and returning with automatic stock updates.
5. **Generate Reports**: Access reports for analytics and tracking overdue books.

## Project Structure

```
library-management-system/
├── library/                       # Main application folder
│   ├── migrations/                # Database migrations
│   ├── templates/                 # HTML templates
│   │   ├── base.html              # Base template for layout
│   │   ├── landing_page.html      # Home page
│   │   ├── dashboard.html
│   │   ├── book_list.html         # Book-related templates
│   │   ├── add_book.html
│   │   ├── update_book.html
│   │   ├── delete_book.html
│   │   ├── member_list.html       # Member-related templates
│   │   ├── add_member.html
│   │   ├── update_member.html
│   │   ├── delete_member.html
│   │   ├── borrow_book.html       # Borrow-related templates
|   |   ├── borrowed_book.html
|   |   ├── return_book.html
|   |   ├── login.html             # Login user template
|   |   ├── register.html          # Register user template
|   |   └── report.html
│   ├── admin.py                   
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── test.py
│   ├── urls.py
│   └── views.py                   # Views for handling requests
├── library_management/            # Project folder with settings
│   ├── settings.py                # Project settings
│   ├── urls.py                    # URL routing
│   └── wsgi.py
├── manage.py                      # Django’s CLI tool
└── README.md

