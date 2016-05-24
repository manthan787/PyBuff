#!/usr/local/bin/python

import platform
from os import listdir
from os.path import (isfile, isdir, join, abspath)
import subprocess
import random

# Where your Show is located on your computer
show_path 	= "/Users/admin/Desktop/season7"
# Supported Extensions
extensions 	= ['avi', 'mkv', 'mp4', 'mpg']
# List of all the playable files
playables 	= []


def getVlcPath() :

	if platform.system() == 'Darwin':
		return "/Applications/VLC.app/Contents/MacOS/VLC"

	elif platform.system() == 'Windows':
		return "C:\Program Files\VideoLAN\VLC\VLC.exe"


def dig(path) :
	try:
		# Get the list of all the directories and files for the given path
		result = listdir(path)
		print result

		if result:
			for item in result:
				item_path = join(path, item)

				# If the item is a file and is playable add it to the playables list
				if isfile(item_path) and isPlayable(item):
					file_path = join(path, item)
					print "Adding New Playable : "+file_path
					playables.append(file_path)

				# If the item is a directory, recursively dig into it to find any playables
				elif isdir(item_path) :
					dir_path = join(path, item)
					current_dir = item
					dig(dir_path)

	except Exception as e:
		print("An Error Occurred while digging through folders!\n")
		print(e)


def isPlayable(file) :
	# Pick the last value in the list returned after the split
	file_extension = file.split(".")[-1]

	if file_extension in extensions:
		return True


def play(video_path) :
	try:
		subprocess.call([vlc_path, video_path, "--play-and-exit","--fullscreen"])
	except OSError :
		print("\nLooks like you haven't installed VLC Media Player. If You're on Windows, try and change the vlc_path in the script!")


if __name__ == "__main__":
	vlc_path = getVlcPath()
	dig(show_path)
	print "--------------------------------------------------------------------"
	print("{0} video files found!\n").format(len(playables))
	print "--------------------------------------------------------------------"
	print("\n Let's play something for you!")
	print "--------------------------------------------------------------------"
	choice = random.choice(playables)
	play(choice)
