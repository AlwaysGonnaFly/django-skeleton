dev:
	pip install -r requirements/base.txt \
	&& pip install -r requirements/development.txt

prod:
	pip install -r requirements/base.txt \
	&& pip install -r requirements/production.txt

all:
	pip install -r requirements/base.txt \
	&& pip install -r requirements/development.txt \
	&& pip install -r requirements/production.txt

clean:
	find . -iname "*.pyc" -delete
	find . -iname "*.pyo" -delete
	find . -iname "__pycache__" -delete

migrate:
	python manage.py makemigrations \
	&& python manage.py migrate

clearcache:
	python manage.py invalidate_cachalot

collect:
	python manage.py collectstatic

createsuperuser:
	python manage.py createsuperuser