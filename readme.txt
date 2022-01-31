## Customer Management System
- Using this App you can manage a customer data very easily.


## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Screenshots](#screenshots)
* [Setup](#setup)
* [Project Status](#project-status)
* [Room for Improvement](#room-for-improvement)
* [Acknowledgements](#acknowledgements)
* [Contact](#contact)


## General Information
- Customer Management System is a system design to make the customr Management a easy task.
- This app can store information on customers and lets them add, edit or delete items
- Using Admin pannel admins can manage the cutomers and access some information which are restricted to customers


## Technologies Used
- html5 
- css 
- bootstrap 4
- django 3.1.7
- python 3.9.6


## Features
- customers have attractive register page that thet can register their username and password to create a customer account
- on the login page both customers and admins can login by using username and the password
- on the login page both customers and admins can recover their password if forgotten
- for customers they can see the total orders ,orders pending and orders delivers on the screen
- cutomers can view the products but they are not allowed to update or change the details of the products
- bith customers and admins can logout using logout button
- both customers and admins can edit customer data but admins are not allowed to delete customer data
- admins can view the list of all the customers and their information seperately
- admins can view total orders and their information as total in the main page
- admins can add new products to the system but only root user is allowed to delete products


## Screenshots
- please look at the screenshots folder to see the screenshots


## Setup
project requirements/dependencies
1. django 3.1.7
2. django-filters
3. pillow
4. python-decouple 3.5

Installing project requirements/dependencies
- django 3.1.7 :
    install using " pip install Django " command 
    check your django version using " python -m django --version "

- django-filters :
    django-filter can be installed from PyPI with tools like " pip install django-filter " 
    Then add 'django_filters' to your INSTALLED_APPS.
*   INSTALLED_APPS = [
*       ...
*       'django_filters',
*   ]

- pillow :
    this python imaging library adds image processing capabilities to your Python interpreter.
    install using " pip install pillow " command 
    pillow requires python >=3.7

- python-decouple :
    Decouple helps you to organize your settings 
    so that you can change parameters/passwords without having to redeploy your app.
    install using " pip install python-decouple " command
    your dotenv (.env) file need to contain 
*ADMIN_EMAIL="your email"
*ADMIN_PW="your password"


## Project Status
Project is:  _complete_ 


## Room for Improvement
Include areas you believe need improvement / could be improved. Also add TODOs for future development.

Room for improvement:
- giving admins more freedom over products (currently only root user can edit or delete new products)
- eliminating redundant code

To do:
- add edit and delete new products for admin user
- refactor code for better preformence
- adding custom css to make the screens look better


## Acknowledgements
Give credit here.
- This project was inspired by dennis ivy's django crash course
- This project was based on dennis ivy's django crash course
- Many thanks to web dev simplified , dennis ivy


## Contact
Created by Shashika Danasekara - feel free to contact me! @ https://www.linkedin.com/in/shashika-danasekara/
