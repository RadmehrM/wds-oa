# WDS-OA Project

This project consists of a Django backend and a Vue 3 frontend.

## Prerequisites

- Python 3.10+
- Node.js 18+
- npm (comes with Node.js)
- [pipenv](https://pipenv.pypa.io/en/latest/) or `venv` and `pip`
- Git

---

## Backend Setup (Django)

1. **Clone the repository**  
   ```sh
   git clone <your-repo-url>
   cd wds-oa/backend
   ```

2. **Create and activate a virtual environment**  
   Using `venv`:
   ```sh
   python -m venv venv
   venv\Scripts\activate
   ```
   Or using `pipenv`:
   ```sh
   pipenv shell
   ```

3. **Install dependencies**  
   ```sh
   pip install -r requirements.txt
   ```

4. **Apply migrations**  
   ```sh
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Start the backend server**  
   ```sh
   python manage.py runserver
   ```
   The backend will be available at [http://127.0.0.1:8000](http://127.0.0.1:8000).

---

## Frontend Setup (Vue 3)

1. **Open a new terminal and navigate to the frontend directory**  
   ```sh
   cd wds-oa/frontend
   ```

2. **Install dependencies**  
   ```sh
   npm install
   ```

3. **Start the frontend development server**  
   ```sh
   npm run dev
   ```
   The frontend will be available at [http://localhost:5173](http://localhost:5173).

---

## Additional Notes

- Make sure the backend server is running before using the frontend, as the frontend expects the API at `http://127.0.0.1:8000`.
- If you add new Python packages, update `requirements.txt` with `pip freeze > requirements.txt`.
- For any issues with CORS, ensure the backend `settings.py` has the correct `CORS_ALLOWED_ORIGINS`.

---

## Troubleshooting

- If you get a database error, ensure you have run all migrations.
- If you get a CORS error, check your backend CORS settings.
- If you get a "Failed saving to database" alert, make sure your backend server is running.

---
