FROM python:3.14.0a4-alpine3.21

# Prevents django from writing unnecessary files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Set an environment variable to unbuffer Python output, aiding in logging and debugging
ENV PYTHONBUFFERED=1

# Define an environment variable for the web service's port, commonly used in cloud services
ENV APP_PORT 8000

# Define an environment variable for the project name
ENV cdc_project = PROJECT_NAME

# Set the working directory within the container to /app for any subsequent commands
WORKDIR /project

# Copy the requirements.txt into the container
COPY requirements.txt .

# Check for python3 and pip installation and output version
RUN python3 --version
RUN pip --version

# Upgrade pip to ensure we have the latest version for installing dependencies
RUN pip install --upgrade pip

# Update apk and install psycopg2 dependencies
RUN apk update
RUN apk add postgresql-dev

# Install dependencies from the requirements.txt file to ensure our Python environment is ready
RUN pip install -r requirements.txt

# Copy the entire current directory contents into the container at /app
COPY . .

# # Set the command to run our web service using Gunicorn, binding it to 0.0.0.0 and the PORT environment variable
CMD gunicorn ${PROJECT_NAME}.wsgi:application --bind 0.0.0.0:"${APP_PORT}"

# Inform Docker that the container listens on the specified network port at runtime
EXPOSE ${APP_PORT}

# docker build -t django-docker:latest .