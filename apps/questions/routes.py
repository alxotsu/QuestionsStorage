from core import app
from .views import index

def route_views():
    app.route("/", methods=['POST'])(index)
