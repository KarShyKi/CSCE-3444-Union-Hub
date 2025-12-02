FROM python:3.10

WORKDIR /app

COPY . /app/

RUN pip install --no-cache-dir -r requirements.txt

# Collect static into /app/staticfiles
RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "unionhub_backend.wsgi:application", "--bind", "0.0.0.0:8000"]
