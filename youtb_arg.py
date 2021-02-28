from youtb_alter import YoutubeRev
import sys

url = "".join(sys.argv[1])
try:
    if sys.argv[3] == "audio": 
        audio = True
    itag = int(sys.argv[2])
except Exception:
    itag = None
    audio = False

obj1 = YoutubeRev(url)
obj1.formatedViewer()

if itag != None:
    obj1.downloadParams(itag=itag ,audio=audio)


"""Muskil Waqt Commando Shakht"""
