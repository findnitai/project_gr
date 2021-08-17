from model import Client
import motor.motor_asyncio


conn = 'mongodb+srv://nitai:Headtotoe%40123..@cluster0.ekp3r.mongodb.net'
client = motor.motor_asyncio.AsyncIOMotorClient(conn)
database = client.Clients
collection_login = database.client_login
collection = database.client_info

class MongoDatabase():
    async def find_one(query, collection):
        return await collection.find_one(query)

    async def insert_one(data, collection):
        new_insert = await collection.insert_one(data)
        return await collection.find_one({"_id": new_insert.inserted_id})

    async def update_one(query, update):
        updated_document = await collection.update_one(query, update)
        return await collection.find_one({"_id": updated_document.inserted_id})


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



async def update_client_record(query, employee_email,  update):
    '''
    Use this only to add employee to Client list, update will be a different API
    '''
    client_info =  await collection.find_one(query)
    if not client_info:
        return {"detail" : "Client does not exist!"}
    else:
        for employee in client_info["employees"]:
            if employee["email"] == employee_email:
                return{"detail" : "Employee Already Exists, please use update api"}
    try: 
        result = await collection.update_one(query, update)
        if result.matched_count > 0:
            response = {"detail" : "Employee Added"}
            return response
        else:
            return {"detail" : "Error, client exists but employee not updated"}
    except:
        return {"detail" : "Error, client exists but employee not updated"}

# async def update_employee_record(query, update):
#     #check if client exists
#     #check if employee exists
#     # if both yes, do the deed
#     pass