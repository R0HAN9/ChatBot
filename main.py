# main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import mysql.connector

app = FastAPI()

# CORS configuration
origins = [
    "http://localhost:3000",  # Frontend URL
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)
 
# Pydantic model to handle incoming message data
class Message(BaseModel):
    user_message: str

# MySQL configuration (use in-memory for now)
use_mysql = False

# Simulating in-memory storage for the chat messages
chat_history = []

# Database connection function (for MySQL)
def get_db_connection():
    if use_mysql:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="password",  # Update with your MySQL password
            database="chatbot_db"
        )
        return conn
    else:
        return None

# Route to handle sending a message to the chatbot
@app.post("/send_message")
async def send_message(message: Message):
    user_message = message.user_message
    bot_response = f"Bot: {user_message[::-1]}"  # Simple bot response (echoes the user input in reverse)

    # Store chat history in MySQL or in-memory based on configuration
    if use_mysql:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO messages (user_message, bot_response) VALUES (%s, %s)", (user_message, bot_response))
        conn.commit()
        cursor.close()
        conn.close()
    else:
        chat_history.append({"user_message": user_message, "bot_response": bot_response})

    return {"response": bot_response}

# Route to retrieve chat history (for display purposes)
@app.get("/get_history")
async def get_history():
    if use_mysql:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT user_message, bot_response FROM messages")
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return {"history": result}
    else:
        return {"history": chat_history}














