FROM python:3.8-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

COPY run_flask.sh /app/run_flask.sh

RUN chmod +x /app/run_flask.sh

CMD ["./run_flask.sh"]
