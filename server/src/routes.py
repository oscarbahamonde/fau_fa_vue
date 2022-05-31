from src.lib import download_youtube_video, get_youtube_ids
from fastapi import APIRouter
from src.models import *
from src.middlewares import upload_to_s3, post_document

yt = APIRouter()

@yt.get("/")
async def download_video(url: str):
    return download_youtube_video(url)

@yt.post("/")
def yt_ids(url: str):
    return get_youtube_ids(url)


