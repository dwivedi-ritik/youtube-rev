import argparse
import sys

from youtb_alter import YoutubeRev

if len(sys.argv) == 2 and sys.argv[1].startswith("http"):
    url = sys.argv[1]
    obj = YoutubeRev(url)
    obj.formatedViewer()
    exit(1)

parser = argparse.ArgumentParser(description="A Python script to download youtube videos withhelp of ffmpeg" , epilog="Download restricted videos can't be download")
parser.add_argument( "--url" , help="pass video url" , metavar='' , dest="url" , type=str , required=True)
parser.add_argument( "--vtag" , help="Pass itag of video quality" , metavar='' , dest="vtag" , type=int )
parser.add_argument( "--atag" , help="Pass itag of audio quality" , metavar='' , dest="atag" , type=int)
args = parser.parse_args()

if args.vtag == None and args.atag == None:
    print("Provide itags")
    exit(1)

obj = YoutubeRev(args.url)
obj.downloadParams(itag=args.vtag , audio=args.atag)

"""Capable of downloading videos that url are not ciphered"""