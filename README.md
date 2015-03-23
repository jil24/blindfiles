#blindfiles <img style="float:right" src="blindfiles.png">

A simple filename randomizer for experimental results requiring blind analysis.

#### Installing:

Download the [most recent release]:
* [Windows][win32] (Tested on Windows 7)
  - Simply run the .exe file.

* [Mac OS X][osx] (Tested on Yosemite).
  - Extract the .zip file whereever you like, then run the program.

* Cross-platform [Python]  
  - (python version requires packages [`easygui`][easygui] on OS X and a windows port of [`EasyDialogs`][easydialogs] on Win32)

#### Usage (GUI):
* You will need to have some files whose names you want to randomize. Put them all in one folder, or alternatively, you can randomize an entire directory tree as-is.
* You will also need a place to put the blinded copy, so create an empty folder.
* Run the program.
  * It will prompt you for the source directory, destination directory, and for the file extension to randomize.
  * Find your randomized files your selected destination directory, along with a key, `index.txt`, which reveals the original name of the file. No peeking until you're done scoring!

#### Usage (CLI/python)
```
blindfiles.py [source] [destination - must be empty, will be created if it doesn't exist] [file extension]
```
Pretty simple.

[icon]: blindfiles.png
[most recent release]: https://github.com/jil24/blindfiles/releases

[osx]: https://github.com/jil24/blindfiles/releases/download/v0.1.0/blindfiles_osx_yosemite.zip
[win32]: https://github.com/jil24/blindfiles/releases/download/v0.1.0/blindfiles_win32.exe
[Python]: blindfiles.py?raw=True
[easygui]: http://easygui.sourceforge.net/
[easydialogs]: http://www.averdevelopment.com/python/EasyDialogs.html
