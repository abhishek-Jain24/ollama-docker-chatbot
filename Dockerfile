# Small official Python image. Streamlit 1.66 needs Python 3.11 or newer.
FROM python:3.12-slim

WORKDIR /app

# Install dependencies before copying the app so this layer stays cached
# when only app.py changes.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# .dockerignore keeps .env out of this copy, so the API key is not baked in.
COPY . .

EXPOSE 8501

# 0.0.0.0 lets a browser on your computer reach Streamlit inside the container.
# headless=true skips Streamlit's first-run prompt so the container can start.
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0", "--server.headless=true"]
