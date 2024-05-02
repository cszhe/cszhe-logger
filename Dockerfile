from ubuntu:noble

# disable python buffer
ENV PYTHONUNBUFFERED=1

# ajust time to Auckland
ENV TZ=Pacific/Auckland
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# install necessary packages
RUN apt update && apt-get upgrade -y
RUN apt install -y python3-pip && pip3 install --upgrade pip

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
RUN pip install /code

# put other files in docker-compose
