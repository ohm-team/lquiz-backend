FROM python:3.7
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY app /app/
RUN pip install -r requirements.txt

ENV PYTHONPATH = $PYTHONPATH:/app/

CMD ["python", "/app/app.py"]