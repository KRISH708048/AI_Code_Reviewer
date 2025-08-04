import os
from pymongo import MongoClient
from dotenv import load_dotenv
from urllib.parse import quote_plus

load_dotenv()
username = quote_plus(os.getenv("DB_USERNAME")) 
password = quote_plus(os.getenv("DB_PASSWORD")) 
MONGO_URL = f"mongodb+srv://{username}:{password}@cluster0.qvw4wd0.mongodb.net/AI_Code_Reviewer"

client = MongoClient(MONGO_URL)
database = client.get_database("ai_code_reviewer_db") 

# Collections
user_collection = database.get_collection("users")
history_collection = database.get_collection("analysis_history")