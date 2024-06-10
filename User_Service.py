import hashlib
from datetime import datetime
import uvicorn
from fastapi import FastAPI, Request
from logger import add_logger

log = add_logger('myFastApiApp')

api_app = FastAPI()

@api_app.get("/generate_id")
def generate_id(request: Request):
    current_time = str(datetime.now()).encode()
    generated_id = hashlib.md5(current_time).hexdigest()
    log.info(f"{request.client.host}: Generated ID = {generated_id}")
    return {"generated_id": generated_id}

log.info("Launching FastAPI Application")
uvicorn.run(api_app)