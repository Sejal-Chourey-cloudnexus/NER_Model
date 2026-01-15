import os
import re
import pdfplumber
import pandas as pd


# 1 Helper Extraction Functions

def extract_email(text):
    match = re.search(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-z]{2,}", text)
    return match.group(0) if match else ""

def extract_phone(text):
    match = re.search(r"\+?\d[\d\s\-]{8,15}", text)
    return match.group(0) if match else ""

def extract_name(text):
    lines = text.split("\n")
    first_line = lines[0].strip()

    first_line = re.sub(r'^(name[:\-]?\s*)', '', first_line, flags=re.IGNORECASE)
    first_line = re.sub(r'\d+', '', first_line).strip()

    words = re.findall(r'[A-Za-z]+', first_line)
    if 1 <= len(words) <= 4:
        return " ".join(words)

    return ""

SKILLS = ["python", "java", "sql", "excel", "flask", "django", "ml", "ai", "data analysis"]

def extract_skills(text):
    text_lower = text.lower()
    found = [skill for skill in SKILLS if skill in text_lower]
    return ", ".join(found)

def extract_cgpa(text):
    match = re.search(r"CGPA[:\s-]*([\d\.]+)", text, re.IGNORECASE)
    return match.group(1) if match else ""

# 2 Main NER Function

def process_resume(pdf_path):
    text = ""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
    except Exception as e:
        print("Error reading PDF:", e)
        return {}

    data = {
        "name": extract_name(text),
        "email": extract_email(text),
        "phone": extract_phone(text),
        "skills": extract_skills(text),
        "cgpa": extract_cgpa(text),
        "text": text
    }

    return data
