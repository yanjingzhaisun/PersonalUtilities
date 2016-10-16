#!/usr/local/bin/python3
import os
import sys
import glob
import shutil

# get a list of all txt files
import datetime
foldername = '~/Music/temp/' + datetime.datetime.now().strftime('%Y%m%d')
os.system('mkdir －p ' + foldername )
if (len(sys.argv) < 2):
    url = input("Enter URL: ")
else:
    url = sys.argv[1]
bashCommand = "youtube-dl --extract-audio --audio-format mp3 --audio-quality 0 -o '" + foldername + "/%(title)s.%(ext)s' "
# sort according to time of last modification/creation (os-dependent)
# reverse: newer files first
os.system(bashCommand + url)
