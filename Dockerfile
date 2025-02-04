FROM python:3.12-alpine


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update && apk add --no-cache \
    libpq \
    libpq-dev \
    gcc \
    musl-dev

WORKDIR /dogs

COPY requirements.txt ./
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

COPY dog_site/ .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]