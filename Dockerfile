# Use a base image with Python pre-installed
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install dependencies using pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire application content into the container
COPY . .

# Set environment variables for the application
ENV MODEL_URL='MODEL_ML_URL'
ENV TF_ENABLE_ONEDNN_OPTS=0

# Expose port 5000 (the default Flask port)
EXPOSE 5000

# Specify the command to run the application when the container starts
CMD ["python", "app.py"]
