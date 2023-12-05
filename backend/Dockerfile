# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . /usr/src/app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt



# Expose port 8000 to the outside world
EXPOSE 8000

# Run uvicorn when the container launches
CMD ["uvicorn", "src.main:app","--host", "0.0.0.0", "--port", "8000", "--reload"]
