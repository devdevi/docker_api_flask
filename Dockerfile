FROM alpine:latest

RUN apk add --no-cache python3-dev \
    && pip3 install --upgrade pip


WORKDIR /api_flask

COPY api_flask/ .

RUN pip3 --no-cache-dir install -r requirements.txt

ENV FLASK_APP=app.py
ENV FLASK_ENV=development

EXPOSE 5000

CMD [ "flask", "run", "-h", "127.0.0.1", "-p", "5000" ]