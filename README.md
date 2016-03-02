# LEDAPS
docker commands to preprocess landsat data
##Commands
docker build -t ledaps/ledaps:v1 .

docker run --rm -v <path to directory with ancilliary data>:/opt/ledaps -v <path to local directory with data>:/data -v <path to directory for results>:/results ledaps/ledaps:v1 <path to ancilliary data in docker> <path to source data in docker/L*.*.tar.bz> <path to destiny results in docker>
