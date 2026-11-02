FROM python:3.12-slim
WORKDIR /app

RUN pip install --no-cache-dir flask gunicorn

COPY app.py .
RUN useradd -m appuser && mkdir /logs && chown appuser /logs

USER appuser

CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
