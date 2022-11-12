FROM python:3.10-slim-bullseye

LABEL maintainer="Amogh Madan <amoghmadaan@gmail.com>"

WORKDIR /split-wiser

RUN apt-get update
RUN apt-get install -y gcc libssl-dev libmariadb-dev
RUN python3 -m pip install poetry

COPY ./pyproject.toml /split-wiser/
COPY ./poetry.lock /split-wiser/

RUN poetry config virtualenvs.create false
RUN poetry install --no-dev --no-root --no-interaction --no-ansi
