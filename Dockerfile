# Use a base Python image
FROM python:3.11

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy your Django application code into the container
COPY . /app/

# Expose port 8000
EXPOSE 8000

# Start the Django application with "python3 manage.py runserver"
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
