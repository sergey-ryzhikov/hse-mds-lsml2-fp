FROM python:3.8-slim
ENV VIRTUAL_ENV="/opt/venv"
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN python3 -m venv $VIRTUAL_ENV \
    && pip3 install --no-cache-dir \
        numpy

COPY requirements.txt .
RUN pip3 install --requirement requirements.txt

RUN pip3 --no-cache-dir install torchvision

RUN mkdir -p /app
WORKDIR /app

COPY *.py .

CMD celery --app transform worker --autoscale 10 --loglevel=info
