#!/bin/bash

sudo chmod -R 0777 ./mongodb
docker-compose up -d --remove-orphans
CID=$(docker ps -qf "name=mongodb")
echo "CID=$CID"
