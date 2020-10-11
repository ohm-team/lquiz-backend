FROM python:3.7
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY lquiz-backend /app/lquiz-backend
COPY conf /app/lquiz-backend/conf
COPY data /app/data
RUN pip install -r /app/lquiz-backend/requirements.txt

ENV PYTHONPATH = $PYTHONPATH:/app/

CMD ["python", "/app/lquiz-backend/app.py"]