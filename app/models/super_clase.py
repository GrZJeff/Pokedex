from app import mongo

class SuperClass:
    def __init__(self,collection):
        self.collection = mongo.db[collection] 


   
    def find_all(self):
        data = self.collection.find()
        return list(data)
    

    def find_by_id(self,object_id):
        datum = self.collection.find_one({
            "_id": object_id
        })
        return datum
    
    def create(self,data):
        datum = self.collection.insert_one(data)
        return datum.inserted_id
    
    
    def update(self,object_id, data):
        datum = self.collection.update_one({
            "_id":object_id
        },{
            "$set":data
        })
        return datum
    
    
    def delete(self,object_id):
        return self.collection.delete_one({"_id":object_id})
    

