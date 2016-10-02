#!/bin/bash

# designate folder for operation (hard coded)
cd /Volumes/DATA_DRIVE/NatRiskChange/Data
destiny=/Volumes/DATA_DRIVE/NatRiskChange/Data

# designate subfolder to process
read basename
dir=$destiny/$basename

# switch to subdirectory
cd $dir/$basename.TIFF
echo $(ls)

# extract scene ID of MTL file (cut at '_' )
scene_id=$(ls -1 *_MTL.txt | cut -f 1 -d '_')
echo $scene_id

# move subfolder to new destination
mv $dir/$basename.TIFF/ $destiny/$scene_id/

# remove empty original directory
rm -rf $dir
