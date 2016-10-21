#!/bin/bash

# Build image first
# Documentation https://docs.docker.com/engine/reference/commandline/build/
docker build -t natriskchange/ledaps .

# Locate auxiliary data
# Source directory
# Results directory
# Source directory (argument $1 for shell script)
# Auxiliary data (argument $2 for shell script)

# Name the Scene in the data folder
echo "Please paste the Landsat Scene ID to process. (example: LT41760361990224XXX03)"
read sceneID

## declare an array variable
declare -a arr=($sceneID)

## now loop through the above array
for i in "${arr[@]}"
do
  # or do whatever with individual element of the array
  echo  "Processing $i"
  docker run -ti --rm \
  -v /Volumes/DATA_DRIVE/NatRiskChange/Auxiliary/ledaps_aux.1978-2014:/opt/ledaps \
  -v /Volumes/DATA_DRIVE/NatRiskChange/Data:/data \
  -v /Volumes/DATA_DRIVE/NatRiskChange/Results:/results \
  natriskchange/ledaps /data/$i /opt/ledaps
done
