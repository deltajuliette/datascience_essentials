# Use the official lightweight Python image.
# https://hub.docker.com/_/python
FROM python:3.8-slim

# Copy all the files needed for the app to work
COPY requirements.txt serve.py cats_vs_dogs.h5 ./

# Install all the necessary libraries
RUN pip install -r requirements.txt

# Run the app!
CMD python serve.py