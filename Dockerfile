from ubuntu:jammy

# ajust time to Auckland
ENV TZ=Pacific/Auckland
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# disable python buffer
ENV PYTHONUNBUFFERED=1

# install necessary packages
RUN apt update && apt-get upgrade -y
RUN apt install -y python3-pip && pip3 install --upgrade pip

# copy code
# install the code
RUN  mkdir /code
WORKDIR /code
COPY . /code
RUN rm -rf /code/.git/
# RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
RUN pip install /code

# put other files in docker-compose
