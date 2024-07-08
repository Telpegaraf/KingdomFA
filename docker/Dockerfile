FROM python:3.11-slim as python

FROM python as python-build-stage

ENV POETRY_VERSION=1.8.3 PYTHONUNBUFFERED=1 PYTHONDONTWRITEBYTECODE=1

RUN apt-get update &&apt-get install --no-install-recommends -y \
    gcc \
    libc6-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

RUN curl -sSL https://install.python-poetry.org | python3 - \
    && ln -s /root/.local/bin/poetry /usr/local/bin/poetry

ENV POETRY_VIRTUALENVS_IN_PROJECT=false

COPY pyproject.toml poetry.lock ./

RUN poetry export -f requirements.txt --output requirements.txt --without-hashes \
    && pip wheel --wheel-dir /usr/src/app/wheels -r requirements.txt

FROM python:3.11-slim AS python-run-stage

RUN apt-get update && apt-get install --no-install-recommends -y \
    libffi-dev \
    libssl-dev \
    libgl1 \
    flac \
    && rm -rf /var/lib/apt/lists/*

COPY --from=python-build-stage /usr/src/app/wheels /wheels

RUN pip install --no-cache-dir --no-index --find-links=/wheels /wheels/* \
    && rm -rf /wheels

RUN pip install "uvicorn[standard]"

WORKDIR /app

COPY . .

COPY ./docker/start-asgi /start-asgi
RUN chmod +x /start-asgi

COPY ./docker/entrypoint /entrypoint
RUN chmod +x /entrypoint

ENTRYPOINT ["/entrypoint"]

CMD ["/start-asgi"]