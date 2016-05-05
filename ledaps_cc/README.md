# LEDAPS
docker commands to preprocess landsat data, tm and etm+ that are based in ancilliary data: http://espa.cr.usgs.gov/downloads/auxiliaries/ledaps_auxiliary/ledaps_aux.1978-2014.tar.gz 

LEDAPS based in https://github.com/USGS-EROS/espa-surface-reflectance.git and images after year 2012 with metadata "resampling option: CC" 

##Commands
```
$docker build -t ledaps/ledaps:v1 .

$docker run --rm -v <path to directory with ancilliary data>:/opt/ledaps -v <path to local directory with data>:/data -v <path to directory for results>:/results ledaps/ledaps:v1 <path to ancilliary data in docker> <path to source data in docker/L*.*.tar.bz> <path to destiny results in docker>

#Example:

$docker run -v /Users/ledaps_anc:/opt/ledaps -v /Users/data:/data -v /Users/results:/results name_image /opt/ledaps /data/LE70210481999203AGS00.tar.bz /results
```

The directory *path to directory for results* will have the results

To update the auxilliary data, we can use the updatetoms.py and updatencep.py

An example using updatetoms.py:

```
$docker run --rm -v <path to directory to update ancilliary data>:/data --entrypoint=/bin/bash -it name_docker_image

#export PATH=$BIN:$PATH

#/$BIN/updatetoms.py -s 1990 -e 1991

#cp -r /root/EP_TOMS /data

#exit

```
*path to directory to update ancilliary data* will have the results

