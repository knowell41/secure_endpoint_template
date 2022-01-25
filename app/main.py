from fastapi_simple_security import api_key_router, api_key_security
from fastapi import Depends, FastAPI
from pydantic import BaseModel


####### 

app = FastAPI()

app.include_router(api_key_router, prefix="/auth", tags=["_auth"])

@app.get("/secure", dependencies=[Depends(api_key_security)])
async def secure_endpoint():
    return {"message": "This is a secure endpoint"} 
