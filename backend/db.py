from model import Client
import motor.motor_asyncio


conn = 'mongodb+srv://nitai:Headtotoe%40123..@cluster0.ekp3r.mongodb.net'
client = motor.motor_asyncio.AsyncIOMotorClient(conn)
database = client.Clients
collection_login = database.client_login
collection = database.client_info


async def fetch_client_login(client_email):
    document = await collection_login.find_one({"email": client_email})
    return document


async def create_client_login(data):
    document = data
    new_client = await collection_login.insert_one(document)
    created_client = await collection_login.find_one({"_id": new_client.inserted_id})
    return created_client


async def add_client_details(data):
    document = data
    new_client_details = await collection.insert_one(document)
    created_client_details = await collection.find_one({"_id": new_client_details.inserted_id})
    return created_client_details


async def fetch_client_info(client_email):
    document = await collection.find_one({"email": client_email})
    return document
