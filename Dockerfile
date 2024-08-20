FROM python:3.12.5-alpine

WORKDIR /usr/src/app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["fastapi", "run"]

EXPOSE 8000