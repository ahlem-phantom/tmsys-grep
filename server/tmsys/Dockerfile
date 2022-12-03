FROM python:3.7.6-stretch

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 5000

ENV FLASK_ENV=production    

CMD python run.py
