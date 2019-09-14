
help:
	@echo  "usage: make <target>"
	@echo  "Targets:"
	@echo  "    up				Update requirements files."
	@echo  "    deps			Ensure dependencies are installed."
	@echo  "    run				Runs the runserver, and installs all dependencies."
	@echo  "    migrate			Runs python manage.py migrate"
	@echo  "    su				Runs python manage.py createsuperuser"

up:
	@pip-compile -o requirements.txt etc/requirements.in -U
	@pip-compile -o requirements_dev.txt etc/requirements_dev.in -U

deps:
	@pip install -q pip-tools
	@pip-sync requirements_dev.txt

migrate:
	@python manage.py migrate

su:
	@python manage.py createsuperuser

run: deps
	./manage.py runserver 0.0.0.0:8010
