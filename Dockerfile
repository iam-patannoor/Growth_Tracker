# Stage 1: Build and dependency compilation
FROM python:3.9-slim AS builder

LABEL maintainer="noor"
LABEL description="Build stage for the Mind Detox tracking application"

WORKDIR /app

# Install compilation dependencies if needed
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy only requirements to leverage Docker caching layers
COPY requirements.txt .

# Install dependencies into a local user directory
RUN pip install --no-cache-dir --user -r requirements.txt


# Stage 2: Final lightweight runtime image
FROM python:3.9-slim AS final

LABEL maintainer="noor"
LABEL description="Production image for the Mind Detox web app"

WORKDIR /app

# Copy the installed dependencies from the builder stage
COPY --from=builder /root/.local /root/.local
COPY . .

# Ensure the local pip binaries are accessible in the system path
ENV PATH=/root/.local/bin:$PATH

# Streamlit default networking port
EXPOSE 8501

# Run the Streamlit application
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
