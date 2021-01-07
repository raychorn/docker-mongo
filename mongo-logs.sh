#!/bin/bash

MONGO_LOGS=./mongodb/data/log/mongod.log
if [[ -f $MONGO_LOGS ]]
then
    tail -n 100 $MONGO_LOGS
fi
