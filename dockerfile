FROM python:3.10-slim-buster
WORKDIR /get_wb_price_bot
COPY requirements.txt .
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
RUN apt-get update && apt-get install -y \
    vim \
    wget \
    unzip \
    libglib2.0-0 \
    libnss3 \
    libgconf-2-4 \
    xvfb \
    --no-install-recommends
RUN wget https://dl.google.com/linux/chrome/deb/pool/main/g/google-chrome-stable/google-chrome-stable_134.0.6998.35-1_amd64.deb \
    && dpkg -i google-chrome-stable_134.0.6998.35-1_amd64.deb \
    || apt-get install -f -y \
    && dpkg -i google-chrome-stable_134.0.6998.35-1_amd64.deb \
    && rm google-chrome-stable_134.0.6998.35-1_amd64.deb
RUN wget https://storage.googleapis.com/chrome-for-testing-public/134.0.6998.35/linux64/chromedriver-linux64.zip
RUN unzip chromedriver-linux64.zip
RUN chmod +x /chromedriver-linux64/chromedriver
RUN apt-get clean && rm -rf /var/lib/apt/lists/*
COPY . .
CMD ["python", "src/main.py"]