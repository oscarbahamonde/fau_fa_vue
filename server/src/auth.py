from fastapi import APIRouter, Depends, FastAPI
from requests import post
from src.config import process
from starlette.responses import RedirectResponse
from src.models import users


auth = APIRouter()



@auth.get("/")
async def redirect_to_login():
    return RedirectResponse(process.env.COGNITO_IDP_HOSTED_UI_URL)
@auth.get('/token')
async def token(code: str):
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'grant_type': 'authorization_code',
        'client_id': process.env.COGNITO_APP_CLIENT_ID,
        'client_secret': process.env.COGNITO_APP_CLIENT_SECRET,
        'code': code,
        'redirect_uri': process.env.COGNITO_CALLBACK_URL
    }
    payload = post(process.env.COGNITO_TOKEN_URL, headers=headers, data=data)
    return RedirectResponse(process.env.FRONTEND_URL + '/user?token=' + payload.json()['access_token'])
@auth.post('/token', response_model=users)
def user(access_token:str)->users:
    user_info_endpoint = process.env.COGNITO_DOMAIN_URL + '/oauth2/userInfo'
    headers = {
        'Authorization': 'Bearer ' + access_token
    }
    payload = post(user_info_endpoint, headers=headers)
    user = {
        'id': payload.json()['sub'],
        'username': payload.json()['username'],
        'email': payload.json()['email']
    }
    return user

@auth.post('/config')
def config(access_token = Depends(user)):
    if access_token is None:
        return {'error': 'no user'}
    firebase_config = {
        'apiKey': process.env.FIREBASE_API_KEY,
        'authDomain': process.env.FIREBASE_AUTH_DOMAIN,
        'projectId': process.env.FIREBASE_PROJECT_ID,
        'storageBucket': process.env.FIREBASE_STORAGE_BUCKET,
        'messagingSenderId': process.env.FIREBASE_MESSAGING_SENDER_ID,
        'appId': process.env.FIREBASE_APP_ID,
        'measurementId': process.env.FIREBASE_MEASUREMENT_ID
    }
    return firebase_config