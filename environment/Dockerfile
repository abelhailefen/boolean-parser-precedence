FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install pytest for running tests
RUN pip install --no-cache-dir pytest

# Copy only the buggy file into the image context
COPY parser.py /app/parser.py

# Ensure directories for verifiers and outputs are present
RUN mkdir -p /logs/agent /logs/verifier /tests /solution