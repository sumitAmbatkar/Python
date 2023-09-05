def get_data_from_mongo():
    import pymongo
    data = "mongodb+srv://sumitambatkar21:sumit111@cluster0.uu9dqdm.mongodb.net/?retryWrites=true&w=majority"

    client = pymongo.MongoClient(data)

    db = client["db1"]

    col = db["sample_table"]

    all_documents = col.find()

    for document in all_documents:
        print(document)
get_data_from_mongo()