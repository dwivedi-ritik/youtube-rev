## Youtube-rev

#### A lightweight Python script for downloading youtube videos 


```shell

usage: youtb.py [-h] --url  [--vtag] [--atag]

A Python script to download youtube videos withhelp of ffmpeg

optional arguments:
  -h, --help  show this help message and exit
  --url       pass video url
  --vtag      Pass itag of video quality
  --atag      Pass itag of audio quality

Download restricted videos can't be download

```


### API of this script

Instantiate an object by passing video-id of youtube video.

```python
from youtube-rev import YoutubeRev
y1 = YoutubeRev("17qbqlCgyEg")
```
Print details about video such as type , quality , itag , audio present or not

```python
y1.formatViewer()
```
Return all the video related json data such codec , itags and other stuffs.

```python 
y1.videoData()
```

Return all the video meta data such as title , description.

```python 
y1.videoInfo() 
````

This method takes two parameter itag="itag of file" , audio="True/False"  , you can find itag using .formatViewer() method

```python
y1.downloadParams(itag=241 , audio=True)
#This will download both audio and video file and merge them using ffmpeg
```
### Note

This script can't download those video which restricted for download by creator.
Youtube cipher the video urls , they keep changing their algo.


