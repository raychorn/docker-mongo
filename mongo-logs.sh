#!/bin/bash

MONGO_LOGS=./mongodb/data/log/mongod.log
if [[ -f $MONGO_LOGS ]]
then
    tail -f $MONGO_LOGS
fi
