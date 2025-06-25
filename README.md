1. Project Overview
    This is a Django REST API project with a lightweight frontend using HTML, CSS, and JavaScript. It uses MySQL as the database

2. Environment Setup:
    * Open your terminal and navigate to your project directory.
    * Create a virtual environment:
        python -m venv venv
    * Activate the environment:
        venv\Scripts\activate
      
3. Install Dependencies:
     pip install django djangorestframework mysqlclient

4. Configure MySQL Database:
     * In your Django project’s settings.py, locate the DATABASES section.
     * Replace it with your MySQL configuration:
          DATABASES = {
             'default': {
                 'ENGINE': 'django.db.backends.mysql',
                 'NAME': 'your_db_name',
                 'USER': 'your_username',
                 'PASSWORD': 'your_password',
                 'HOST': 'localhost',
                 'PORT': '3306',
           }
       }

      * Ensure your MySQL service is running and that the specified database is created.

5. Database Migration:
      * Create migration files:
           python manage.py makemigrations
      * Apply migrations to create tables:
           python manage.py migrate

6. Run the Django Server:
       * Launch the development server:
           python manage.py runserver 8080
       * Open your browser and go to:
           http://127.0.0.1:8080/

7. Access the API:
       * The REST API endpoint for messages is:
           http://127.0.0.1:8080/api/messages/
       * Use HTTP methods like:
           i.GET to fetch messages
           ii.POST to submit new ones

8. Frontend Details:
        * frontend interface is a simple HTML page served with Django templates.
        * JavaScript sends form data to the API using fetch().
        * CSS is used to style the form (no external libraries or frameworks involved).  
   
        
        
  
        
    
      
 
