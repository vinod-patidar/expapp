# Expression Evaluate Backend API

## Table of Contents

- [Project Layout](#project-layout)
- [Setting up the expapp api project](#setting-up-the-expapp-project)
- [Setting up the expapp project manually](#setting-up-the-expapp-project-manually)

---

## Project Layout
  
  Here is the my project layout and Architecture:
  
  ```
  expapp
   |__ api/
   |__ myproject/
      |__ __init__.py/
      |__ .env
      |__ asgi.py
      |__ settings.py
      |__ urls.py
      |__ wsgi.py
   |__ .gitignore
   |__ manage.py
   |__ requirements.txt
   |__ README.md
  
  ```
  
  ## Setting up the `expapp` project
  
  Start by cloning the project with the command:
  ```
  $ git clone https://github.com/vinod-patidar/expapp.git
  ```
 
  ## Setting up the `expapp` project manually
  
  - setup the expapp api manually follow the directions below.
  
  - Go to the project root and start by installing the dependencies for the api:
  - Create virtual enviorment
  ```
  $ cd expapp/
  $ python -m venv env
  ```
  
  Let's activate the virtual enviorment first.
  - To run the below command and run in terminal from root directory:
  ```
  $ source env/bin/activate
  ```

  - Installing the dependencies for the api:
  ```
  $ cd expapp/
  $ pip install -r requirements.txt
  ```

  - Let's skip the database setup commands.

  Let's start the api backend server.
  - To run the below command and run in terminal from root directory:
  ```
  $ python manage.py runserver
  ```

  - Now, go to http://127.0.0.1:8000/ or http://localhost:8000/ in your browser.

  - That's it :)
 