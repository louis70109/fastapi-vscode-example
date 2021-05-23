FROM python:3.7-alpine

COPY requirements.txt /requirements.txt
RUN apk update --no-cache \
&& apk add build-base postgresql-dev libpq --no-cache --virtual .build-deps \
&& pip install --no-cache-dir --upgrade pip \
&& pip install --no-cache-dir -r requirements.txt \
&& apk del .build-deps
RUN apk add postgresql-libs libpq --no-cache

RUN pip install -r requirements.txt

WORKDIR /app
COPY . /app
EXPOSE 80
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]