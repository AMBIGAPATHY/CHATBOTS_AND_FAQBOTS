from django.shortcuts import render

from django.shortcuts import render

FAQS = {
    "What is Django?": "Django is a high-level Python web framework that follows the MVT (Model-View-Template) architecture.",
    "What is GPT-2?": "GPT-2 is an AI language model developed by OpenAI for generating human-like text.",
    "What is Python?": "Python is a high-level, interpreted programming language known for its simplicity and readability.",
    "What is an API?": "API (Application Programming Interface) is a set of rules that allows different software applications to communicate with each other.",
    "What is a database?": "A database is a structured collection of data that allows efficient storage, retrieval, and management of information.",
    "What is an ORM in Django?": "ORM (Object-Relational Mapping) in Django is a way to interact with the database using Python instead of SQL queries.",
    "What is MVT architecture?": "MVT (Model-View-Template) is Django's architecture pattern, separating data handling (Model), logic (View), and UI (Template).",
    "How does Django handle authentication?": "Django provides built-in authentication, including user login, logout, password management, and permission handling.",
    "What is middleware in Django?": "Middleware is a way to process requests before they reach the view and responses before they are sent to the client.",
    "What is Django REST Framework (DRF)?": "Django REST Framework is a toolkit for building web APIs in Django with authentication, serialization, and viewsets.",
    "What is CSRF protection in Django?": "Django includes CSRF (Cross-Site Request Forgery) protection to prevent unauthorized actions on behalf of users.",
    "How to install Django?": "Install Django using the command: `pip install django`.",
    "What is a Django model?": "A Django model is a Python class that defines the structure of database tables, fields, and relationships.",
    "What is a Django template?": "A Django template is an HTML file with dynamic placeholders for displaying data from views.",
    "What is Django migration?": "Django migrations are used to update the database schema based on changes in the models.",
    "What is Django Admin?": "Django Admin is a built-in interface for managing database records through a web-based UI.",
    "What is a Django form?": "A Django form is a Python class that helps handle user input, validation, and form rendering.",
    "How to run a Django project?": "Use the command: `python manage.py runserver` to start a Django project on a local server.",
    "What is static files handling in Django?": "Static files in Django (CSS, JS, images) are served using the `STATICFILES_DIRS` and `STATIC_URL` settings.",
    "What is Django cache?": "Django cache is a system for storing frequently accessed data to improve performance and reduce database load.",
    "What is Django Signals?": "Django Signals allow different parts of an application to communicate when certain events occur.",
    "What is Django Celery?": "Celery is an asynchronous task queue that integrates with Django for handling background tasks.",
    "What is Django Channels?": "Django Channels extends Django to support WebSockets, long polling, and asynchronous communication.",
    "How does Django handle sessions?": "Django stores session data in databases, cookies, or caches to manage user-specific data across requests.",
    "What is a Django view?": "A Django view is a function or class that handles HTTP requests and returns responses.",
    "How to deploy a Django app?": "Django apps can be deployed using AWS, Heroku, DigitalOcean, or other cloud platforms.",
    "What is Gunicorn?": "Gunicorn is a WSGI HTTP server for running Python web applications, commonly used with Django in production.",
    "What is WSGI?": "WSGI (Web Server Gateway Interface) is a standard for Python web applications to communicate with web servers.",
    "What is ASGI?": "ASGI (Asynchronous Server Gateway Interface) extends WSGI to support async features like WebSockets.",
    "What is Django ModelSerializer?": "ModelSerializer in Django REST Framework is used to automatically serialize and deserialize model instances.",
    "How to use Django with PostgreSQL?": "Install PostgreSQL and configure `DATABASES` in `settings.py` to use PostgreSQL as the database backend.",
    "What is a foreign key in Django?": "A foreign key in Django models creates a relationship between two tables in the database.",
    "How to reset Django migrations?": "Use the commands: `python manage.py migrate --fake` and `python manage.py makemigrations` to reset migrations.",
    "How to handle file uploads in Django?": "Use `FileField` or `ImageField` in Django models and configure `MEDIA_URL` and `MEDIA_ROOT` in settings.",
    "What is a Django signal?": "A Django signal allows functions to run automatically when certain actions occur in the application.",
    "How to create a custom Django command?": "Create a Python script inside `management/commands/` directory and use `BaseCommand` to define commands.",
    "What is Django Q?": "Django Q is an asynchronous task queue for managing scheduled and background tasks in Django.",
    "What is Django Haystack?": "Django Haystack is a search framework that integrates with search engines like Elasticsearch and Solr.",
    "What is Django CMS?": "Django CMS is a content management system (CMS) built on Django for managing websites easily.",
    "How to create a Django API?": "Use Django REST Framework (DRF) to create API views, serializers, and authentication for Django applications.",
}

def faq_view(request):
    query = request.GET.get("query", "")
    answer = FAQS.get(query, "Sorry, I don't have an answer for that.")
    return render(request, "faq_bot/faq.html", {"query": query, "answer": answer})

