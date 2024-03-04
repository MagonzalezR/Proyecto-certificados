FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY installs.txt /app/requirements/
RUN pip install -r requirements/installs.txt
RUN wget https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.4/wkhtmltox-0.12.4_linux-generic-amd64.tar.xz
RUN tar xvf wkhtmltox-0.12.4_linux-generic-amd64.tar.xz
RUN mv wkhtmltox/bin/wkhtmlto* /usr/local/bin
RUN apt-get update && apt-get install -y --no-install-recommends \
    openssl libssl-dev libxrender-dev libx11-dev libxext-dev libfontconfig1-dev libfreetype6-dev fontconfig
