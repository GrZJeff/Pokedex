from flask import Blueprint, request, jsonify
from app.schemas.pokemon_schema import PokemonSchema
from marshmallow import ValidationError
from app.models.factory import ModelFactory
from bson import ObjectId

bp = Blueprint("pokemons", __name__, url_prefix="/pokemons")
pokemon_schema = PokemonSchema()
pokemon_model = ModelFactory.get_model("pokemons")

@bp.route("/create", methods=["POST"])
def create_pokemon():
    try:
        data = pokemon_schema.load(request.json)
        pokemon_id = pokemon_model.create(data)
        return jsonify({"pokemon_id": str(pokemon_id)}, 200)
    except ValidationError as err:
        return jsonify({"error": "Los parámetros enviados son incorrectos", "details": err.messages}, 400)

@bp.route("/update/<string:pokemon_id>", methods=["PUT"])
def update_pokemon(pokemon_id):
    try:
        data = pokemon_schema.load(request.json)
        pokemon = pokemon_model.update(ObjectId(pokemon_id), data)
        return jsonify({"data": pokemon}, 200)
    except ValidationError as err:
        return jsonify({"error": "Los parámetros enviados son incorrectos", "details": err.messages}, 400)

@bp.route("/delete/<string:pokemon_id>", methods=["DELETE"])
def delete_pokemon(pokemon_id):
    pokemon_model.delete(ObjectId(pokemon_id))
    return jsonify({"message": "Pokémon eliminado con éxito"}, 200)

@bp.route("/get/<string:pokemon_id>", methods=["GET"])
def get_pokemon(pokemon_id):
    pokemon = pokemon_model.find_by_id(ObjectId(pokemon_id))
    return jsonify(pokemon, 200)
