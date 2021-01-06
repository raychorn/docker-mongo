#!/bin/bash

VENV=.venv
REQS=./requirements.txt

if [[ ! -d $VENV ]]
then
    virtualenv --python /usr/bin/python3.9 -v $VENV
fi

if [[ -d $VENV ]]
then
    . ./$VENV/bin/activate
    pip install --upgrade pip

    if [[ -f $REQS ]]
    then
        pip install -r $REQS
    fi

fi
