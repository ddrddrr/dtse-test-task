FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PATH="/opt/bin:$PATH"

RUN apt-get update && apt-get install -y --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

COPY --from=ghcr.io/astral-sh/uv:0.7.11 /uv /uvx /bin/

WORKDIR /app
COPY ./docker/entrypoint.sh ./
RUN chmod +x entrypoint.sh

COPY pyproject.toml ./
COPY uv.lock ./

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --locked --group prod

COPY musikk ./

ENTRYPOINT ["./entrypoint.sh"]