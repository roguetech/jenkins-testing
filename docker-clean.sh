#!/bin/bash
set -ux
echo "Y" | docker volume prune || true
echo "Y" | docker container prune ||  true
docker rmi -f $1:$2 || true
docker container inspect $1
if [ 0 == $? ]; then
  docker rm -f -v $1 || true
fi
#docker system prune -f
#docker rmi $(docker images --filter "dangling=true" -q --no-trunc)
