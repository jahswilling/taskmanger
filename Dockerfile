# Use a base Python image
FROM python:3.11

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy your Django application code into the container
COPY . /app/

RUN pip install channels

# Install Daphne and any other necessary dependencies
RUN pip install daphne

# Expose port 8000 (Daphne's default port)
EXPOSE 8000

# Start Daphne to serve the Django Channels application
CMD ["daphne", "taskmanager.asgi:application"]
