# LEDAPS
docker commands to preprocess landsat data, tm and etm+ that are based in ancilliary data: http://espa.cr.usgs.gov/downloads/auxiliaries/ledaps_auxiliary/ledaps_aux.1978-2014.tar.gz 

according to https://github.com/USGS-EROS/espa-surface-reflectance.git and images after year 2012 with metadata "resampling option: CC" 

Use the shell_script on this repository where you execute the following command

##Commands
```
$docker build -t ledaps/ledaps:v1 .

$docker run --rm -v <path to directory with ancilliary data>:/opt/ledaps -v <path to local directory with data>:/data -v <path to directory for results>:/results ledaps/ledaps:v1 /results/shell_script <path to ancilliary data in docker> <path to source data in docker/L*> <path to destiny results in docker>

#Example:

$docker run --rm -v /Users/auxilliary_data:/opt/ledaps -v /Users/data:/data -v $(pwd):/results name_image /opt/ledaps /data/LE70210482012015ASN00 /results
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


