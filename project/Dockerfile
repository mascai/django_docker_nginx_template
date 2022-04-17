FROM python:3.9-alpine

WORKDIR /project

# forbid .pyc file recording
# forbid bufferization
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONBUFFERED=1 

COPY . .

# install postgres, libs and forbid cache
RUN apk add --update  --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev && \
    pip install  -r requirements.txt

