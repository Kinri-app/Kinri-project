from app.vaultcards import vaultcards_bp 
from app.vaultcards.schemas import vaultcard_schema, vaultcards_schema
from flask import request, jsonify
from app.models import Vaultcard, db
from sqlalchemy import select
from marshmallow import ValidationError


# -------------------Vaultcard Routes--------------------------
@vaultcards_bp.route("/", methods=["GET"])
def get_vaultcards():
    query = select(Vaultcard)
    result = db.session.execute(query).scalars().all()

    return vaultcards_schema.jsonify(result), 200

@vaultcards_bp("/<int:vaultcard_id")
def get_vaultcard_by_id(vaultcard_id):
    try:
        query = select(Vaultcard).where(Vaultcard.id == vaultcard_id)
        single_vaultcard = db.session.execute(query)

    except ValidationError as e:
        return jsonify(e.messages), 400
    
    db.session.commit()
    
    return jsonify(single_vaultcard)