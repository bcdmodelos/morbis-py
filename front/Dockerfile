FROM python:3.11

WORKDIR /app

COPY front/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY front /app
COPY data /app/data

CMD ["python", "app.py"]
