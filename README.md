Document Processing App

This application processes documents by extracting data from PDFs, matches extracted items with a predefined set, and stores the results in a PostgreSQL database. It consists of two main parts: a Flask backend and a React (TypeScript) frontend.

Features
- Upload PDF files: Users can upload a PDF document, which is processed to extract item data.
- API Integration: Data is extracted via an external API, and item matches are found through another external API.
- Database Storage: The matched items are stored in a PostgreSQL database.
- Manual Adjusting: Users can manually input or remove items from the database using the PSQL shell
- View Matches: After uploading the document, users can view the matched items on the frontend.

Technologies Used
- Frontend: React with TypeScript
- Backend: Flask (Python)
- Database: PostgreSQL
- APIs: External extraction and matching APIs
- CORS: Flask-CORS for handling cross-origin requests

Prerequisites
Before running this application, ensure the following are installed:

1. Node.js (for React app)
2. Python 3.x (for Flask backend)
3. PostgreSQL (database)

Backend Setup (Flask)
1. Clone the repository.
2. Install Python dependencies:
   pip install -r requirements.txt
3. Set up the PostgreSQL database:
   - Ensure PostgreSQL is installed and running.
   - Create a database named document_processing:
     CREATE DATABASE document_processing;
   - Create a table for storing matched items:
     CREATE TABLE matched_items (
       id SERIAL PRIMARY KEY,
       item_name VARCHAR(255),
       amount INTEGER DEFAULT 0,
       confirmed BOOLEAN DEFAULT FALSE
     );
   - Replace the database connection credentials in app.py (Flask backend) with your PostgreSQL credentials.
4. Start the Flask server:
   python app.py
   The backend will be running on http://localhost:5000.

Frontend Setup (React with TypeScript)
1. Clone the repository.
2. Install Node.js dependencies:
   npm install
3. Set up TypeScript:
   - If the project isn't already configured with TypeScript, run:
     npm install --save typescript @types/react @types/react-dom @types/jest
   - Rename the files in the src directory from .js to .tsx.
4. Start the React development server:
   npm run dev
   The frontend will be running on http://localhost:5173.

How to Use
1. Upload a Document:
   - Navigate to http://localhost:3000 in your browser.
   - Use the file input to upload a PDF document.
   - Click the Upload button to send the file to the backend for processing.

2. View Matches:
   - After the document is processed, the frontend will display a list of matched items from the backend.
   - Each item is shown with its name.
