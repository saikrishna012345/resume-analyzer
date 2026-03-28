from flask import Flask, request, jsonify
from flask_cors import CORS
import PyPDF2

app = Flask(__name__)
CORS(app)

def extract_text(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        content = page.extract_text()
        if content:
            text += content
    return text

@app.route("/")
def home():
    return "Backend is running!"

@app.route("/test", methods=["POST"])
def test_pdf():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"})

    file = request.files["file"]
    text = extract_text(file)

    return jsonify({
        "message": "PDF processed successfully",
        "preview": text[:500]
    })

if __name__ == "__main__":
    app.run(debug=True)