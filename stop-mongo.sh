#!/bin/bash

CID=$(docker ps -qf "name=mongodb")
echo "CID=$CID"
if [[ ! $CID. == . ]]
then
    echo "Stopping $CID"
    docker stop $CID
fi
