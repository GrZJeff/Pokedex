from marshmallow import Schema, fields, ValidationError

class PokemonSchema(Schema):
    pokemon_id = fields.Str(
        required=True,
        validate=lambda x: len(x) > 0,
        error_messages={
            "required": "El id del Pokémon es requerido"
        }
    )
    name = fields.Str(
        required=True,
        validate=lambda x: len(x) > 0,
        error_messages={
            "required": "El nombre del Pokémon es requerido"
        }
    )