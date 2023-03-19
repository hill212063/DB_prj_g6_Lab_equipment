FROM node:18.13

WORKDIR /src
COPY . .
RUN apt-get update && apt-get install build-essential -y

RUN npm install 
# Update packages 
#RUN apt-get update -y

#RUN apt-get install supervisor -y

COPY . .
#RUN python3 manage.py makemigrations

#RUN python3 manage.py migrate
EXPOSE 3000

CMD ["npm","run","dev"]
#CMD supervisord -c /src/supervisord.conf
