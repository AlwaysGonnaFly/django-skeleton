migrate:
	python manage.py makemigrations \
	&& python manage.py migrate

clean:
	find . -iname "*.pyc" -delete
	find . -iname "*.pyo" -delete
	find . -iname "__pycache__" -delete

clearcache:
	python manage.py invalidate_cachalot

collect:
	python manage.py collectstatic

createsuperuser:
	python manage.py createsuperuser