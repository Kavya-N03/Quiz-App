# Django Quiz Application

This is a **full-stack Django web application** built using Django templates and static files.  
The project allows users to take quizzes based on categories, answer multiple-choice questions, and view results.

## Project Overview
- User authentication (Login & Registration)
- Category-wise quizzes
- Multiple-choice questions
- Score evaluation after quiz submission
- Admin panel for managing quizzes and questions

## Database Models
The application uses a relational database structure:

- **Category** → Groups quizzes  
- **Quiz** → Linked to a category  
- **Question** → Linked to a quiz  
- **Answer** → Linked to a question (with correct answer flag)

Foreign key relationships are used to maintain proper data integrity.

## Tech Stack
- Django
- Django ORM
- HTML, CSS, JavaScript
- SQLite (default)

## Run Project Locally
```bash
git clone https://github.com/Kavya-N03/Quiz-App.git
cd Quiz-App
python -m venv env
env\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
