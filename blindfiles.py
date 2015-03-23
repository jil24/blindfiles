#!/usr/bin/python
#Public Domain
import os
import sys
import re
import shutil
import EasyDialogs
from random import sample

if len(sys.argv) == 1:
    print("use `blindfiles.py --help` for command line options")
    origdir = EasyDialogs.AskFolder(message="Choose directory with files to blind", windowTitle = "Choose Source")
    if origdir is None: sys.exit()
    blinddir = EasyDialogs.AskFolder(message="Choose an empty directory to place blinded files", windowTitle="Choose Destination")
    if blinddir is None: sys.exit()
    suffix = EasyDialogs.AskString(prompt='Enter file extensions to blind (e.g. `.jpg` or `.tif`)', default='.tif')
    if suffix is None: sys.exit()
elif len(sys.argv) < 4:
    print("")
    print("blindfiles.py assigns files in a directory tree a random name to reduce bias during subjective scoring procedures")
    print("original names and paths are stored in index.txt")
    print("blindfiles makes a blind copy and leaves the originals alone")
    print("usage: blindfiles.py <directory to blind (recursive)> <Directory to place blinded files (must not exist or be empty)> <file extensions to blind including dot>")
    print("")
    sys.exit()
else:
    origdir = sys.argv[1]
    blinddir = sys.argv[2]
    suffix = sys.argv[3]

filenamearray = []
fullpatharray = []

# example code modified from stackoverflow.com
for dirname, dirnames, filenames in os.walk(origdir):
    for filename in filenames:
        if filename.endswith(suffix):
#        if re.search(suffix+"$",filename):
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
    print("Creating directory " + blinddir)
#don't block on dotfiles. I'm lookin at you, .DS_Store!
if [f for f in os.listdir(blinddir) if not f.startswith('.')] != []:
    print("Error! Directory to place blinded files must not exist or must be empty")
    sys.exit()

index = open(os.path.join(blinddir,"index.txt"), "w")
index.write("Blind File\tOrig File\tOrig pathfile\n")

for entry in blinded:
    newbasename=str(entry[0])
    newextension=os.path.splitext(entry[2])[1]
    index.write(newbasename+newextension+"\t"+entry[1]+"\t"+entry[2]+"\n")
    shutil.copy(entry[2], os.path.join(blinddir,newbasename+newextension))

index.close()
