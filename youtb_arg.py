from youtb_alter import YoutubeRev
import sys

"""Command Line for the script"""

url = "".join(sys.argv[1])
audio = False
if sys.argv[-1] == "audio": 
    audio = True
try:
	if isinstance(int(sys.argv[2]) , int):
		itag = int(sys.argv[2])
except Exception:
    itag = None
obj1 = YoutubeRev(url)

if not itag and not audio:
	obj1.formatedViewer()
else:
	obj1.downloadParams(itag = itag , audio=audio)

"""Muskil Waqt Commando Shakht"""
