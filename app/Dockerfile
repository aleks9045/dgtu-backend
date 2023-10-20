FROM python:3.10-alpine3.17

ENV PYTHONDONTWRITEBYTECODE 1
# Если проект крашнется, выведется сообщение из-за какой ошибки это произошло
ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt && alembic revision --autogenerate && alembic upgrade head

COPY .. .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]