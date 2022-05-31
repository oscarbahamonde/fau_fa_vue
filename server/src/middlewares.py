from fastapi import Request, Depends, File, UploadFile
from pydantic import BaseModel, HttpUrl
from faunadb import query as q
from faunadb.objects import Query, Ref
from boto3 import client
from src.config import process
from starlette.responses import FileResponse
from src  import models as m
from typing import List, Dict
from src.db import fauna
from urllib.parse import quote
import json
def useAws(service:str):
    return client(service,
        aws_access_key_id=process.env.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=process.env.AWS_SECRET_ACCESS_KEY,
        region_name=process.env.AWS_REGION_NAME)

s3 = useAws('s3')

CONTENT_TYPES = {
        'jpg': 'image/jpeg',
        'jpeg': 'image/jpeg',
        'png': 'image/png',
        'gif': 'image/gif',
        'mp4': 'video/mp4',
        'webm': 'video/webm',
        'svg': 'image/svg+xml',
        'mp3': 'audio/mp3',
        'wav': 'audio/wav',
        'ogg': 'audio/ogg',
        'pdf': 'application/pdf',
        'doc': 'application/msword',
        'docx': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
        'xls': 'application/vnd.ms-excel',
        'xlsx': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        'ppt': 'application/vnd.ms-powerpoint',
        'pptx': 'application/vnd.openxmlformats-officedocument.presentationml.presentation',
        'txt': 'text/plain',
        'md': 'text/markdown',
        'html': 'text/html',
        'json': 'application/json',
        'zip': 'application/zip',
        'rar': 'application/x-rar-compressed',
        '7z': 'application/x-7z-compressed',
        'tar': 'application/x-tar',
        'gz': 'application/x-gzip',
        'bz2': 'application/x-bzip2',
        'iso': 'application/x-iso9660-image',
        'exe': 'application/x-msdownload',
        'msi': 'application/x-msdownload',
        'dmg': 'application/x-apple-diskimage',
        'apk': 'application/vnd.android.package-archive',
        'ipa': 'application/vnd.android.package-archive',
        'xpi': 'application/x-xpinstall',
        'xz': 'application/x-xz',
        'cab': 'application/vnd.ms-cab-compressed',
        'deb': 'application/vnd.debian.binary-package',
        'ar': 'application/x-unix-archive',
        'rpm': 'application/x-rpm',
        'msi': 'application/x-msi',
        'bin': 'application/octet-stream',
    }


def upload_to_s3(file: UploadFile, uid:str)->HttpUrl:
    key = f'{uid}/{file.filename}'
    url = f'https://{process.env.AWS_BUCKET_NAME}.s3.{process.env.AWS_REGION_NAME}.amazonaws.com/{key}'
    s3.put_object(
        Bucket=process.env.AWS_BUCKET_NAME,
        Key=key,
        Body=file.file,
        ContentType=CONTENT_TYPES.get(file.filename.split('.')[-1]),
        ACL='public-read'
    )
    return url

def collection_exists(collection: str) -> bool:
    return fauna.query(q.exists(q.collection(collection)))

def create_collection(collection: str):
    if not collection_exists(collection):
        fauna.query(q.create_collection(q.collection(collection)))
    else:
        print(f'Collection {collection} already exists')

def post_document(data: dict, uid:str,col:str ):
    collection = col
    try:
        return fauna.query(q.create(q.collection(collection),  {
            "data": {

            'user': uid,
            **data
            }
        }))
    except Exception as e:
        print(e)
        return {'error': str(e)}
