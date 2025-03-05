from flask import Blueprint, request
from app.tools.response_manager import ResponseManager
from app.schemas.pokemon_favorites_schema import PokemonFavoriteSchema
from marshmallow import ValidationError
from app.models.factory import ModelFactory
from bson import ObjectId
from flask_jwt_extended import jwt_required, get_jwt_identity

bp = Blueprint("pokemon_favorites", __name__, url_prefix="/pokemon_favorites")
RM = ResponseManager()
FP_SCHEMA = PokemonFavoriteSchema()
FP_MODEL = ModelFactory.get_model("pokemon_favorites")

@bp.route("/", methods=["POST"])
@jwt_required()
def create():
    try:
        data = request.json
        data = FP_SCHEMA.validate(data)
        fp = FP_MODEL.create(data)
        return RM.success({"_id": fp})
    except ValidationError as err:
        print(err)
        return RM.error({"Los parámetros enviados son incorrectos"})


@bp.route("/<string:id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    FP_MODEL.delete(ObjectId(id))
    return RM.success({"Pokémon favorito eliminado con éxito"})

@bp.route("/", methods=["GET"])
@jwt_required()
def get_all():
    user_id = get_jwt_identity()
    data = FP_MODEL.find_all(user_id)
    return RM.success(data)


