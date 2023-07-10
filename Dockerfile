FROM python:3.11.4-slim-buster

WORKDIR /app
COPY ./app /app/app
COPY ./pyproject.toml ./poetry.lock /app/
COPY ./tests /app/tests

RUN pip install --upgrade pip
RUN pip install poetry

RUN poetry config virtualenvs.create false
RUN poetry install
