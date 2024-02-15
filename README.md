How to run the application
  Please install the requiremnt mention under the requirements.txt file
  Activate the virtual environment by command :- source <venv_name>/bin/activate (django_demo_venv)
  Need to Activate the djnago local server by command :- python manage.py runserver (after come to proper directory)
  hit the local url :- http://127.0.0.1:8000/ (application is up and running)

Under this solution :-
  we are using the django rest as backend and created 4 CURD API for the Customer object
  under the application following API we craeted 
    1. api/customers --> GET customer list 
    2. api/customers --> POST new customer information
    3. api/customers/<customer_id> --> GET single customer information
    4. api/customers/<customer_id> --> PATCH update single customer information
    5. api/customers/<customer_id> --> DELETE delete single customer information

  Already uploaded rthe json file for the reference
    
