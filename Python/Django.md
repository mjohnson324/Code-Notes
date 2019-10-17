# Django Setup

* Basic Workflow: Model -> URL -> View -> Template

## Setup

1. Check Python version. Use pyenv or conda if needed.
2. Set up a virtual environment in your project
3. Install Django
4. To start a project: `django-admin startproject project`
5. Alter settings.py: TIME_ZONE, LANGUAGE_CODE, ALLOWED_HOSTS
6. Then run `python manage.py migrate`
7. Then: `python manage.py runserver`

## Useful Commands

* **Run Server:** python manage.py runserver
* **Run Migrations:** python manage.py migrate
* **Start new App:** python manage.py startapp _name_
* **Create Migrations:** python manage.py makemigrations _name_
* **Set Admin:** python manage.py createsuperuser
* **Shell:** python manage.py shell
* **Static File Optimization:** python manage.py collectstatic (CSS, etc.)

## ORM

* Django expects model fields to be set by default
* Do not use the default user model. Make a custom one.

* QuerySets - array-like object used to hold model objects. QuerySets can be chained

* Eager Loading: prefetch_related()
* Save:
  * commit=False prevents saving a model prematurely

## Django Rest Framework

### Authentication Strategies

1. Stateless (testing) - but requires constant password usage
2. HTTP (simple sites) - cookies used for auth; only allows single sessions
3. Signed Tokens (default) - Permits single validation and multiple sessions but does not expire
