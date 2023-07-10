run:
	@docker-compose up

stop:
	@docker-compose down

test:
	@docker-compose run --rm app py.test

build: stop
	@docker-compose build app --no-cache

clean:
	@rm -rf `find . -iname __pycache__`
	@rm -rf `find . -iname .pytest_cache`

bash:
	@docker-compose run --rm app bash

migrate:
	@docker-compose run --rm app ./app/manage.py migrate
