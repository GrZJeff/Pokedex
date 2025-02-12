from app import mongo

class Users:
    collection = mongo.db.users

    @staticmethod
    def find_all():
        users = Users.collection.find()
        return list(users)
    
    @staticmethod
    def find_by_id(user_id):
        user = Users.collection.find_one({
            "_id": user_id
        })
        return user
    
    @staticmethod
    def create(data):
        user = Users.collection.insert_one(data)
        return user.inserted_id
    
    @staticmethod
    def update(user_id, data):
        user = Users.collection.update_one({
            "_id": user_id
        }, {
            "$set": data
        })
        return user
    
    @staticmethod
    def delete(user_id):
        return Users.collection.delete_one({"_id": user_id})
