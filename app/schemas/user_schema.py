from marshmallow import Schema, fields, ValidationError

class UserSchema(Schema):
    name = fields.Str(
        requiered=True,
        validate=lambda x:len (x) > 0,
        error_messages={
            "required": "El nombre es requerido"
        }
    )
    password = fields.Str(
        requiered=True,
        validate=lambda x:len (x) > 0,
        error_messages={
            "required": "El contraseña es requerido"
        }
    )
    email = fields.Str(
        requiered=True,
        validate=lambda x:"@" in x,
        error_messages={
            "required": "El correo es requerido"
        }
    )

