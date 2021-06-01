from utils.settings import Settings
from server.server import app, socketio


if __name__ == '__main__':            
    settings = Settings()    
    socketio.run(app, port=settings.port, debug=settings.debug)