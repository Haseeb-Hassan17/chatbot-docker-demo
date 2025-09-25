import os
from dotenv import load_dotenv
load_dotenv()

import logging
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from chatbot import SimpleChatbot # Import SimpleChatbot from the root directory

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

app = FastAPI()

app.mount("/static", StaticFiles(directory="."), name="static")

templates = Jinja2Templates(directory=".")

chatbot = SimpleChatbot()

class ChatRequest(BaseModel):
    message: str

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    logger.info("Serving index.html") # Log when index.html is served
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/chat")
async def chat_endpoint(chat_request: ChatRequest):
    user_message = chat_request.message
    logger.info(f"Received message from frontend: {user_message}") # Log user message
    bot_response = chatbot.chat(user_message)
    logger.info(f"Sending response to frontend: {bot_response}") # Log bot response
    return {"response": bot_response}
