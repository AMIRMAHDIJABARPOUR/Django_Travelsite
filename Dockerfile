FROM python:3.11

WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
COPY . .

CMD ["python", "manage.py", "runserver", "128.0.0.1:8000"]