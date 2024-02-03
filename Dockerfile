# Use an official Python runtime as a parent image
FROM python:3.9

# Set environment variables for Django
ENV DJANGO_SETTINGS_MODULE=MoneyManaer.settings
ENV PYTHONUNBUFFERED=1

# Create and set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt
#
# Copy the current directory contents into the container at /app
COPY . /app/

# Expose port 8000 for the Django application to listen on
EXPOSE 8000

# Run Django's development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]