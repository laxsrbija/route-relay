FROM python:3-slim

WORKDIR /app

COPY app.py requirements.txt ./
RUN install --no-cache-dir -r requirements.txt

EXPOSE 8080
CMD ["python", "app.py"]
