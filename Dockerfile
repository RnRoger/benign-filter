FROM python:3.6

WORKDIR /app

COPY requirements.txt ./
COPY app.py ./
RUN pip install --upgrade pip &&\
    pip install numpy &&\
    pip install -r requirements.txt &&\
    apt-get update &&\
    apt-get install nano

EXPOSE 80

CMD ["python", "-u", "app.py"]