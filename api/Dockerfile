FROM pypy:3-6

# Create work dir
RUN mkdir /home/api
WORKDIR /home/api

# Create uwsgi tmp dir
RUN mkdir /tmp/gunicorn-sockets

# Install pipenv
RUN pip3 install pipenv==2018.10.13

# Set encoding for pipenv
ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8

# Copy pipfile into project
COPY ./core/Pipfile* /home/api/

# Setup path to pypy3
RUN pipenv --python $(which pypy3)

# Install deps to system
RUN pipenv install --system --dev

ENTRYPOINT ["gunicorn", "-c", "config.py", "--reload", "api.api:APPLICATION"]
