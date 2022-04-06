from flask import Flask

from backend.settings import Config

app = Flask(__name__, static_folder="../../frontend/static", template_folder="../../frontend/templates")
app.secret_key = Config.SECRET_KEY