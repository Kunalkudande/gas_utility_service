# Gas Utility Service

This is a Backend Project built with Django and containerized with Docker to help people request gas utility services online. Customers can send requests, track them, and see their account info. Staff can manage these requests.

## What You Need to Run It
- Docker (to run the app in a container)
- Docker Compose (to manage the app and services)

## How to Run It on Your Computer
1. **Get the Code**  
   Download the project from GitHub or use this command: git clone https://github.com/Kunalkudande/gas_utility_service.git
   Then go into the project folder:    cd gas_utility_service

2. **Start the App with Docker**  
Build and run the app using this command:    docker-compose up --build

It might take a minute to set up.

3. **Open the App**  
Go to `http://127.0.0.1:8000/` in your browser to see the app.

## Main Pages to Try
- `/submit/`: Send a new request (you need to log in first).
- `/track/`: See your requests (you need to log in).
- `/manage/`: For staff to see and update all requests (you need staff access).
- `/admin/`: For admins to manage everything (you need a superuser account).

## How to Make an Admin Account
To log in as an admin or staff, create a superuser account:  docker-compose exec web python manage.py createsuperuser

Follow the steps to set a username, email, and password.

## About the Project
- Made with Django 5.1.7
- Uses SQLite to store data (like a small database)
- Runs in Docker so it works the same everywhere

