from fastapi import FastAPI
from .sockets import sio_app
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.mount('/', app= sio_app)    

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/index')
async def index():
    return {'msg': 'Welcome to my app'}


