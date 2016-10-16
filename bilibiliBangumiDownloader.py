#!/usr/local/bin/python3
import os
import sys
import glob
import shutil

# get a list of all txt files
import datetime
foldername = '~/Movie/temp/' + datetime.datetime.now().strftime('%Y%m%d')
os.system('mkdir －p ' + foldername )
if (len(sys.argv) < 2):
    url = input("Enter URL: ")
else:
    url = sys.argv[1]

if (len(sys.argv) < 3):
    lengthStr = input("Enter Length:")
else:
    lengthStr = sys.argv[2]

length = int(lengthStr)

bashCommand = "youtube-dl -o '" + foldername + "/%(title)s.%(ext)s' "

startPos = url.rfind('/')
startUrl = url[:startPos+1]
startUrlNumber = int(url[startPos + 1:])
print(startUrl + str(startUrlNumber + 2))

for current in range(0, length):
    url = startUrl+str(startUrlNumber + current)
    os.system(bashCommand + url)

# sort according to time of last modification/creation (os-dependent)
# reverse: newer files first

