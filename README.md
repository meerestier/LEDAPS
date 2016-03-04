# LEDAPS
docker commands to preprocess landsat data. For years after 2013 go to directory ledaps_after_2013
##Commands
```
$docker build -t ledaps/ledaps:v1 .

$docker run --rm -v <path to directory with ancilliary data>:/opt/ledaps -v <path to local directory with data>:/data -v <path to directory for results>:/results ledaps/ledaps:v1 <path to ancilliary data in docker> <path to source data in docker/L*.*.tar.bz> <path to destiny results in docker>
```
The ancilliary data: http://espa.cr.usgs.gov/downloads/auxiliaries/ledaps_auxiliary/ledaps_aux.1978-2014.tar.gz
