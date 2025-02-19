from flask import Blueprint, request, jsonify
from app.tools.response_manager import ResponseManager
from app.models.factory import ModelFactory
from bson import ObjectId

bp = Blueprint("pokemon", __name__, url_prefix="/pokemon")
RM = ResponseManager()
POKEMON_MODEL = ModelFactory.get_model("pokemon")

@bp.route("/", methods=["GET"])
def find_all():
    data = POKEMON_MODEL.find_all()
    return RM.success(data)

@bp.route("/<string:pokemon_id>", methods=["GET"])
def find_by_id(pokemon_id):
    pokemon = POKEMON_MODEL.find_by_id(ObjectId(pokemon_id))
    if not pokemon:
        return RM.error("Pokémon no encontrado")
    return RM.success(pokemon)