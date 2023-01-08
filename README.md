# BookMyTicket

An Application to book movie tickets.  

## Description

The application has two users Theatre staff and users who book tickets. The theatre staff can Create, Update, Delete Movies and add Shows for each movie on any day. 
The end users can book tickets after creating an account. The application is developed using Django the database used is PostgreSQL. 

## UI Preview

User End / Customer / Booking App (gif @1fps)
![movie ticket project](https://user-images.githubusercontent.com/37036491/211182417-084e8044-2733-4272-ab7e-7c50ce8f5a89.gif)

Admin End / Theatre Staff (gif @1fps)
![movie ticket project 2](https://user-images.githubusercontent.com/37036491/211182565-7e12ab00-0f85-448a-be37-76fd35195167.gif)


## Getting Started

### Dependencies

Python, Pip, Virtualenv, Django, Other (psycopg2-binary, crispy-bootstrap5, django-crispy-forms, psycopg2, python-dotenv)
```
pip install -r requirements.txt
```

### Installing (Windows)
```
django-admin startproject movieticket
cd movieticket
django-admin startapp accounts
django-admin startapp staff
django-admin startapp booking
```
- add app names, 
- change default user model, 
- change database configuration (if needed) in .env file file.

### Executing program

```
Python manage.py runserver
```

## Authors
[Bhaksara](https://github.com/bhaskars9)

## License

This project is licensed under the MIT License - see the LICENSE.md file for details

## Acknowledgments

Inspiration, code snippets, etc.
* [StartBootstrap](https://github.com/StartBootstrap/startbootstrap-sb-admin)
* [Caroline Rodrigues](https://codepen.io/loracsilva/pen/ZrRYVL)
* [Pavlos](https://codepen.io/paulantoniou/pen/RdBogQ?editors=1100)
* [Coolors](https://coolors.co/02010a-04052e-140152-fff309-0d00a4)
