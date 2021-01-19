#!/bin/bash

# deploy this into /workspaces in the container

do_it(){
    REQS=requirements.txt

    dir1="/workspaces/microservices-framework/"
    dir2="$dir1/microservices-framework/"
    VENV=$dir1/.venv

    cd $dir1
    git pull origin main

    python=/usr/bin/python3.8
    vers=$($python -c 'import sys; i=sys.version_info; print("{}{}{}".format(i.major,i.minor,i.micro))')

    if [[ ! -d $VENV$vers ]]
    then
        virtualenv --python $python -v $VENV$vers
    fi

    . $VENV$vers/bin/activate
    pip install -r $dir2/$REQS

    gunicorn -c $dir2/config.py microservices_framework.wsgi:application
}

do_it >/workspaces/runserver_report.txt 2>&1
