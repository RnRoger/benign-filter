FROM python:3.6

WORKDIR /app

COPY requirements.txt ./
COPY app.py ./
COPY Snakefile ./
RUN pip install --upgrade pip &&\
    pip install numpy &&\
    pip install -r requirements.txt &&\
    pip install Snakemake





EXPOSE 80

#CMD ["python", "-u", "app.py"]
CMD ["snakemake", "-n"]