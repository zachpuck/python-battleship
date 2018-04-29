FROM python:3.6.5-alpine

RUN pip install flask flask_debugtoolbar

RUN mkdir app
WORKDIR /app
COPY ./app .

EXPOSE 8080/tcp

CMD [ "python", "web.py" ]
