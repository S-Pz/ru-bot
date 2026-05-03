FROM python:3.12
WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ ./src/
WORKDIR /app

CMD ["python", "run.py"]