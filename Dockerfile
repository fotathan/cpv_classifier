FROM python:3.11-slim

# Avoid Python writing pyc files and buffering stdout/stderr
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    # Streamlit settings
    STREAMLIT_SERVER_PORT=8501 \
    STREAMLIT_SERVER_ADDRESS=0.0.0.0 \
    STREAMLIT_SERVER_HEADLESS=true \
    STREAMLIT_BROWSER_GATHER_USAGE_STATS=false \
    # HF Spaces forbids writing to /home/user/.cache (the default for HF Hub
    # and sentence-transformers). Redirect both to /tmp which is writable.
    HF_HOME=/tmp/huggingface \
    TRANSFORMERS_CACHE=/tmp/huggingface \
    SENTENCE_TRANSFORMERS_HOME=/tmp/huggingface

WORKDIR /app

# System deps (kept minimal). git is needed by some HF download paths.
RUN apt-get update && apt-get install -y --no-install-recommends \
        git \
        && rm -rf /var/lib/apt/lists/*

# Install Python deps first for better layer caching
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy the app
COPY . .

# HF Spaces routes port 8501 for Streamlit apps. Don't change.
EXPOSE 8501

CMD ["streamlit", "run", "app.py"]
