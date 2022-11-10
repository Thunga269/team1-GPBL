FROM python:3.8

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 1337

USER 1000

CMD [ "python", "./server.py" ]
