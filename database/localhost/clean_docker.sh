#!/bin/bash

# get container ids

containers=$(docker ps -a -q)

if [ -z "$containers" ]; then
    echo "No containers to clean!"
else
    echo "Cleaning containers..."
    # stop all containers
    echo "Stopping containers..."
    docker stop $containers
    # remove all containers
    echo "Removing containers..."
    docker rm $containers
fi