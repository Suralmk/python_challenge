from pymongo import MongoClient

client = MongoClient("localhost", 27017)
db = client["SMS"]
Students = db["Students"]
Users = db["User"]
Departments = db["Department"]

Students.insert_one({
    "name" : "Surafel Melaku",
    "department":"Software Engineering"
})