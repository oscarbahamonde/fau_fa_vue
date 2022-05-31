from fastapi import APIRouter, File, UploadFile, Depends
from src.models import users
from src.middlewares import upload_to_s3, post_document
from src.auth import user
from src.utils import date_time
from src import get_session_id
from src.db import fauna
from faunadb import query as q


bucket = APIRouter()

@bucket.post('/upload')
async def upload(file: UploadFile = File(...), user: users = Depends(user)):
    print(user)
    url = upload_to_s3(file, user['id'])
    media = {
    'id' : get_session_id(),
    'uid' : user['id'],
    'filename' : file.filename,
    'url' : url,
    'content_type' : file.content_type,
    'last_modified' :  date_time()
    }
    print(media)
    try:
        print(post_document(
            col = 'media',
            data = media,
            uid = user['id']
        ))
    except Exception as e:
        print(e)
        return {'error': str(e)}
    return media