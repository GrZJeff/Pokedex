from marshmallow import Schema, fields, ValidationError

class PokemonFavoriteSchema(Schema):
    pokemon_id = fields.Str(
        required=True,
        validate=lambda x: len(x) > 0,
        error_messages={
            "required": "El id del Pokémon es requerido"
        }
    )
    user_id = fields.Str(
        required=True,
        validate=lambda x: len(x) > 0,
        error_messages={"required": "El id del usuario es requerido"
        }
    )
