FROM ubuntu:latest

RUN apt-get update

RUN apt install node

RUN apt install npm

RUN apt install python:3

RUN mkdir /code_dir

WORKDIR /code_dir

COPY . /code_dir/

RUN pip install -r requirements.txt

RUN npm install -g http-server

CMD ["http-server", "-s"]

