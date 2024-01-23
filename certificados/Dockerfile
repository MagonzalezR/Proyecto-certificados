FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY installs.txt /app/requirements/
RUN pip install -r requirements/installs.txt