# WisconsinDistrictMap
A web application showing various district maps of Wisconsin and how they fare in gerrymandering metrics.

The application has two components, a Django backend as well as an Angular server to run the front end and its own backend compiler.

## Prerequisites
- Node v8.9.4 LTS
- NPM
- Angular CLI (not required but recommended)
- Django
- Python 3
- Pip
- SQLite (Usually bundled with Django Install)

## Running Front End
1. Open a terminal window in angular/WIdistricting
2. Run ``` npm install ``` to install necessary dependencies
3. Run ``` npm start ``` for a webserver that accessible from the LAN or WAN, otherwise you can run ``` ng start ``` for local viewing. ```ng start``` makes the webserver only accessible from the local machine.

## Running Backend
1. Open a terminal window in django/WIdistricting
2. Run ```pip3 install django-nose nose django-cors-headers``` to install the testing library and the cross domain authorization library. Please note that the application is currently configured to report to TeamCity, our CI utility. You may not see an output when ```manage.py test``` is run.
3. Run ```python manage.py runserver```
