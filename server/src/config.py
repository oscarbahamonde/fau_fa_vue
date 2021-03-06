from dotenv import load_dotenv
from os import getenv
load_dotenv()

class process:
    class env:
        AWS_ACCESS_KEY_ID = getenv('AWS_ACCESS_KEY_ID')
        AWS_SECRET_ACCESS_KEY = getenv('AWS_SECRET_ACCESS_KEY')
        AWS_REGION_NAME= getenv('AWS_REGION_NAME')
        AWS_BUCKET_NAME= getenv('AWS_BUCKET_NAME')
        COGNITO_APP_CLIENT_ID= getenv('COGNITO_APP_CLIENT_ID')
        COGNITO_APP_CLIENT_SECRET= getenv('COGNITO_APP_CLIENT_SECRET')
        COGNITO_DOMAIN_URL= getenv('COGNITO_DOMAIN_URL')
        COGNITO_USER_POOL_ID= getenv('COGNITO_USER_POOL_ID')
        COGNITO_CALLBACK_URL= getenv('COGNITO_CALLBACK_URL')
        COGNITO_IDP_HOSTED_UI_URL = getenv('COGNITO_IDP_HOSTED_UI_URL')
        COGNITO_TOKEN_URL= getenv('COGNITO_TOKEN_URL')
        COGNITO_ISSUER= getenv('COGNITO_ISSUER')
        FRONTEND_URL= getenv('FRONTEND_URL')
        MYSQL_URI= getenv('MYSQL_URI')
        FAUNA_DOMAIN= getenv('FAUNA_DOMAIN')
        FAUNA_SCHEME= getenv('FAUNA_SCHEME')
        FAUNA_SECRET= getenv('FAUNA_SECRET')
        FIREBASE_API_KEY= getenv('firebase_apiKey')
        FIREBASE_AUTH_DOMAIN= getenv('firebase_authDomain')
        FIREBASE_PROJECT_ID= getenv('firebase_projectId')
        FIREBASE_STORAGE_BUCKET= getenv('firebase_storageBucket')
        FIREBASE_MESSAGING_SENDER_ID= getenv('firebase_messagingSenderId')
        FIREBASE_APP_ID= getenv('firebase_appId')
        FIREBASE_MEASUREMENT_ID= getenv('firebase_measurementId')