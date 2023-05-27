FROM python:latest

WORKDIR /app

COPY bin .

RUN pip install -r requirements.txt

ENTRYPOINT [ "python" ]

CMD ["app.py"]
