FROM python:3.12-slim

WORKDIR /

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN playwright install
RUN playwright install-deps

COPY . .

EXPOSE 5000

CMD ["python", "main.py", "start-api"]
