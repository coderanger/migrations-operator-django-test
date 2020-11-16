FROM python:3.8
LABEL org.opencontainers.image.source https://github.com/coderanger/migrations-operator-django-test

WORKDIR /app
COPY . ./
RUN python -m pip install -r requirements.txt

USER 65534:65534
CMD ["python", "-m", "kubernetes_wsgi", "migrationtest.wsgi"]
