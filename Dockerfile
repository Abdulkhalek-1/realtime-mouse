# Use the official Python image as the base image
FROM python:3.13.0-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Copy the requirements file first to leverage Docker caching
COPY requirements.txt /app/

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the container
COPY . /app/

# Expose the port the app runs on
EXPOSE 8000

# Start the Django application (use manage.py runserver or your WSGI server)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
