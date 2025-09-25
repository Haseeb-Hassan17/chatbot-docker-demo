# Use official Python image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy dependencies first
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Run the chatbot
CMD ["python", "chatbot.py"]
