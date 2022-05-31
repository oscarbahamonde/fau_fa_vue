import re
from typing import List
from pytube import YouTube
from requests import get
from starlette.responses import FileResponse
from urllib.parse import quote
def get_youtube_ids(url) -> List[str]:
    """
    Gets the video ids from a youtube url
    """
    html = get(url).text
    videoIds = re.findall(r'"videoId":"(.*?){11}"', html)
    res = []
    for i in range(len(videoIds)):
        video = {
            "id": videoIds[i],
            'url': f'https://www.youtube.com/watch?v={videoIds[i]}'
        }
        res.append(video)
    return res

def download_youtube_video(url, path="src/static/video")->FileResponse:
    """
    Downloads a youtube video
    """
    yt = YouTube(url)
    yt.streams.filter(progressive=True, file_extension='mp4').order_by(
        'resolution').desc().first().download(path)
    filepath = f'video/{quote(yt.title)}.mp4' or f'video/{yt.title}.mp4'
    return FileResponse(filepath, media_type='video/mp4')
