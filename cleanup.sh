#/bin/sh

# kill any running containers
docker kill $(docker ps -a | awk '{print $1}')

# cleanup docker stuff
yes | docker system prune --all
yes | docker image prune --all

# delete db directory
sudo rm -fr ${PWD}/db-data 

# make db directory
mkdir ${PWD}/db-data/
sudo chown ec2-user:ec2-user db-data/
