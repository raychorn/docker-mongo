#!/bin/bash

do_installation(){
    groupadd django
    useradd django -s /bin/bash -p 'Peek@bb1423'
    usermod -a -G django django
    mkdir -p /workspaces/microservices-framework
    chown -R django:django /workspaces
    cd /workspaces
    git clone https://github.com/raychorn/microservices-framework.git
}

do_installation >./workspaces/installation_report.txt 2>&1
