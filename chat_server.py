# chat_server.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from pydantic import BaseModel

app = FastAPI()
messages = []

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Message(BaseModel):
    sender: str
    content: str

@app.post("/send")
def send_message(msg: Message):
    messages.append(msg)
    return {"status": "ok"}

@app.get("/messages", response_model=List[Message])
def get_messages():
    return messages
\
