FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

RUN mkdir /drfapi_app

WORKDIR /drfapi_app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN python app/manage.py makemigrations

RUN python app/manage.py migrate

CMD [ "python3", "app/manage.py", "runserver", "0.0.0.0:8000", "--noreload"]