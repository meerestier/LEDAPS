# Python Script to moderate LEDAPS Docker Workflow
# Name: Launch LEDAPS
# Description: Describes what your action will do.
# Handles: Files, Folders
# Creator: Lars Schulz
# URL: http://eco.systemic.de
# Version: 0.0.1


import time
import os, sys

#----------------------------------------------------------------------------------------------
# globals 
#----------------------------------------------------------------------------------------------

dir = "~/Desktop"
# Directory with Subdirectories of Scenes
dir_input = "/Volumes/DATA_DRIVE/NatRiskChange/Data"
dir_output = "/Volumes/DATA_DRIVE/NatRiskChange/Results"
dir_auxiliary

#----------------------------------------------------------------------------------------------
# helper functions
#----------------------------------------------------------------------------------------------

def my_dir():
	'''Get the path'''
	global dir
	# https://docs.python.org/2/library/os.path.html
	dir = os.path.dirname( os.path.abspath(__file__) )
	print dir
	return dir

def dir_chooser():
	global dir_input, dir_output
	dir_input = raw_input('Enter path to source folder: ')
	dir_output = raw_input('Enter path to results folder: ') 
	return str(folder)

def get_immediate_subdirectories(dir):
    return [name for name in os.listdir(dir)
            if os.path.isdir(os.path.join(dir, name))]

def cleanup():
    # TODO implement
    global data

def read_text_clip():
    global data
    data = dz.read_clipboard().splitlines()

def read_text():
    global data, text
    text = open(items[0], "r")
    data = text.read().splitlines()
    print "data: ", data
    print "data 1: ", data[0]

def create_folder():
    global data
    count = 1

    for data in data:
        # progress
        print count
        print len(data[0])

        count += 1
        dz.percent( count/len(data[0]) * 100)
        current_name = dir + "/" + data
        print current_name
        if not os.path.exists(current_name):
            os.makedirs(current_name)
            
	

#----------------------------------------------------------------------------------------------
#  Actions
#----------------------------------------------------------------------------------------------

dir_chooser()

scenes = get_immediate_subdirectories(dir_input)
print scenes


# same as above
for scene in scenes:
    print "Scene ID: %s" % scene
    print "TODO: Subprocess"






# def dragged():
#     # Do Action
#     my_dir()
#     read_text()
#     create_folder()
# 
#     # Notify completion
#     dz.finish("Folders created.")
#  
# def clicked():
#     global dir
#     # TODO: Set dir dynamically at finder selection
# 
#     # Use clipboard content for folder creation
#     read_text_clip()
#     create_folder()
# 
#     # Notify completion
#     dz.finish("Folders created from clipboard.")
#     dz.url(False)
