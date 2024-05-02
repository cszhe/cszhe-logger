from ubuntu:noble

# disable python buffer
ENV PYTHONUNBUFFERED=1

# ajust time to Auckland
ENV TZ=Pacific/Auckland
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# install necessary packages
RUN apt update && apt-get upgrade -y
RUN apt install -y python3-pip python3-venv

# ajust time to Auckland
RUN apt install -y tzdata && \
    echo "Pacific/Auckland" > /etc/timezone && \
    dpkg-reconfigure -f noninteractive tzdata

# additional packages
RUN apt install -y curl

# copy code
# install the code
RUN  mkdir /code
WORKDIR /code
COPY . /code
RUN rm -rf /code/.git/
# RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
# ubuntu noble, must install in venv
RUN python3 -m venv /venv
RUN /venv/bin/pip install /code

# put other files in docker-compose
