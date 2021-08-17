from typing import Hashable
from fastapi import FastAPI, HTTPException, Body, status, Depends
from fastapi.middleware.cors import CORSMiddleware
from model import Client, ClientLogin, Employee
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.security import OAuth2PasswordRequestForm
from db import create_client_login, add_client_details, fetch_client_login, fetch_client_info, update_client_record
from hash import Hash
from auth import create_access_token


app = FastAPI()


origins = ['http://localhost:3000']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def check_status():
    return {"Message": "Server is up"}


@app.post('/api/register/')
async def create_client(request:ClientLogin):
    hashed_pass = Hash.bcrypt(request.password)
    client_object = jsonable_encoder(request)
    client_object["password"] = hashed_pass
    response = await create_client_login(client_object)
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=response)


@app.post('/api/login/v2/')
async def login_client(request:OAuth2PasswordRequestForm = Depends()):
    client = await fetch_client_login(request.username)
    print(client)
    if not client:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f'No user found with this {request.username} username')
    if not Hash.verify(client["password"] , request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail = f'Wrong Username or password')
    access_token = create_access_token(data={"sub": client["email"] })
    return {"access_token": access_token, "token_type": "bearer"}


@app.post("/api/login/", response_description="Add new client", response_model=ClientLogin)
async def client_login(client: ClientLogin = Body(...)):
    client = jsonable_encoder(client)
    response = await create_client_login(client)
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=response)


@app.get("/api/login/get_client_info", response_description="Get Client Login Information")
async def get_client(email: str):
    response = await fetch_client_login(email)
    if response:
        return {"detail": "Client Exists"}
    raise HTTPException(404, "Client with entered email not found")


@app.post("/api/client/", response_model=Client)
async def post_client_info(data: Client = Body(...)):
    data = jsonable_encoder(data)
    response = await add_client_details(data)
    if response:
        return response
    raise HTTPException(400, "Bad Request")


@app.get("/api/client", response_model=Client)
async def get_client_info(email: str):
    response = await fetch_client_info(email)
    if response:
        return response
    raise HTTPException(404, "There is no client with this id")


@app.post("/api/add_employee/")
async def add_employee_to_client(client_email : str, data : Employee = Body(...)):
    data = jsonable_encoder(data)
    query = {"email" : client_email}
    employee_email = data["email"]
    update = {"$push":{"employees" : data}}
    response = await update_client_record(query, employee_email, update)
    if response:
        return response
    raise HTTPException(400, "Bad request for adding employee to employer")


@app.post("api/update_employee_details/")
async def update_employee_details(client_email:str, employee_email:str, data: Employee = Body(...)):
    return {"detail" : "Under Construction"}

