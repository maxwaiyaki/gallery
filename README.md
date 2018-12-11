[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/maxwaiyaki/pitch/blob/master/LICENSE)
[![Django](https://img.shields.io/badge/django-1.11-blue.svg)](https://www.djangoproject.com/)
[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)

# Flickr

 A personal gallery application that  displays photos for others to see.

### Live Link
You can preview the deployed application here 👉🏾 [Flickr](https://)

## Getting Started


### User Stories
- [x] View different photos that interest me.
- [x] Click on a single photo to expand it and also view the details of the photo. The photo details must appear on a modal within the same route as the main page.
- [x] Search for different categories of photos. (ie. Travel, Food)
- [x] Copy a link to the photo to share with my friends.
- [x] View photos based on the location they were taken.

### BDD
The program lets the admin upload photos
* Example input: Submit image form
* Example output: Image is shown on website

The program lets the user search for an image based on category
* Example input: Submit search form
* Example output: displays results based on search term

The program lets the user select images based on a location
* Example input: User selects specific location
* Example output: displays images for location selected

## Setup & Installation

### Prerequisites
Click on the any of the buttons to get instructions on how to install the technology on your local machine.
- [x] [![Git](https://img.shields.io/badge/git-2.17.1-rgb(245%2C%2077%2C%2039).svg)](https://git-scm.com/)
- [x] [![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)
- [x] [![Pip](https://img.shields.io/badge/pypi-v18.1-blue.svg)](https://pypi.org/project/pip/)
- [x] [![Virtualenv](https://img.shields.io/badge/virtualenv-16.1.0-brightgreen.svg)](https://virtualenv.pypa.io/en/latest/installation/)
- [x] [![Flask](https://img.shields.io/badge/flask-1.0.2-lightgrey.svg)](http://flask.pocoo.org/)
- [x] [![PostgreSQL](https://img.shields.io/badge/postgreSQL-11.1-darkblue.svg)](https://www.postgresql.org/)

### Installation ⬇️
To access this application locally on your machine, you'll need to clone it by typing this command to your terminal: ```
git clone https://github.com/maxwaiyaki/gallery.git```. 
You will then need to create a virtual enviroment inside your application  ``` python3.6 -m venv virtual``` and activate it ``` source virtual/bin/activate``` for you to install the dependacies of this application. Run the command ``` pip install -r requirements.txt ``` in your virtual enviroment to install all the required dependancies. You will also need to create a .env file using the format below.
Server the application using ``` python3.6 manage.py runserver ``` to view it on your local web browser.

### .ENV 
```python
#don't share your .env settings make sure you ignore them in your .gitignore file
SECRET_KEY='<Your SECRET_KEY>'
DEBUG=True #set to false in production
DB_NAME='<gallery>'
DB_USER='<YOUR DB USERNAME>'
DB_PASSWORD='<YOUR DB USERNAME>'
DB_HOST='127.0.0.1'
MODE='dev' #set to 'prod' in production
ALLOWED_HOSTS='.localhost', '.herokuapp.com', '.127.0.0.1'
DISABLE_COLLECTSTATIC=1
```

## Known Bugs 🐛
There are no known bugs yet but if you encounter a bug(s) create an issue stating the problem(s).

### Technologies used 💻
[![Django](https://img.shields.io/badge/django-1.11-blue.svg)](https://www.djangoproject.com/)
[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)
[![PostgreSQL](https://img.shields.io/badge/postgreSQL-11.1-darkblue.svg)](https://www.postgresql.org/)
[![HEROKU](https://img.shields.io/badge/heroku-v24-%239E7CC1.svg)](https://devcenter.heroku.com/articles/heroku-cli)
[![Git](https://img.shields.io/badge/git-2.17.1-rgb(245%2C%2077%2C%2039).svg)](https://git-scm.com/)
[![Bootstrap](https://img.shields.io/badge/bootstrap-4.0.0-purple.svg)](https://getbootstrap.com/)
[![Pip](https://img.shields.io/badge/pypi-v18.1-blue.svg)](https://pypi.org/project/pip/)
[![HTML5](https://img.shields.io/badge/html-html5-e34f26.svg)](https://www.w3schools.com/html/html5_intro.asp)

### Author 👨🏾
 **Maxwell Waiyaki** 

### License 📝
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/maxwaiyaki/pitch/blob/master/LICENSE) ©️ 2018