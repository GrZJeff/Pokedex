from flask import Blueprint, request, jsonify
from app.schemas.user_schema import UserSchema
from marshmallow import ValidationError
from app.models.factory import ModelFactory
from bson import ObjectId


bp = Blueprint("users", __name__, url_prefix="/users")
user_schema = UserSchema()
user_model = ModelFactory.get_model("users")

@bp.route("/login", methods=["POST"])
def login():
    data = request.json
    email = data.get("email", None)
    password = data.get("password", None)
    if not email or not password:
        return jsonify("Es necesario enviar toadas las credenciales", 400)
    user = user_model.get_by_email_password(email, password)
    if not user:
        return jsonify("No se encontro un usuario", 400)
    return jsonify(user,200)
    

@bp.route("/register", methods={"POST"})
def register():
    data = user_schema.load(request.json)
    try:
        data = user_schema.load(request.json)
        user_id = user_model.craete(data)
        return jsonify({"user_id": str(user_id)}, 200)
    except ValidationError as err:
        return jsonify("Los parametros enviados son incorrectos", 400)
    
@bp.route("/update/<string:user_id>", methods=["PUT"])
def update(user_id):
        try:
            data= user_schema.load(request.json)
            user = user_model.update(Object(user_id), data)
            return jsonify({
                "data": user
            }, 200)
        except ValidationError as err:
            return jsonify("Los parametros enviandos son incorrectos", 400)
        

@bp.route("/delete/<string:user_id>", methods=["DELETE"])
def delete(user_id):
    user_model.delete(ObjectId(user_id))
    return jsonify("Usuario eliminado con exito", 200)

@bp.route("/get/<string:user_id>", methods=["GET"])
def get_user(user_id):
    user = user_model.find_by_id(ObjectId(user_id))
    return jsonify(user,200)