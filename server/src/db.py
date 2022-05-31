from fastapi import Depends, FastAPI
from src.config import process
from faunadb.client import FaunaClient
from faunadb import query as q
from pydantic import BaseModel
import src.models as I
from src.auth import user


fauna: FaunaClient = FaunaClient(secret=process.env.FAUNA_SECRET, domain=process.env.FAUNA_DOMAIN, scheme=process.env.FAUNA_SCHEME, port=443)

collections = [
    I.users,
    I.media,
    I.posts,
    I.comments,
    I.reactions,
    I.tracks,
    I.videos,
    I.images,
    I.skills,
    I.projects,
    I.profiles,
    I.roles,
]

def fauna_create_all():
    for collection in collections:
            fauna.query(q.create_collection({
                "name": collection.__name__
            }
            ))
    for collection in collections:
        fauna.query(q.create_index({
            "name": f"{collection.__name__}_by_uid",
            "source": q.collection(collection.__name__),
            "terms": [  
            {
                "field": ["data", "uid"]
            }
            ]
        }))



def useDB(app:FastAPI)->FastAPI:
    @app.on_event('startup')
    async def startup():
        try:
            fauna_create_all()
        except Exception as e:
            print(e)
    return app


    #Top Level Functions

def post_document(collection:str, data:BaseModel, user:I.users=Depends(user)):
    document = {
        "data": {
            "uid": user.uid,
            **data.dict()
        }
    }
    try:
        response = fauna.query(q.create(q.collection(collection), document))
        return response['ref']
    except Exception as e:
        print(e)
        return None

def get_document(collection:str, ref:str = Depends(post_document)):
    try:
        response = fauna.query(q.collection(collection).get(ref))
        return response['data']
    except Exception as e:
        print(e)
        return None

def get_documents(collection:str, uid:str):
    try:
        response = fauna.query(q.collection(collection).filter(q.match(q.index(f"{collection}_by_uid"), uid)))
        return response
    except Exception as e:
        print(e)
        return None

def put_document(collection:str, data:BaseModel,ref:str = Depends(post_document)):
    try:
        response = fauna.query(q.update(q.collection(collection).get(ref), data = data.dict()))
        return response
    except Exception as e:
        print(e)
        return None

def put_documents(collection:str, data:BaseModel, uid:str):
    try:
        response = fauna.query(q.update(q.collection(collection).filter(q.match(q.index(f"{collection}_by_uid"), uid)), data = data.dict()))
        return response
    except Exception as e:
        print(e)
        return None

def delete_document(collection:str, ref:str = Depends(post_document)):
    try:
        response = fauna.query(q.delete(q.collection(collection).get(ref)))
        return response
    except Exception as e:
        print(e)
        return None

def delete_documents(collection:str, uid:str):
    try:
        response = fauna.query(q.delete(q.collection(collection).filter(q.match(q.index(f"{collection}_by_uid"), uid))))
        return response
    except Exception as e:
        print(e)
        return None

