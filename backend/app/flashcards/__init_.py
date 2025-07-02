from flask import Blueprint

flashcards_bp = Blueprint('flashcards_bp',__name__)

from . import routes