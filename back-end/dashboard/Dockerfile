# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt /app/

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt


# Copy the rest of the application code into the container
COPY . /app/

# Expose the port the app runs on
EXPOSE 8000

# Define environment variable
ENV DJANGO_SETTINGS_MODULE=dashboard.settings

# Run the command to start the Django server
CMD ["gunicorn", "dashboard.wsgi:application", "--bind", "0.0.0.0:8000"]
