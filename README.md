# THE PJPROJECT

## Introduction
The PJPROJECT is a free and open source multimedia communication library written in C language implementing standard based protocols such as SIP, SDP, RTP, STUN, TURN, and ICE. It combines signaling protocol (SIP) with rich multimedia framework and NAT traversal functionality into high level API that is portable and suitable for almost any type of systems ranging from desktops, embedded systems, to mobile handsets.

## Contents
* Rust bindings for pjsua
* Pip-installable pjsua2 python module
* Installing pjsip on Debian
* Pjsua usage examples in ```c``` and ```rust```
* Pjsua2 usage examples in ```c++``` and ```python3```
* A ready to use docker image with pjsua and pjsua2 installed
* A ready to use docker image with a dev ```kamailio``` sip server

## Dependencies
* For the Installation of pjsip on Debian, you need to install ```gcc```, ```g++``` and ```make```
```sh
sudo apt install -y gcc g++ make
``` 
* For generating the rust bindings for pjsau, you need to install ```rust``` and ```clang```
```sh
sudo apt install -y curl clang
sudo curl https://sh.rustup.rs -sSf | sh -s -- -y
```
* For building the pjsua2 python module, you need to install ```python3```, ```python3-dev``` and ```swig```
```sh
sudo apt install -y swig python3 python3-dev
```
## Installing pjsip on Debian
* Navigate to pjproject directory
```sh
cd pjproject
```
* Configure the build
```sh
./configure --enable-shared
```
* Build the project
```sh
make dep
make
```
* Install the project
```sh
sudo make install
```
## Installing pjsua2 python module

* Navigate to pjsua2 swig python directory
```sh
cd pjproject/pjsip-apps/src/swig/python
```
* Build the module
```sh
make
```
* Install the module
```sh
sudo make install
```

## Installing pjsua2 python module using pip
```sh
sudo pip3 install git+https://github.com/JadKHaddad/THE-PJPROJECT.git --verbose
```

## Running the examples

* C
```sh
cd c
make
./out
make clean
```
* C++
```sh
cd cpp
make
./out
make clean
```
* Rust
```sh
cd rust
cargo run
cargo clean
``` 
* Python3
```sh
cd python3
python3 main.py
```

## Libraries not found?
* Set the environment variable ```LD_LIBRARY_PATH``` to the directory where the libraries are located
```sh
export LD_LIBRARY_PATH=/usr/local/lib
```
## Don't know where the libraries are located?
* Run the following command to collect your libraries and headers
```sh
chmod u+x ./copy-lib-include.sh
./copy-lib-include.sh
```
* Now you can set the environment variable ```LD_LIBRARY_PATH``` to the directory where the libraries are located

## Don't have a sip server or Debian?

* Create a docker network
```sh
docker network create net
```
* Build and run the kamailio docker image
```sh
docker build -t kamailio5.5.0-trusty -f dockerfiles/Dockerfile.kamailio .

docker run -it --rm --name kamailio5.5.0-trusty --network net -p 5060:5060/udp kamailio5.5.0-trusty
```
* Build and run the debian docker image
```sh
docker build -t pjsip -f dockerfiles/Dockerfile.debian .

docker run -it --rm --name pjsip --network net --add-host=host.docker.internal:host-gateway pjsip
```
* Inside the pjsip container, run the examples using ```kamailio5.5.0-trusty:5060``` as a sip domain

## References

* [pjsip](https://www.pjsip.org/)
* [pjproject on github](https://github.com/pjsip/pjproject)
* [pjsua2 API Reference](https://www.pjsip.org/pjsip/docs/html/group__PJSUA2__Ref.htm)
* [pjsua2 Documantation](https://www.pjsip.org/docs/book-latest/html/)

## Notes
* pjproject cloned from the official repository on 2022-09-22
