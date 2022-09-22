FROM python:3.9-slim-buster

COPY . .

RUN python3 -m pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]