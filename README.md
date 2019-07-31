# Django Youtube Search Demo

## About

This is a demo project for practicing Django.
The idea was to build some basic blogging platform.

It was made using **Python 3.6** + **Django** and database is **SQLite**.
**Bootstrap** was used for styling.
Testing is done using **untitest** module.

There is a login and registration functionality included.

User has his own blog page, where he can add new blog posts. 
Every authenticated user can comment on posts made by other users.
Home page is paginated list of all posts.
Non-authenticated users can see all blog posts, but cannot add new posts or comment.

App is covered with tests.

## Prerequisites

\[Optional\] Install virtual environment:

```bash
$ python -m virtualenv env
```

\[Optional\] Activate virtual environment:

On macOS and Linux:
```bash
$ source env/bin/activate
```

On Windows:
```bash
$ .\env\Scripts\activate
```

Install dependencies:
```bash
$ pip install -r requirements.txt
```

## How to run

### Default

You can run the application from the command line with manage.py.
Go to the root folder of the application.

Run migrations:
```bash
$ python manage.py migrate
```

Initialize data:
```bash
$ python manage.py loaddata users posts comments
```

Run server on port 8000:
```bash
$ python manage.py runserver 8000
```

