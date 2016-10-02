#!/bin/bash

# designate folder for operation (hard coded)
cd /Volumes/DATA_DRIVE/NatRiskChange/Data
dir_source=/Volumes/DATA_DRIVE/NatRiskChange/Data
destiny=/Volumes/DATA_DRIVE/NatRiskChange/Data_Prepared


for path in *; do
	
	# unzip 
    [ -d "${path}" ] || continue # if not a directory, skip
    dirname="$(basename "${path}")"
    echo $dirname

	# designate subfolder to process
	dir=$dir_source/$dirname
	
	# switch to subdirectory
	cd $dir/$dirname.TIFF
	echo $(ls)
	
	# extract scene ID of MTL file (cut at '_' )
	scene_id=$(ls -1 *_MTL.txt | cut -f 1 -d '_')
	echo $scene_id
	
	# move subfolder to new destination
	mv $dir/$dirname.TIFF/ $destiny/$scene_id/
	
	# remove empty original directory
	rm -rf $dir
	rm -rf $dir.ZIP
done