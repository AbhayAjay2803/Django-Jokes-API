Documentations for setting up and running the Django Application:
1. Set up Environment:
  a) Install Django using 'pip install django'
  b) Create a new Django Project and application using the commands mentioned below
  python -m venv venv
  venv\Scripts\Activate(Windows) or source venv/bin/activate(MacOS)
  c) Only if you want to create the project from scratch follow this
  django-admin startproject myproject
  cd myproject
  django-admin startapp myapp
2. Running the server 
   Navigate to the project directory and run 'python manage.py runserver'
3. APIs
   a) Greet User API:
   URL: 'http://127.0.0.1: 8000/greet/?name=YourName'
   Method: GET
   Response: JSON Message with Greeting
   b) Process Form API
   URL: 'http://127.0.0.1: 8000/process_form'
   Method: GET for form, POST for Submission
   Validations: Name(non-empty String), Age(Positive integer), Salary(positive number)
   c) Fetch Jokes API:
   URL: 'http://127.0.0.1: 8000/fetch_jokes/'
   Method: GET for form, POST for Submission
   Validations: Count(1-10)
4. Explaination of Form Validation Logic:
   a) UserForm: 
   name: Ensures the field is a non-empty string
   age: Ensures the field is a positive integer using min_value=0
   salary: Ensures the field is a positive number using min_value=0
   b) JokesForm:
   Count: Ensures the field is a positive integer between 1 and 10 using min_value=1 and max_value=10 