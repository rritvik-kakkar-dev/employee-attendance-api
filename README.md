# Employee Attendance API

A full-stack Employee Attendance Application built with FastAPI (Backend) and React/Vite (Frontend).

## 🚀 Getting Started

Follow these instructions to set up and run the project locally.

### Prerequisites
*   **Python 3.10+**
*   **Node.js 18+** & **npm**

---

### 1. Backend Setup

1.  **Navigate to the project root:**
    ```bash
    cd /path/to/employee-attendance-api
    ```

2.  **Create and Activate Virtual Environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Server:**
    ```bash
    python -m uvicorn main:app --reload
    ```
    *   The backend will start at: `http://localhost:8000`
    *   API Documentation (Swagger): `http://localhost:8000/docs`

---

### 2. Frontend Setup

1.  **Open a new terminal** and navigate to the frontend folder:
    ```bash
    cd frontend
    ```

2.  **Install Node Modules:**
    ```bash
    npm install
    ```

3.  **Run the Development Server:**
    ```bash
    npm run dev
    ```
    *   The frontend will usually start at: `http://localhost:5173`

---

### 3. Usage Guide

1.  **Register/Login**:
    *   Open the frontend (`http://localhost:5173`).
    *   Register a new account or Login.
    *   Once logged in, you will be redirected to the Dashboard.

2.  **API Exploration**:
    *   Visit `http://localhost:8000/docs`.
    *   Click "Authorize" (Green Button).
    *   Paste your `access_token` (you can get this from the Network tab in your browser after logging in via frontend, or use the `/auth/login` endpoint directly in Swagger).
    *   Test the endpoints!
