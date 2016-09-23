#!/bin/bash

# Build image first
# Documentation https://docs.docker.com/engine/reference/commandline/build/
docker build -t natriskchange/ledaps .

# Locate auxiliary data
# Source directory
# Results directory
# Source directory (argument $1 for shell script)
# Auxiliary data (argument $2 for shell script

# docker run -ti --rm --name=ledaps_image \
# -v /Volumes/DATA_DRIVE/NatRiskChange/Auxiliary/ledaps_aux.1978-2014:/opt/ledaps \
# -v /Volumes/DATA_DRIVE/NatRiskChange/Data/LT41760361990224XXX03:/data \
# -v /Volumes/DATA_DRIVE/NatRiskChange/Results:/results \
# natriskchange/ledaps /bin/bash

docker run -ti --rm --name=ledaps_image \
-v /Volumes/DATA_DRIVE/NatRiskChange/Auxiliary/ledaps_aux.1978-2014:/opt/ledaps \
-v /Volumes/DATA_DRIVE/NatRiskChange/Data/LT51760361987032ESA00:/data \
-v /Volumes/DATA_DRIVE/NatRiskChange/Results:/results \
natriskchange/ledaps /data/LT51760361987032ESA00/ /opt/ledaps/
