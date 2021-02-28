## Youtube-rev

#### A lightweight Python script for downloading youtube videos 

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

Return all the json data without filtering and formatting.
```python
y1.jsonData()
```

This return video url and json data of highest quality video but audio are absent.

```python
y1.filter["adaptiveVideos"]
```

This retrun json data of audio link of that video. Do note youtube audio are in webm format you have to encode in mp3.

```python
y1.filter["audios"]
```
This return link and json data of that video in which both audio and video is available.

```python
y1.filter["videos"]
```
This will download that video file which have both audio and video

```python
y1.download()
```

This method takes two parameter itag="itag of file" , audio="True/False"  , you can find itag using .formatViewer() method

```python
y1.downloadParams(itag=241 , audio=True)
#This will download both audio and video file and merge them using ffmpeg
```
### Note

This script can't download those video which restricted for download by creator.
Youtube cipher the video urls , they keep changing their algo.


