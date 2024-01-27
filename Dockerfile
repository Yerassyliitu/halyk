ARG PORT=443

FROM cypress/browsers:latest

RUN apt-get update && apt-get install -y python3 python3-pip

COPY requirements.txt /app/
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

# Копируем entrypoint.sh
COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

# Указываем entrypoint.sh в CMD
CMD ["/app/entrypoint.sh"]
