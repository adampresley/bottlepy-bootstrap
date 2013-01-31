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

## Directions
To start a new project follow these steps:

1. Create a directory for your application
2. Copy all the files and directories found in this repo into your new directory
3. Open a terminal, change directory to *app*, and run **./start.sh**
4. Open a browser and go to http://localhost:8080

## Layout
Here are the basics of how this is all layed out.

#### Configuration
The majority of the configuration is found in the **config.py** file found in the root
of this repository. Here you will find settings to turn on DEBUG mode, database connection
information, and session management information.

#### Domain Model
This bootstrap offers a basic domain model concept. Essentially you get a basic set
of classes for Service and DAO (Data Access Object) components. A factory object is
provided as a place for your application get easy access to all your service components.
An simple example service object is provided.

#### Application
The web application lives in the *app* directory. Here you will find controllers,
views, static resources (CSS, JS, images) and the primary WSGI startup script.
A sample controller and view are provided, as well as a Twitter Bootstrap
layout.

#### Unit Tests
The *tests* directory contains unit tests for testing your services, controllers, and
whatever else tickles your fancy. 

#### Bin
This is where scripts go. I have a basic script to deploy the application to servers
running on Amazon EC2 based on the tags **Name** and **env** (environment). It basically
assumes you have a Git repository on the EC2 instance, and are pulling updates. 

A CSS/JS bundle/minify script is also provided that will bundle and minify all CSS/JS
found in the main layout file, then replace the JS/CSS references in the layout to point
to the newly minified file.


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

## MIT License
Copyright (c) 2013 Adam Presley

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated 
documentation files (the "Software"), to deal in the Software without restriction, including without limitation 
the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, 
and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES 
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE 
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR 
IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Other Licenses
This section lists the licenses of software and/or software components included
in this repository.

* jQuery - MIT License
* Twitter Bootstrap - Apache License v2.0
* Bottle - MIT License
* YUI Compressor - BSD license (includes Rhino under Mozilla Public License, JArgs under JArgs BSD license)
