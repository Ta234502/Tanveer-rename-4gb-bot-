FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN apt update && apt install -y ffmpeg git

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python3", "bot.py"]
