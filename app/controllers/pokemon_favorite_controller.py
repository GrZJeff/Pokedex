from flask import Blueprint, request, jsonify
from app.schemas.pokemon_favorites_schema import PokemonFavoriteSchema
from marshmallow import ValidationError
from app.models.factory import ModelFactory
from bson import ObjectId

bp = Blueprint("pokemon_favorites", __name__, url_prefix="/pokemon_favorites")
pokemon_favorite_schema = PokemonFavoriteSchema()
pokemon_favorite_model = ModelFactory.get_model("pokemon_favorites")

@bp.route("/create", methods=["POST"])
def create_favorite():
    try:
        data = pokemon_favorite_schema.load(request.json)
        pokemon_favorite_id = pokemon_favorite_model.create(data)
        return jsonify({"pokemon_favorite_id": str(pokemon_favorite_id)}, 200)
    except ValidationError as err:
        return jsonify({"error": "Los parámetros enviados son incorrectos", "details": err.messages}, 400)

@bp.route("/update/<string:pokemon_favorite_id>", methods=["PUT"])
def update_favorite(pokemon_favorite_id):
    try:
        data = pokemon_favorite_schema.load(request.json)
        pokemon_favorite = pokemon_favorite_model.update(ObjectId(pokemon_favorite_id), data)
        return jsonify({"data": pokemon_favorite}, 200)
    except ValidationError as err:
        return jsonify({"error": "Los parámetros enviados son incorrectos", "details": err.messages}, 400)

@bp.route("/delete/<string:pokemon_favorite_id>", methods=["DELETE"])
def delete_favorite(pokemon_favorite_id):
    pokemon_favorite_model.delete(ObjectId(pokemon_favorite_id))
    return jsonify({"message": "Pokémon favorito eliminado con éxito"}, 200)

@bp.route("/get/<string:pokemon_favorite_id>", methods=["GET"])
def get_favorite(pokemon_favorite_id):
    pokemon_favorite = pokemon_favorite_model.find_by_id(ObjectId(pokemon_favorite_id))
    return jsonify(pokemon_favorite, 200)


