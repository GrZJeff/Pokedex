from app import mongo
from app.models.super_clase import SuperClass

class User(SuperClass):
 def __init__(self):
     super().__init__("users")