#!/usr/local/bin/python
import platform
from os import listdir
from os.path import (isfile, isdir, join, abspath)
import subprocess
import random
import sys


# Default VLC Media Player path on Windows
windows_vlc_path = "C:\Program Files\VideoLAN\VLC\VLC.exe"

# Default VLC Media Player path on Mac OS
mac_vlc_path 	 = "/Applications/VLC.app/Contents/MacOS/VLC"


# Supported Extensions
extensions 	= ['avi', 'mkv', 'mp4', 'mpg']

# List of all the playable files
playables 	= []


# DO NOT CHANGE ANYTHING FROM THIS POINT ONWARDS
# ENJOY!
def getVlcPath() :
	if platform.system() == 'Darwin':
		return mac_vlc_path

	elif platform.system() == 'Windows':
		return windows_vlc_path


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
	if len(sys.argv) > 1:
		vlc_path = getVlcPath()
		show_path = sys.argv[1]
		dig(show_path)
		print "--------------------------------------------------------------------"
		print("{0} video files found!\n").format(len(playables))
		print "--------------------------------------------------------------------"
		print("\n Let's play something for you!")
		print "--------------------------------------------------------------------"
		choice = random.choice(playables)
		play(choice)
	else:
		print "Invalid Command. \n Usage: ./PyBuff.py <show_path>"
