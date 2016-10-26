#!/bin/bash

# Name: Reformat ESA Folders
# Creator: Lars Schulz
# URL: http://eco.systemic.de
# Version: 0.0.1

# designate folder for operation (hard coded)
cd /Volumes/DATA_DRIVE/NatRiskChange/Data

# set variables
dir_zip=/Volumes/DATA_DRIVE/NatRiskChange/Downloads/Downloads_esa_TM
dir_source=/Volumes/DATA_DRIVE/NatRiskChange/Data
destiny=/Volumes/DATA_DRIVE/NatRiskChange/Data_Prepared


for path in *.ZIP; do

	# get name without .ZIP
    dirname="$(basename "${path}" | cut -f 1 -d '.')"

	# designate subfolder to process and create it
	dir=$dir_source/$dirname
    mkdir $dir

    # unzip into subfolder
    unzip $path -d $dir_source/$dirname

	# switch to subdirectory
	cd $dir/$dirname.TIFF
	echo $(ls)

	# extract scene ID of MTL file (cut at '_' )
	scene_id=$(ls -1 *_MTL.txt | cut -f 1 -d '_')
	echo $scene_id

	# move subfolder to new destination
	mv $dir/$dirname.TIFF/ $destiny/$scene_id/

	# go back to base folder
	cd $dir_source

	# remove empty original directory
	rm -rf $dir_source/$dirname
	#rm -rf $path

done
