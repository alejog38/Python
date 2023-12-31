FROM python:3.4-slim

RUN apt-get update && apt-get install -y \
		gcc \
		gettext \
		mysql-client \
		postgresql-client libpq-dev \
		sqlite3 \
	--no-install-recommends && rm -rf /var/lib/apt/lists/*

ENV DJANGO_VERSION 1.10

RUN pip install mysqlclient psycopg2 django=="$DJANGO_VERSION"