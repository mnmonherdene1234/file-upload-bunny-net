FROM python:latest

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt    

# Expose port 8000 for the Flask app to listen on
EXPOSE 8000

CMD [ "gunicorn", "-w", "4", "-b", "0.0.0.0", "app:app" ]