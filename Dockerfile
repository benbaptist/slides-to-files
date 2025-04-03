FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first to leverage Docker cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY export_slides.py .

# Create directory for exported slides
RUN mkdir -p exported_slides

# Run as non-root user
RUN useradd -m appuser && \
    chown -R appuser:appuser /app
USER appuser

CMD ["python", "export_slides.py"] 