.PHONY: init 

init: down up fixtures ps
down:
	docker-compose down --volumes --remove-orphans
pull:
	docker-compose pull
build:
	docker-compose build
up: pull build
	docker-compose up -d
ps:
	docker-compose ps
migrations:
	docker-compose run --rm core python manage.py makemigrations
migrate: migrations
	docker-compose run --rm core python manage.py migrate
fixtures: migrate
	docker-compose run --rm core python manage.py populatedb
su:
	 docker-compose run --rm core python manage.py createsuperuser
test:
	 docker-compose run --rm core python manage.py test
