# LEDAPS
docker commands to preprocess landsat data, tm and etm+ that are based in ancillary data from 1980 to 2013

The dockerfile used in this branch use an old release: http://ledaps.googlecode.com/svn/releases/version_1.3.0 and an old ancillary data,
for a new approach go to folder ledaps_cc

##Commands
```
$ docker build -t natriskchange/ledaps .


$ docker run -ti --rm \
  -v /Volumes/DATA_DRIVE/NatRiskChange/Auxiliary/ledaps_aux.1978-2014:/opt/ledaps \
  -v /Volumes/DATA_DRIVE/NatRiskChange/Data:/data \
  -v /Volumes/DATA_DRIVE/NatRiskChange/Results:/results \
  natriskchange/ledaps /data /opt/ledaps





$ docker run --rm -v <path to directory with ancillary data>:/opt/ledaps -v <path to local directory with data>:/data -v <path to directory for results>:/results ledaps/ledaps:v1 /results/shell_script /data/<L*.*.tar.bz> /opt/ledaps

# Example:

$ docker run --rm -v /Users/ledaps/ancillary_data/:/opt/ledaps -v /Users/data/:/data -v $(pwd):/results ledaps/ledaps:v1 /results/shell_script /data/LE70210481999203AGS00/ /opt/ledaps
```
The directory *path to directory for results* will have the results
