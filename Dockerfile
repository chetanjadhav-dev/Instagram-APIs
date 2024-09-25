# Step 1: Use Python 3.11 as the base image
FROM python:3.11-slim

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy the requirements.txt file into the container
COPY requirements.txt /app/

# Step 4: Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy the entire Django project into the container
COPY . /app/

# Step 6: Expose port 8000 (Django runs on this port by default)
EXPOSE 8000

# Step 7: Ensure environment variables from .env are loaded
RUN pip install python-dotenv

# Step 8: Start Django's development server (running on all network interfaces)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
