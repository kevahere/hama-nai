#Nahamia-nai

#### By **ALPHA TEAM**

## Description
This application is meant for expatriates and any other individuals trying looking to live in the beautiful city of Nairobi. The essense of the application is to provide individuals with a sense of familiarity by providing a platform where they can find a footing with regards to where to stay, which places to visit, how to interact and move around in addition to making them generally comfortable with their environment. 

## Prerequsites
    - Python 3.6 required

## Set-up and Installation
    - Clone the Repo
    - Install python 3.6
    - Run chmod a+x start.py
    - Run ./start.py
    
## Dependencies
    - pip3 install -r requirements (dependencies)

## Technologies used
    - Python 3.6
    - HTML
    - Bootstrap
    -Postgresql
    -Heroku(hosting)

### Create a Virtual Environment
Run the following commands in the same terminal:
`sudo apt-get install python3.6-venv`
`python3.6 -m venv virtual`
`source virtual/bin/activate`

### Prepare environment variables
```bash
export DATABASE_URL='postgresql+psycopg2://username:password@localhost/nahamia'
export SECRET_KEY='Your secret key'
```
### The application does use Postgresql. To Run database Migrations, run the following: 
```
python manage.py db init
python manage.py db migrate -m "initial migration"
python manage.py db upgrade
```
### Running the app in development
In the same terminal type:
`python3 manage.py server`

Open the browser on `http://localhost:5000/`

### [License](LICENSE)
Copyright (c) **ALPHA TEAM**
