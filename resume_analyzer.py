import PyPDF2
import json

def extract_text_from_pdf(uploaded_file):
    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text.lower()

def load_keywords(role):
    with open("roles.json", "r") as f:
        data = json.load(f)
    return data.get(role, [])

def analyze_resume(text, keywords):
    found = [kw for kw in keywords if kw in text]
    missing = [kw for kw in keywords if kw not in text]
    score = round((len(found) / len(keywords)) * 100, 2)
    return found, missing, score
