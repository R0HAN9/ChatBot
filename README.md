# Chatbot Application (Next.js + FastAPI + MySQL)

A simple chatbot application that connects a **Next.js** frontend to a **FastAPI** backend with optional **MySQL** integration for storing chat history. This project demonstrates a production-ready architecture for building a full-stack application.

---

## Features

- **Frontend:** Built with Next.js and TypeScript, providing a responsive and interactive chatbot interface.
- **Backend:** Developed using FastAPI with support for both in-memory and MySQL database configurations.
- **Database:** MySQL integration for storing and retrieving chat history (optional).
- **CORS Enabled:** Seamless connection between frontend and backend.
- **Error Handling:** Graceful error messages and robust API handling.

---

## Tech Stack

- **Frontend:** 
  - Next.js (15.1.5)
  - TypeScript
  - Material-UI (MUI)

- **Backend:** 
  - FastAPI (Python 3.12)
  - MySQL (Optional)

- **Tools:**
  - Postman (for API testing)
  - Axios (HTTP client for Next.js)

---

## Project Structure

### Frontend (Next.js)
- **File:** `chatbot.tsx`
- Handles the user interface and communicates with the FastAPI backend.

### Backend (FastAPI)
- **File:** `main.py`
- Provides the API for sending and retrieving messages.

### Database (MySQL)
- **Table Schema:**
  ```sql
  CREATE TABLE messages (
      id INT AUTO_INCREMENT PRIMARY KEY,
      user_message TEXT NOT NULL,
      bot_response TEXT NOT NULL,
      timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
  );
