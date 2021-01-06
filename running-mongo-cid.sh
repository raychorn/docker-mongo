#!/bin/bash

CID=$(docker ps -qf "name=mongodb")
echo "CID=$CID"
