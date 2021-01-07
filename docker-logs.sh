#!/bin/bash

CID=$(docker ps -qf "name=mongodb")
echo "CID=$CID"
if [[ ! $CID. == . ]]
then
    echo "Showling logs $CID"
    docker logs --tail 2500 $CID
fi
