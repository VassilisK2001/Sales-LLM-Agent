FROM python:3.9-slim 

# Set the working directory
WORKDIR /app

COPY requirements.txt requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Ensure environment variables are loaded
ENV PYTHONUNBUFFERED=1   

# Expose the port the app runs on
EXPOSE 5000    

# Command to run the application
CMD ["python", "main.py"]
