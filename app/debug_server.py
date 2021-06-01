from utils.settings import Settings
from database.database import Database
from server.server import app, socketio


if __name__ == '__main__':           
    database = Database()
    database.reset() 
    settings = Settings()    
    socketio.run(app, port=settings.port, debug=settings.debug)