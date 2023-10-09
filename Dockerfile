FROM python:3.8

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY ./app /app

# Adicione a configuração das variáveis de ambiente
ENV MONGO_HOST=localhost
ENV MONGO_PORT=27017
ENV MONGO_USERNAME=
ENV MONGO_PASSWORD=

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
