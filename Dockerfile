FROM python:3.11.1-slim

COPY ./requirements.txt /src/requirements.txt

WORKDIR /src

RUN pip install --no-cache-dir --upgrade -r /src/requirements.txt

COPY ./src /src

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]