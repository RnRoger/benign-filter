FROM python:3.6

WORKDIR /app

COPY requirements.txt ./
RUN pip install numpy
RUN pip install -r requirements.txt 



EXPOSE 80

CMD ["python", "-u", "app.py"]
