from flask import Blueprint

vaultcards_bp = Blueprint('vaultcards_bp',__name__)

from . import routes