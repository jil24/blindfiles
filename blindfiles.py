#!/usr/bin/python
#Public Domain
import os
import sys
import re
import shutil

myos = sys.platform

if myos == 'win32':
    import EasyDialogs
if myos == 'darwin':
    import easygui

def showMessage(message=''):
    if len(sys.argv) == 1:
        if myos == 'win32':
            EasyDialogs.Message(message)
            return None
        if myos == 'darwin':
            easygui.msgbox(message)
            return None
    else:
        print(str(message)+"\n")
        return None
            

from random import sample

if len(sys.argv) == 1:
    print("use `blindfiles.py --help` for command line options")
    if myos == 'win32':
        origdir = EasyDialogs.AskFolder(message="Choose directory with files to blind", windowTitle = "Choose Source")
    if myos == 'darwin':
        origdir = easygui.diropenbox(title="Choose directory with files to blind")
    if origdir is None: sys.exit()
    if myos == 'win32':
        blinddir = EasyDialogs.AskFolder(message="Choose an empty directory to place blinded files", windowTitle="Choose Destination")
    if myos == 'darwin':
        blinddir = easygui.diropenbox(title="Choose empty directory to place blinded files")
    if blinddir is None: sys.exit()
    if myos == 'win32':
        suffix = EasyDialogs.AskString(prompt='Enter file extensions to blind (e.g. `.jpg` or `.tif`)', default='.tif')
    if myos == 'darwin':
        suffix = easygui.enterbox(msg='Enter file extensions to blind (e.g. `.jpg` or `.tif`)', title='File extensions to blind', default='.tif', strip=True)
    if suffix is None: sys.exit()
elif len(sys.argv) < 3:
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
    if len(sys.argv) > 3: suffix = sys.argv[3]
    else: suffix = ''

filenamearray = []
fullpatharray = []

# example code modified from stackoverflow.com
for dirname, dirnames, filenames in os.walk(origdir):
    for filename in filenames:
        fullpath = os.path.join(dirname, filename)
        #hardcoded to ignore dotfiles
        if filename.endswith(suffix) and os.path.isfile(fullpath) and (not filename.startswith(".")):
            filenamearray.append(filename)
            fullpatharray.append(fullpath)

blindingarray = sample(xrange(len(filenamearray)), len(filenamearray))

blinded = zip(blindingarray, filenamearray, fullpatharray)

if len(blinded) == 0:
    showMessage("Error: No files matched the extension specified.")
    sys.exit()

nfiles = len(blinded)
digitsneeded = len(str(nfiles))

if not os.path.exists(blinddir):
    os.makedirs(blinddir)
    print("Creating directory " + blinddir)
#don't block on dotfiles. I'm lookin at you, .DS_Store!
if [f for f in os.listdir(blinddir) if not f.startswith('.')] != []:
    showMessage("Error: Directory to place blinded files must either not exist or be empty")
    sys.exit()

index = open(os.path.join(blinddir,"index.txt"), "w")
index.write("Blind File\tOrig File\tOrig pathfile\n")

for entry in blinded:
    newbasename= '%0*d' % (digitsneeded,entry[0]+1)
    newextension=os.path.splitext(entry[2])[1]
    index.write(newbasename+newextension+"\t"+entry[1]+"\t"+entry[2]+"\n")
    shutil.copy(entry[2], os.path.join(blinddir,newbasename+newextension))
index.close()

showMessage("Success: Blinded " + str(nfiles) + " files.\n")