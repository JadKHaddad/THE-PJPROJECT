# PJSUA2-Python3 Extended Example With Kamailio

## This example shows how to use PJSUA2-Python3 with Kamailio.
<br>
PLEASE RUN THE COMMANDS IN THE ROOT DIRECTORY
<br>
<br>

Create a network
```sh
docker network create net
```

Build and run kamailio
```sh
docker build -t kamailio5.5.0-trusty -f dockerfiles/kamailio/Dockerfile.kamailio .
docker run -it --rm --name kamailio5.5.0-trusty --network net -p 5060:5060/udp kamailio5.5.0-trusty
```

Build pjsua2
```sh
docker build -t pjsua2-latest-version-debian -f dockerfiles/Dockerfile.debian-slim . 
```

Run 2 pjsua2 containers
```sh
docker run -it --rm -v ${pwd}\dockerfiles\kamailio:/home/ --network net --add-host=host.docker.internal:host-gateway pjsua2-latest-version-debian
```

Run the answerer.py script in the first container
```sh
python3 answerer.py
```
Run the caller.py script in the second container
```sh
python3 caller.py
```

