# Use an appropriate Alpine Linux base image with Python
FROM python:3.9-alpine

# Environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PORT=5000

# Setting the working directory
WORKDIR /app

# Copy any requirements and install dependencies
COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app source code into the container
COPY . /app/

# Define volume for persistent storage of data
VOLUME /app/data

# Port that the app will run on
EXPOSE $PORT

# Starting the Flask app with Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:create_app()"]





