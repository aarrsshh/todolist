#To-Do List Implementation using Django

##Pre-requisite
* Python Binaries.
#### `Python version > 3.7`

* Django uses SQLite3 as backend database server.
#### `sqlite3 version > 3.7.17`

##Installation

* Install all required python packages.
#### `pip3 install -r requirement.txt`

* Create Migration file.
#### `python3 manage.py makemigrations ToDoList`

* Migrate Database.
#### `python3 manage.py migrate ToDoList`

##Test Application
To-Do List application have 4 test cases each perform CRUD operation.
* `C`: Create Entry into Database.
* `R`: Retrieve Entry from Database
* `U`: Update Entry in Database.
* `D`: Delete Entry from Database.

To Test the application against CRUD operation. Run below command:

#### `python3 manage.py test`


##Start Server
* If you want to run server on local machine only.
#### `python3 manage.py runserver`

* If you want to run server on local as well as remote machine.
#### `python3 manage.py runserver 0.0.0.0:8000`

##How To-Do:
* Task Creation date time is in accordance to Indian timezone. To change it perform below steps:
    * Open `ToDo` > `settings.py`.
    * Change `TIME_ZONE = 'Asia/Kolkata'` as per your needed timezone.