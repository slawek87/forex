FROM python:3.6

ADD src      /var

WORKDIR /var
RUN pip install --upgrade pip setuptools
RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["app.py"]

