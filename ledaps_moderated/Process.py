#!/usr/bin/python

# Python Script to moderate LEDAPS Docker Workflow
# Name: Launch LEDAPS
# Description: Describes what your action will do.
# Handles: Files, Folders
# Creator: Lars Schulz
# URL: http://eco.systemic.de
# Version: 0.0.1

import time
import subprocess
import os, sys
# import zipfile

#----------------------------------------------------------------------------------------------
# globals
#----------------------------------------------------------------------------------------------

dir = "~/Desktop"
# Directory with Subdirectories of Scenes
dir_input = "/Volumes/DATA_DRIVE/NatRiskChange/Data"
dir_output = "/Volumes/DATA_DRIVE/NatRiskChange/Results"
dir_auxiliary = "/Volumes/DATA_DRIVE/NatRiskChange/Auxiliary/ledaps_aux.1978-2014"

#----------------------------------------------------------------------------------------------
# helper functions
#----------------------------------------------------------------------------------------------

def my_dir():
	'''Get the path'''
	global dir
	# https://docs.python.org/2/library/os.path.html
	dir = os.path.dirname( os.path.abspath(__file__) )
	os.chdir(dir)
	return dir

def dir_chooser():
	'''Asks for directories needed for the conversion.'''
	global dir_input, dir_output, dir_auxiliary
	dir_input = raw_input('Enter path to source folder (scenes in subfolders): ')
	dir_output = raw_input('Enter path to results folder: ')
	dir_auxiliary = raw_input('Enter path to auxiliary folder: ')
	return dir_input, dir_output, dir_auxiliary

def get_immediate_subdirectories(dir):
    return [name for name in os.listdir(dir)
            if os.path.isdir(os.path.join(dir, name))]

def rename_dir():
	for scene in scenes:
		print "Scene ID: %s" % scene
		print "TODO: Subprocess"
		command = "/bin/bash shell_rename.sh"
		process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
		print process.returncode



def unzip(source_filename, dest_dir):
    with zipfile.ZipFile(source_filename) as zf:
        for member in zf.infolist():
            # Path traversal defense copied from
            # http://hg.python.org/cpython/file/tip/Lib/http/server.py#l789
            words = member.filename.split('/')
            path = dest_dir
            for word in words[:-1]:
                while True:
                    drive, word = os.path.splitdrive(word)
                    head, word = os.path.split(word)
                    if not drive:
                        break
                if word in (os.curdir, os.pardir, ''):
                    continue
                path = os.path.join(path, word)
            zf.extract(member, path)

#----------------------------------------------------------------------------------------------
#  Actions
#----------------------------------------------------------------------------------------------

# Set dir
dir = my_dir()
print os.getcwd() #check working directory

# Choose directories for processing
# dir_chooser()

#----------------------------------------------------------------------------------------------
#  Reformat ESA Folders into USGS structure
#----------------------------------------------------------------------------------------------

# get the subdirectories from input as a list
# scenes = get_immediate_subdirectories(dir_input)
#
# # Rename directories
# for scene in scenes:
# print "Scene ID: %s" % scene
# print "TODO: Subprocess"
#
# command = "/bin/bash shell_rename.sh"
# process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
# print process.returncode

#----------------------------------------------------------------------------------------------
#  Process every subdirectory
#----------------------------------------------------------------------------------------------

# get the subdirectories from input as a list
scenes = get_immediate_subdirectories(dir_input)

# Rename directories
for scene in scenes:
	print "Scene ID: %s" % scene

	command = "docker run -ti --rm -v %s:/opt/ledaps -v %s:/data -v %s:/results natriskchange/ledaps /data/%s /opt/ledaps" % (dir_auxiliary, dir_input, dir_output, scene)
	process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
	print process.communicate()
	sys.exit() # exit after first loop
