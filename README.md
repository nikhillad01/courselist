# Back-End Development Assignment

Assingment to create backend server in Python/Django and an API to store Course Information (Course Name, Course Author Name and Price).

## Installation (Backend Server)

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install dependencies.
All the dependencies are mentioned in requirements.txt 

```bash
pip3 install -r requirements.txt
```

## DB migrations 

```bash
python3 manage.py makemigrations
python3 manage.py migrate

```
Above commands will generate DB models 

## Run Backend-Serverver
```bash
python3 manage.py runserver
```
##### URL structure :	/api/courses/	: API for all CRUD operations on courses.

Server will run on port 8000.





## Installation (Front-End Server)

Front end app is developed using React Js, yarn for package management and Axios for http requests , Go to front-end app directory and install required dependencies.

```bash
cd client/courselist/
yarn install or npm install
```


## Run Front-End-Serverver
```bash
yarn start or npm start
```
 By default server will run on port 3000 


