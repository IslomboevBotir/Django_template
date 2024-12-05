FROM python:3.12

WORKDIR /app

RUN pip install --no-cache-dir poetry

COPY pyproject.toml poetry.lock /app/

RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

COPY . /app

ENV DJANGO_SETTINGS_MODULE=src.ofb_api.settings
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app

EXPOSE 8000

CMD ["poetry", "run", "gunicorn", "-b", "0.0.0.0:8000", "--chdir", "/app/src", "src.ofb_api.wsgi:application"]
