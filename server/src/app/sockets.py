import socketio
from .utils import convertImageToCV

socket_io_server = socketio.AsyncServer(
     async_mode='asgi',
     cors_allowed_origins=[]
)

sio_app = socketio.ASGIApp(
    socketio_server=socket_io_server,
    socketio_path='sockets'
)

@socket_io_server.event
async def connect(sid, environ, auth):
    print(f'{sid}: connected')


@socket_io_server.event
async def disconnect(sid):
    print(f'{sid}: disconnected')

@socket_io_server.event
async def capture(sid, data):
    print(convertImageToCV(data['data']))

