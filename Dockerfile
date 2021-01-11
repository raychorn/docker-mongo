FROM raychorn/ubuntu_python38:all-pythons-dev

RUN apt-get update -y && apt-get upgrade -y && apt-get install -y iputils-ping
RUN apt-get install net-tools -y
