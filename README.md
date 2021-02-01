## Youtube-rev

#### A lightweight Python script for downloading youtube videos without any thirdparty library except requests

Instantiate an object by passing video-id of youtube video.

```python
from youtube-rev import YoutubeRev
y1 = YoutubeRev("17qbqlCgyEg")
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

### Note

script can't retrive those video which are can't save offline in youtube app 
in other words those videos can't be embedded.

#### More Feature will be added soon such as ffmpeg integration , cli args , more filtering , playlist downloader.
