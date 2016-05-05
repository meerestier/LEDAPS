# LEDAPS
docker commands to preprocess landsat data, tm and etm+ that are based in ancilliary data from 1980 to 2013

The dockerfile used in this branch use an old release: http://ledaps.googlecode.com/svn/releases/version_1.3.0 and an old ancilliary data,
for a new approach go to folder ledaps_cc

##Commands
```
$docker build -t ledaps/ledaps:v1 .

$docker run --rm -v <path to directory with ancilliary data>:/opt/ledaps -v <path to local directory with data>:/data -v <path to directory for results>:/results ledaps/ledaps:v1 <path to ancilliary data in docker> <path to source data in docker/L*.*.tar.bz> <path to destiny results in docker>

#Example:

$docker run --rm -v /Users/ledaps_anc:/opt/ledaps -v /Users/data:/data -v /Users/results:/results name_image /opt/ledaps /data/LE70210481999203AGS00.tar.bz /results
```
The directory *path to directory for results* will have the results


