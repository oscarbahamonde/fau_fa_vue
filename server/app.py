from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.staticfiles import StaticFiles
from starlette.responses import HTMLResponse, RedirectResponse
from src.auth import auth
from src.routes import yt
from src.hooks import bucket
from src.db import useDB
import random
from src import get_session_id 

app: FastAPI = useDB(FastAPI())
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.mount("/video", StaticFiles(directory="src/static/video"), name="video")

app.include_router(auth)


app.include_router(yt, prefix='/yt')
app.include_router(bucket)
@app.get("/id")
def session_id():
    return  get_session_id()

@app.get("/avatar")
async def avatar():
    choices = ['micah','gridy','avataaars','bottts','human']
    choice = random.choice(choices)
    return f'https://avatars.dicebear.com/api/{choice}/{get_session_id()+get_session_id()}.svg'
   

@app.get("/wp-admin")
async def random_avatar():
    choices = ['micah','gridy','avataaars','bottts','human']
    choice = random.choice(choices)
    return RedirectResponse(f'https://avatars.dicebear.com/api/{choice}/{get_session_id()+get_session_id()}.svg')

@app.get("/.env")
def rickroll_the_hackers()->HTMLResponse:
    # Autoplay with Javascript
    html='''<iframe width="1366" height="768" src="https://www.youtube.com/embed/dQw4w9WgXcQ?controls=0&disablekb=1&fs=0&loop=1&modestbranding=1&rel=0&showinfo=0&start=0&autoplay=1&mute=1" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
   '''
    return HTMLResponse(html)

