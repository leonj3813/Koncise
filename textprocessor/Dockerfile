FROM python:3

# Copy your application code to the container (make sure you create a .dockerignore file of any large files or directories should be excluded)
RUN mkdir /code/
WORKDIR /code/
COPY . /code/

# Install python requirements
RUN pip install -r requirements.txt

# Add any custom, static environment variables needed by Django or your settings file here:
ENV DJANGO_SETTINGS_MODULE=textprocessor.settings

# Collect static files
RUN python manage.py collectstatic --noinput

# Download nltk punkt library
RUN python -c "import nltk; nltk.download('punkt')"

# Start uWSGI
CMD ["uwsgi", "--ini", "textsum_uwsgi.ini"]
