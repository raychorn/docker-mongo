#!/bin/bash

docker-compose down
CID=$(docker ps -qf "name=mongodb")
echo "CID=$CID"
