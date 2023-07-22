import pymongo
client=pymongo.MongoClient("mongodb+srv://test:test@cluster0.orthvww.mongodb.net/?retryWrites=true&w=majority")
print("connection established",client)
database_name="Craftsvilla"
collection_name= "Search-log"
