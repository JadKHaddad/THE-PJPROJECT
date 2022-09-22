FROM debian:11-slim as builder

RUN apt update
RUN apt install -y git gcc make g++ python3 python3-dev swig

WORKDIR /home
RUN git clone https://github.com/pjsip/pjproject.git --depth 1 pjproject

WORKDIR /home/pjproject

# set max calls to 1000
#COPY dockerfiles/config_site_sample.h /home/pjproject/pjlib/include/pj/config_site_sample.h

RUN ./configure --enable-shared
RUN make dep
RUN make
RUN make install

ENV LD_LIBRARY_PATH /usr/local/lib

# install rust
RUN apt install -y curl
RUN curl https://sh.rustup.rs -sSf | sh -s -- -y
RUN apt install -y clang

RUN export PATH=$PATH:/root/.cargo/bin

WORKDIR /home/

# docker build -t pjsua2-rust-debian  . 
# docker run -it --rm -v ${pwd}:/home/rust/ pjsua2-rust-debian