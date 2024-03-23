# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory in the container to /app
WORKDIR /

# Add the current directory contents into the container at /app
ADD . /

# Install pipenv
RUN pip install pipenv

# Install any needed packages specified in Pipfile
RUN pipenv install --system --deploy

# Make port 8501 available to the world outside this container
EXPOSE 8501

# Run the command to start the Streamlit app
CMD streamlit run prediction.py