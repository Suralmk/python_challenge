from pymongo import MongoClient

client = MongoClient("localhost", 27017)
db = client["SMS"]
Students = db["Students"]
Users = db["User"]
Departments = db["Department"]

Users.insert_one({
    "first_name" : "Surafel",
    "last_name" : "Melaku",
    "username": "sura",
    "password": "120",
    "role":"stu",
})