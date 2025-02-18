from app.models.pokemon import Pokemon
from app.models.pokemon_favorite import PokemonFavorites
from app.models.users import User

class ModelFactory:
    @staticmethod
    def get_model(collection_name):
        models = {
            "users": User,
            "pokemons": Pokemon,
            "pokemon_favorites": PokemonFavorites
        }
        if collection_name in models:
            return models[collection_name]()
        raise ValueError(f"El model enviado: {collection_name} no existe")
    
    
