FROM python:3.10-slim-buster

# Set Python environment variable
# FROM python:${PYTHON_VERSION}
RUN apt-get update
RUN apt-get -y install vim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code

COPY . /code/
# COPY requirements.txt /code/
RUN pip install -r requirements.txt


# COPY .env /code/

# Expose port 8000
EXPOSE 8000

# Use gunicorn on port 8000
CMD ["gunicorn", "--bind", ":8000", "--workers", "2", "django_project.wsgi"]