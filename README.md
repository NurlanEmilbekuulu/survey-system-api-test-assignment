# survey-system-api-test-assignment

## Technologies
* Django 4.0.2
* Django REST framework 3.13.1
* Docker

## Starting the service
* To run in a docker-container it is necessary to:
    
    0). add .env file to project folder as shown in .env-sample file
  
    1). run the service 
    ```
    docker-compose up -d --build
    ```
    2). create an administrator
    ```
    docker-compose exec web python3 manage.py createsuperuser
    ```
    3). check the service work: http://localhost:8000/

## Documentation

http://localhost:8000/redoc/
http://localhost:8000/swagger/
