#!/bin/bash

chmod -R 0777 ./mongodb
docker-compose up -d --remove-orphans
CID=$(docker ps -qf "name=mongodb")
echo "CID=$CID"
if [[ ! $CID. == . ]]
then
    echo "Update $CID"
    docker update --restart unless-stopped --cpus="2.5" --memory="2g" --memory-swap="2.5g" $CID
fi
