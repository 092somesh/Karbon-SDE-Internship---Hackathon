# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app


# Copy the requirements file and install Python dependencies
COPY requirements.txt /app/
RUN pip install -r requirements.txt \
    && pip install gunicorn

# Copy the project files into the container
COPY . /app/

# Expose the port that Gunicorn will run on
EXPOSE 8000

# Command to run the application using Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "fin_project.wsgi:application"]
