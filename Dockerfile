FROM python:3.10

WORKDIR /app

COPY . /app/

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["sh", "-c", "python manage.py migrate && python manage.py collectstatic --noinput && gunicorn unionhub_backend.wsgi:application --bind 0.0.0.0:8000"]

