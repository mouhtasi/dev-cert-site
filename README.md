# Developer Certification Site

This site is a proof of concept. A user may enter Python code and the site will run it securely in a sandboxed environment. The result of the code is then compared to the expected result and returned to the user. This forms the basis of a code testing site.

## Getting Started

### Installing
The site:
```
$ sudo apt-get install postgresql postgresql-client
$ pip install Django psycopg2
```

The backend: Debian + Apparmor + virtualenv, will add more here soon.

## Deployment

## Deployment

```
$ python manage.py migrate
$ python manage.py collectstatic
```

Generate a [new secret key](https://www.miniwebtool.com/django-secret-key-generator/) and place it in bikeshare_tools/SECRET_KEY

Run the project with uWSGI:
```
$ uwsgi -ini uwsgi.ini
```
This will create a socket in the project folder which Nginx/Apache etc can proxy to.

If using nginx
```
location /devcert {
    uwsgi_pass  unix:/home/nap/fizzbuzzcert/fizzbuzzcert.sock;
    include     /home/nap/fizzbuzzcert/uwsgi_params;
  }

  location /devcert/static {
    alias /home/nap/fizzbuzzcert/fizzbuzzcert/static;
  }
```
will route for the URL domain.tld/devsite/

## Built With

* [Django 1.11](https://www.djangoproject.com/) - The web framework
* [PostgreSQL](https://www.postgresql.org/) - The database
* [AppArmor](http://wiki.apparmor.net/) - The Linux security system used to securely run the submitted code
* [CodeMirror](https://codemirror.net/) - Pretty code editor on the testing page

## Authors

* [Imad Mouhtassem](https://github.com/mouhtasi) - Initial Work
