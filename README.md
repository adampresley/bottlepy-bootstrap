# bottlepy-bootstrap

**bottlepy-bootstrap** is my skeleton Bottle (Python) application bootstrap application. It
has basic setup for running a Bottle web application, model components, and unit tests. 

**Features**
* SQLAlchemy for database support
* Beaker for session middleware management
* Nose (with rednose for coloring) for running unit tests
* Fabric script to deploy to Amazon EC2 (using boto)
* jQuery 1.9.0
* Twitter Bootstrap 2.2.2

## Requisites 
```bash
$ sudo pip install SQLAlchemy
$ sudo pip install beaker
$ sudo pip install boto
$ sudo pip install nose
$ sudo pip install mock
$ sudo pip install rednose
$ sudo pip install coverage
$ sudo apt-get install fabric
```
