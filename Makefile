DATABASE_NAME ?= hedsupforlife

.PHONY: clean reset rebuild install makemigrations migrate runserver test watch build up docker down sh shell 1024 format format_backend format_frontend format_sort sort sort_check sort_fix ruff ruff_check ruff_fix


reset:
	find . -path "*/hedsupforlife/*/migrations/*.py" -not -name "__init__.py" -delete
	find . -path "*/hedupforlife/*/migrations/*.pyc"  -delete

clean:
	find . -name '*.pyc' -delete
	find . -name '__pycache__' -delete
	find . -name '*.egg-info' | xargs rm -rf

rebuild:
	dropdb --if-exists $(DATABASE_NAME)
	createdb $(DATABASE_NAME)
	uv run manage.py migrate
	uv run manage.py initadmin

install:
	uv sync

makemigrations:
	uv run manage.py makemigrations

migrate:
	uv run manage.py migrate

runserver:
	uv run manage.py runserver

test:
	uv run pytest tests/ -vvv

watch:
	yarn watchify

build:
	docker compose -f docker-compose.yml build

up:
	docker compose -f docker-compose.yml up

docker:
	docker compose -f docker-compose.yml build
	docker compose -f docker-compose.yml up

down:
	docker compose -f docker-compose.yml down

sh:
	docker exec -it hedsupforlife-web-1 sh

shell:
	docker exec -it hedsupforlife-web-1 python manage.py shell

1024:
	# 1024 is the group id of the docker container
	sudo chown -R :1024 public/mediafiles
	sudo chmod -R 775 public/mediafiles
	sudo chmod g+s public/mediafiles
	sudo chown -R :1024 public/staticfiles
	sudo chmod -R 775 public/staticfiles
	sudo chmod g+s public/staticfiles

#
# Format / Lint targets
#
format: format_backend format_sort format_frontend

format_backend: ruff sort

format_frontend: prettier

format_sort: sort

sort: sort_fix

sort_check:
	uv run ruff check src tests --target-version=py311 --exclude=migrations --select I

sort_fix:
	uv run ruff check src tests --target-version=py311 --exclude=migrations --select I --fix

ruff: ruff_fix

ruff_check:
	uv run ruff check src tests --target-version=py39 --exclude=migrations

ruff_fix:
	uv run ruff check src tests --target-version=py39 --exclude=migrations --fix


