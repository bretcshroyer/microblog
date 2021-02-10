from flask import Blueprint

bp = Blueprint('main', __name__)

from app.applications import app1
from app.applications import app2
from app.main import routes
