#!/bin/bash

echo "bringing up docker containers"
docker-compose -f dependencies-compose.yml  up -d --build