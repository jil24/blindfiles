#!/usr/bin/python
#Written / Public Domain'd by Jonathan Lake 4/2011
import os
import sys
import re
import shutil
from random import sample

if len(sys.argv) < 4:
	print("blindfiles assigns files in a directory tree a random name to reduce bias during subjective scoring procedures")
	print("original names and paths are stored in index.txt")
	print("blindfiles makes a blind copy and leaves the originals alone")
	print("usage: blindfiles.py <directory tree to blind> <Directory to place blinded files (must not exist)> <file extensions to blind including dot>")
	sys.exit()

origdir = sys.argv[1]
blinddir = sys.argv[2]
suffix = sys.argv[3]

filenamearray = []
fullpatharray = []


# example code modified from stackoverflow.com
for dirname, dirnames, filenames in os.walk(origdir):
    for filename in filenames:
		if re.search(suffix+"$",filename):
			fullpath = os.path.join(dirname, filename)
			filenamearray.append(filename)
			fullpatharray.append(fullpath)

blindingarray = sample(xrange(len(filenamearray)), len(filenamearray))

blinded = zip(blindingarray, filenamearray, fullpatharray)

if len(blinded) == 0:
	print("No files to blind")
	sys.exit()

if not os.path.exists(blinddir):
    os.makedirs(blinddir)
else:
	print("Destination exists! Bailing out!")
	sys.exit()

index = open(os.path.join(blinddir,"index.txt"), "w")
index.write("Blind File\tOrig File\tOrig pathfile\n")

for entry in blinded:
	newbasename=str(entry[0])
	newextension=os.path.splitext(entry[2])[1]
	index.write(newbasename+newextension+"\t"+entry[1]+"\t"+entry[2]+"\n")
	shutil.copy(entry[2], os.path.join(blinddir,newbasename+newextension))

index.close()