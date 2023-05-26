FROM python:3.9

RUN apt-get update \
 && apt-get install nano \
 && pip install pip poetry --upgrade

COPY pyproject.toml /root/pipper/pyproject.toml
COPY poetry.lock /root/pipper/poetry.lock

RUN poetry config virtualenvs.create false \
 && poetry install
