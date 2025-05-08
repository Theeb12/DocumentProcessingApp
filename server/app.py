from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import psycopg2

app = Flask(__name__)
CORS(app)

# Connect to PostgreSQL database
conn = psycopg2.connect(
    dbname="document_processing", user="postgres", password="Mollyman1", host="localhost"
)
cursor = conn.cursor()

EXTRACTION_API = "https://plankton-app-qajlk.ondigitalocean.app/extraction_api"
MATCHING_API = "https://endeavor-interview-api-gzwki.ondigitalocean.app/match/batch"

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["file"]
    # Send file to extraction API
    #files = {'file': uploaded_file}
    files = {
        'file': (file.filename, file.stream, 'application/pdf')
    }

    # Send the POST request to the extraction API
    headers = {
        'accept': 'application/json',  # Expecting JSON response from the extraction API
    }
    response = requests.post(EXTRACTION_API, files=files, headers=headers)
    extracted_data = response.json()
    #print("Extracted data:", extracted_data)

    # Send extracted data to matching API
    request_items = []
    for item in extracted_data:
        request_items.append(item['Request Item'])

    payload = {
        "queries": request_items
    }
    #print("Request items: ", request_items)

    headers = {'accept': 'application/json', 'Content-Type': 'application/json'}
    response = requests.post(MATCHING_API, json=payload, headers=headers)
    matched_data = response.json()
    #print("Matched data:", matched_data)

    final_items = list(matched_data['results'].keys())

    # Save matched data to the database
    for item in final_items:
        cursor.execute(
            "INSERT INTO matched_items (item_name, amount) VALUES (%s, %s)",
            (item, 0)
        )
    conn.commit()
    print(final_items)
    return final_items

@app.route("/get_matches", methods=["GET"])
def get_matches():
    cursor.execute("SELECT * FROM matched_items WHERE confirmed=False")
    rows = cursor.fetchall()
    matches = [{"item_name": row[1], "amount": row[2]} for row in rows]
    return jsonify(matches)

if __name__ == "__main__":
    app.run(debug=True)
