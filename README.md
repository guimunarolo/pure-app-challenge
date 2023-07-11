# Pure APP Challenge

[![Tests](https://github.com/guimunarolo/pure-app-challenge/actions/workflows/tests.yml/badge.svg)](https://github.com/guimunarolo/pure-app-challenge/actions/workflows/tests.yml)

## How to run

You can simply run the project using the `Makefile` with:

    make run

Or if you prefer:

    docker-compose up

The application runs using port 8000.

> To stop run `make stop` or `docker-compose down`

### Running tests

With `Makefile` with:

    make test

Or if you prefer:

    docker-compose run --rm app py.test

## Performance

Here are the performance results made with [django-silk](https://github.com/jazzband/django-silk).

![Screenshot 2023-07-11 at 16 01 28](https://github.com/guimunarolo/pure-app-challenge/assets/8931516/009cd755-bfaa-495d-b50f-3fd82d3f9b82)
