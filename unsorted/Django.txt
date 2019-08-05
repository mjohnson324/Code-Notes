Django Setup:

Command-Line:
Run Server: python manage.py runserver
Run Migrations: python manage.py migrate
Start new App: python manage.py startapp _name_
Create Migrations: python manage.py makemigrations _name_
Set Admin: python manage.py createsuperuser
Shell: python manage.py shell
Static File Optimization: python manage.py collectstatic (CSS, etc.)

ORM:
-Arrays of model objects are QuerySets. QuerySets can be chained
-commit=False prevents saving a model prematurely
-Django expects model fields to be set by default

-Do not use the default user model. Make a custom one.

-Workflow: Model -> URL -> View -> Template

Django Rest Framework:
Stateless- (testing) but requires constant password usage
HTTP- (simple sites) cookies used for auth; only allows single sessions
Signed Tokens- (default) Permits single validation and multiple sessions but does not expire

eager loading: prefetch_related()