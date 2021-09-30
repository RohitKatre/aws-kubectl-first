FROM python:3.7-slim-buster

WORKDIR /code

RUN pip install Flask

COPY ./ /code/

EXPOSE 5000

# set environment variable
ENV FLASK_APP=main

CMD ["flask", "run", "--host", "0.0.0.0", "--port", "5000"]