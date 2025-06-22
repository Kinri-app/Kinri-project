from app.models import Vaultcard
from app.extensions import ma

class VaultcardSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Vaultcard

vaultcard_schema = VaultcardSchema()
vaultcards_schema = VaultcardSchema(many=True)
