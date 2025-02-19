from flask import Blueprint, request, jsonify
from app.schemas.user_schema import UserSchema
from marshmallow import ValidationError
from app.models.factory import ModelFactory
from bson import ObjectId
from app.tools.response_manager import ResponseManager

RM = ResponseManager()
bp = Blueprint("users", __name__, url_prefix="/users")
user_schema = UserSchema()
user_model = ModelFactory.get_model("users")

@bp.route("/login", methods=["POST"])
def login():
    data = request.json
    email = data.get("email", None)
    password = data.get("password", None)
    if not email or not password:
        return RM.error("Es necesario enviar toadas las credenciales")
    user = user_model.get_by_email_password(email, password)
    if not user:
        return RM.error("No se encontro un usuario")
    return RM.success(user)
    

@bp.route("/register", methods={"POST"})
def register():
    data = user_schema.load(request.json)
    try:
        data = user_schema.load(request.json)
        user_id = user_model.craete(data)
        return RM.success({"user_id": str(user_id)})
    except ValidationError as err:
        return RM.error("Los parametros enviados son incorrectos")
    
@bp.route("/update/<string:user_id>", methods=["PUT"])
def update(user_id):
        try:
            data= user_schema.load(request.json)
            user = user_model.update(ObjectId(user_id), data)
            return RM.success({ "data": user})
        except ValidationError as err:
            return RM.error("Los parametros enviandos son incorrectos")
        

@bp.route("/delete/<string:user_id>", methods=["DELETE"])
def delete(user_id):
    user_model.delete(ObjectId(user_id))
    return RM.error("Usuario eliminado con exito")

@bp.route("/get/<string:user_id>", methods=["GET"])
def get_user(user_id):
    user = user_model.find_by_id(ObjectId(user_id))
    return RM.error(user)