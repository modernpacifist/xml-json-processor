FROM python:3.10-alpine

RUN mkdir -m 777 /app

WORKDIR /app

COPY ./src .

RUN pip install poetry==1.7

RUN poetry install

ENTRYPOINT ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
