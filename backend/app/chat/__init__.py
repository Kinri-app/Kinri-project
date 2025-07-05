from flask import Blueprint

conversations_bp = Blueprint('conversations_bp',__name__)

from . import routes