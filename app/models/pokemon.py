from app import mongo

class Pokemon: 
    collection = mongo.db.pokemons

    @staticmethod
    def find_all():
        pokemons = Pokemon.collection.find()
        return list(pokemons)
    
    @staticmethod
    def find_by_id(pokemon_id):
        pokemon = Pokemon.collection.find_one({
            "_id": pokemon_id
        })
        return pokemon
    
    @staticmethod
    def create(data):
        pokemon = Pokemon.collection.insert_one(data)
        return pokemon.inserted_id
    
    @staticmethod
    def update(pokemon_id, data):
        pokemon = Pokemon.collection.update_one({
            "_id":pokemon_id
        },{
            "$set":data
        })
        return pokemon
    
    @staticmethod
    def delete(pokemon_id):
        return Pokemon.collection.delete_one({"_id":pokemon_id})
    

