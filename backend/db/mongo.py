from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["codereviewer"]
code_collection = db["code"]
report_collection = db["reports"]