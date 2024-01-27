ARG PORT=443

FROM cypress/browsers:latest AS builder

RUN apt-get update && apt-get install -y python3 python3-pip

COPY requirements.txt /app/
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

RUN alembic upgrade head

FROM cypress/browsers:latest

COPY --from=builder /app /app

WORKDIR /app

CMD uvicorn main:app --host 0.0.0.0 --port $PORT
