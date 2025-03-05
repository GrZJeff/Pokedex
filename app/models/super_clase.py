from app import mongo

class SuperClass:
    def _init_(self,collection):
        self.collection = mongo.db[collection] 


   
    def find_all(self):
        data = list(self.collection.find())
        for datum in data:
            datum["_id"] = str(datum["_id"])
        return list(data)
    

    def find_by_id(self,object_id):
        datum = self.collection.find_one({
            "_id": object_id
        })
        if datum:
            datum["_id"] = str(datum["_id"])
        return datum
    
    def create(self,data):
        datum = self.collection.insert_one(data)
        return str(datum.inserted_id)
    
    
    def update(self,object_id, data):
        self.collection.update_one({
            "_id":object_id
        },{
            "$set":data
        })
        datum = self.collection.find_one({"_id":object_id})
        if datum:
            datum["_id"] = str(datum["_id"])
        return datum
    
    
    def delete(self,object_id):
        return self.collection.delete_one({"_id":object_id})
