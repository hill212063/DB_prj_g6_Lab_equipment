FROM python:3.11

WORKDIR /src

COPY requirements.txt .

RUN pip install -r requirements.txt


RUN apt-get update && apt-get install build-essential -y

RUN apt-get install -y mariadb-client

# Update packages 
#RUN apt-get update -y

#RUN apt-get install supervisor -y

COPY . .
#RUN python3 manage.py makemigrations

#RUN python3 manage.py migrate
EXPOSE 8000

CMD ["python3","manage.py","runserver","0.0.0.0:8000"]
#CMD supervisord -c /src/supervisord.conf
