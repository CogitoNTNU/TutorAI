# Use the official Python image from the Docker Hub
FROM python:3.11.2

# Make a new directory to put our code in.
RUN mkdir /code

# Change the working directory.
WORKDIR /code

# Copy only the requirements first
COPY requirements.txt /code/
RUN pip install -r requirements.txt

# Install Tesseract OCR using apt-get
RUN apt-get update && \
    apt-get install -y \
    build-essential \
    python3-dev \
    python3-setuptools \
    libgl1-mesa-glx \
    tesseract-ocr \
    tesseract-ocr-nor \
    make \
    gcc \
    && python3 -m pip install -r requirements.txt \
    && apt-get remove -y --purge make gcc build-essential \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/*


# Then copy the rest of the code
COPY . /code/

# Run the application:
CMD gunicorn --bind :8000 tutorai.wsgi --workers 1 --timeout 120