from distutils.core import setup
import py2exe, sys, os

sys.argv.append('py2exe')

setup(
    options = {'py2exe': {'bundle_files': 1, 'compressed': False, "includes": ["EasyDialogs"],"excludes": ["easygui"]}},
    windows = [{'script': "blindfiles.py",'dest_base':'blindfiles',"icon_resources": [(0, "blindfiles.ico")]}],
    console = [{'script': "blindfiles.py",'dest_base':'blindfiles_cli'}],
    zipfile = None,
)
