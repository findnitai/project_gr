from fastapi import FastAPI, HTTPException, Body, status
from fastapi.middleware.cors import CORSMiddleware
from model import Client, ClientLogin
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from db import create_client_login, add_client_details, fetch_client_login, fetch_client_info

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