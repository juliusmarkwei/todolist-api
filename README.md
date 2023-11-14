## Todo-List Web API

### Description

Building a TodoList API involves defining a database models and fields to represent tasks, users, and other relevant entities such as categories. This API is developed using Django Rest Framework. Protocols such as databse modelling, routing, HTTP status references codes, user management, serialization and signals are implemented in this project.

### Installation

In your terminal, navigate into any directory of your chooses, and clone the repository using the following command:

```
git clone https://github.com/juliusmarkwei/todolist-api
```

After cloning the repository:

```
cd "todolist-api/"
```

Run the commnad below to install the necessary dependencies. Make sure you have pip python manager installed correctly.

```
pip -r install requirements.txt
```

### Usage

After successfully installing all the project dependencies, go ahead and activate the database resources.
Load and migate the database models. Note that the database used is SQLite3. The default database for Django.
Run the following commands to achieve this:

```
python3 manage.py makemigrations
python3 manage.py migrate
```

Create an Admin User to able to manage Django Admin and create tasks.

```
python3 manage.py createsuperuser
```

#### Run the program

```
python3 manage.py runserver
```

### Contributing

In this project, JWT, routers and viewset, and many other REST API functionalities were not implemented because this was my first Django backend project of my Software Development journey and I haven't learnt those as of the time of this project. I will be dropping more huge projects in the future which utilizes most of the functionalities of the REST API development. feel free to modify or enhance this project in anyway.

### License

This project is licensed under the MIT License - see the <a href="https://github.com/juliusmarkwei/todolist-api/blob/main/LICENSE.md">LICENSE</a> file for details.

