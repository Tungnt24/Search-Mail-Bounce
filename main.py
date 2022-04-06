from backend.settings import Config

from backend.routers import app
from backend.routers.search import search_bp

app.register_blueprint(search_bp)

if __name__ == "__main__": 
    app.run(port=Config.PORT, host=Config.HOST)
