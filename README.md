# LEDAPS
docker commands to preprocess landsat data, tm and etm+ 

For images with metadata with "resampling option: CC" go to directory ledaps_cc and use the ancilliary data: 
http://espa.cr.usgs.gov/downloads/auxiliaries/ledaps_auxiliary/ledaps_aux.1978-2014.tar.gz

##Commands
```
$docker build -t ledaps/ledaps:v1 .

$docker run --rm -v <path to directory with ancilliary data>:/opt/ledaps -v <path to local directory with data>:/data -v <path to directory for results>:/results ledaps/ledaps:v1 <path to ancilliary data in docker> <path to source data in docker/L*.*.tar.bz> <path to destiny results in docker>

#Example:

$docker run -v /Users/ledaps_anc:/opt/ledaps -v /Users/data:/data -v /Users/results:/results name_image /opt/ledaps /data/LE70210481999203AGS00.tar.bz /results
```
