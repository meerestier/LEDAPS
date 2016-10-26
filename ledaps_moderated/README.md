docker commands to preprocess landsat data, tm and etm+ that are based in
ancilliary data (link changed recently):
http://edclpdsftp.cr.usgs.gov/downloads/auxiliaries/ledaps_auxiliary/ledaps_aux.1978-2014.tar.gz

LEDAPS
======

according to https://github.com/USGS-EROS/espa-surface-reflectance.git and
images after year 2012 with metadata "resampling option: CC"

Use the shell\_script on this repository where you execute the *docker run
command*

Commands
--------

Step 1: Build the container to run the process in. This is a custom docker
container, that is

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
$docker build -t natriskchange/ledaps .

#Execute the following command in the directory where you have the shell_script

docker run -ti --rm \
-v /Volumes/DATA_DRIVE/NatRiskChange/Auxiliary/ledaps_aux.1978-2014:/opt/ledaps \
-v /Volumes/DATA_DRIVE/NatRiskChange/Data:/data \
-v /Volumes/DATA_DRIVE/NatRiskChange/Results:/results \
natriskchange/ledaps /data /opt/ledaps


$docker run --rm -v <path to directory with ancillary data>:/opt/ledaps \
-v <path to local directory with landsat data>:/data \
-v <path to directory for results>:/results \
ledaps/ledaps:v1 /results/shell_script /data/folder_landsat_data /opt/ledaps

#Example:

$docker run --rm -v /Users/auxilliary_data:/opt/ledaps -v /Users/data:/data \
-v $(pwd):/results name_image /results/shell_script /data/LE70210492015007EDC00 /opt/ledaps
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The directory where you execute the command will have the results

To update the auxilliary data, we can use the updatetoms.py and updatencep.py

An example using updatetoms.py:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
$docker run --rm -v <path to directory to update ancilliary data>:/data -it name_docker_image /bin/bash

#export PATH=$BIN:$PATH

#/$BIN/updatetoms.py -s 1990 -e 1991

#cp -r /root/EP_TOMS /data

#exit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

*path to directory to update ancilliary data* will have the results
