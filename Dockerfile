FROM raychorn/ubuntu_python38:all-pythons-dev

RUN apt-get update -y && apt-get upgrade -y && apt-get install -y iputils-ping && apt install software-properties-common -y --fix-missing
RUN apt-get install net-tools -y
RUN apt-get install python3.8-dev -y
RUN apt-get update -y && apt-get install nginx -y
COPY ./workspaces/installer.sh /workspaces/install/installer.sh
RUN chmod +x /workspaces/install/installer.sh
ENTRYPOINT ["bash", "-c", "/workspaces/install/installer.sh"]