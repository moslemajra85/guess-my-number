# start from an image that aready has python
FROM python:3.11-slim


# Create a working directory isnide the container
WORKDIR  /app

# Copy the current directory contents into the container at /app
COPY game.py .


# Commands To Run Where the container starts
CMD ["python", "game.py"]