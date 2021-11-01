FROM python:3.10
RUN apt update -y
RUN pip install --upgrade pip
RUN mkdir /modules
ADD requirements.txt /modules/
WORKDIR /modules
RUN pip install -r requirements.txt