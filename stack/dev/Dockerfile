FROM ubuntu:20.04

# install dev tools
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \
    build-essential \
    wget \
    curl \
    nano \
    sudo \
    python3 \
    python3-pip

# tell python not to write bytecode and simlink python3 to python
ENV PYTHONDONTWRITEBYTECODE 1
RUN ln -s /usr/bin/python3 /usr/bin/python
RUN ln -s /usr/bin/pip3 /usr/bin/pip

# install nox for testing etc
RUN pip install nox

# setup default terminal
RUN echo TERM='"'xterm-color'"' >> /etc/environment

# copy enter script and run
COPY stack/dev/enter.sh /enter.sh
WORKDIR /rxtouchtoggle
CMD tail -f /dev/null
