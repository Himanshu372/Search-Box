FROM ubuntu:16.04

RUN apt-get update && apt-get install -y \
nodejs npm python3 python3-pip

RUN ln -s /usr/bin/nodejs /usr/bin/node

RUN mkdir /code_dir

WORKDIR /code_dir

COPY . /code_dir/

RUN pip3 install -r requirements.txt

RUN npm install -g http-server

CMD ["http-server", "-s"]

