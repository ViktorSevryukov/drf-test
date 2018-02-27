# DRF TEST PROJECT

Application for working with clients through the django framework, with the ability to export a list of clients to the file.


### Features
  - CRUD operations clients
  - Vote page
  - Export clients list to .xls file

### Project apps
  - auth_core
  - base
  - clients


### Installation

Install the dependencies and start the server.

```
$ make init
$ source venv/bin/activate
$ python src/manage.py migrate
$ python src/manage.py runserver
```

### Additional info

#### Install rabbitmq (celery)
Mac OS:
```
brew install rabbitmq
```
Linux:
```
sudo apt-get install rabbitmq-server
```