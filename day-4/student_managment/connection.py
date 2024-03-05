from pymongo import MongoClient

client = MongoClient("localhost", 27017)
db = client["SMS"]
Grade = db["Grade"]
Users = db["User"]


# Users.insert_many([
#     {
#     "first_name" : "Kaleab",
#     "last_name" : "Alemu",
#     "username": "kal",
#     "password": "120",
#     "role":"stu",
# },
#     {
#     "first_name" : "Alazae",
#     "last_name" : "Dawit",
#     "username": "alwa",
#     "password": "120",
#     "role":"stf",
# }
# ]
    
# )