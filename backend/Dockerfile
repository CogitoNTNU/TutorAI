# Use the official Python image from the Docker Hub
FROM python:3.11.2

# Make a new directory to put our code in.
RUN mkdir /code

# Change the working directory.
WORKDIR /code

# Copy only the requirements first
COPY requirements.txt /code/
RUN pip install -r requirements.txt

# Then copy the rest of the code
COPY . /code/

# Run the application:
CMD gunicorn --bind :8000 tutorai.wsgi --workers 1 --timeout 120