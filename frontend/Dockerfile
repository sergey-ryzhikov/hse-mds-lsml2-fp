FROM python:3.8-alpine

RUN pip install --upgrade pip 

RUN mkdir -p /app
WORKDIR /app

COPY ./requirements.txt /app/requirements.txt
RUN  pip install -r requirements.txt

COPY app/* /app

EXPOSE 5000
CMD [ "gunicorn", "-b 0.0.0.0:5000", "main:app" ]
# CMD [ "python3", "main.py" ]