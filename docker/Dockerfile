# Stage 1: Build Stage
FROM python:3.11-slim as build

WORKDIR /app

COPY pyproject.toml poetry.lock /app/

RUN apt-get update && apt-get upgrade -y \
    && apt-get install --no-install-recommends -y \
    gcc \
    libc6-dev \
    curl \
    && curl -sSL https://install.python-poetry.org | python3 - \
    && poetry --version \
    && poetry install $(test "$DEPLOY_ENV" == production && echo "--only=main") --no-interaction --no-ansi --sync \
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
    && apt-get clean -y && rm -rf /var/lib/apt/lists/*

# Stage 2: Runtime Stage
FROM python:3.11-slim as runtime

ARG DEPLOY_ENV

ENV DEPLOY_ENV=${DEPLOY_ENV} \
    PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    # Poetry's configuration:
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_CACHE_DIR='/var/cache/pypoetry' \
    POETRY_HOME='/usr/local' \
    POETRY_VERSION=1.8.3

WORKDIR /app

COPY . /app

RUN apt-get update && apt-get install --no-install-recommends -y \
    libffi-dev \
    libssl-dev \
    libgl1 \
    flac \
    curl \
    && curl -sSL https://install.python-poetry.org | python3 - \
    && export PATH="/root/.local/bin:$PATH" \
    && poetry --version \
    && poetry install $(test "$DEPLOY_ENV" == production && echo "--only=main") --no-interaction --no-ansi \
    && rm -rf /var/lib/apt/lists/*

# Entrypoint
COPY ./docker/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

# ASGI
COPY ./docker/start-asgi /start-asgi
RUN sed -i 's/\r$//g' /start-asgi
RUN chmod +x /start-asgi

ENTRYPOINT ["/entrypoint"]