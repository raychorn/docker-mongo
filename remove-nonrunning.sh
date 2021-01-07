#!/bin/bash

docker ps -a | cut -c-12 | xargs docker rm
