NER Resume Parsing Project – Complete Documentation
1. Project Overview

This project is an AI-based Resume Information Extraction System built using Named Entity Recognition (NER) and rule-based post-processing. The system automatically extracts key details from resumes such as Name, Email, Phone Number, Skills, Education, and Experience, and displays them through a User Interface (UI).

The goal of the project is to reduce manual resume screening effort and demonstrate end-to-end NLP + UI integration.

2. Objectives

Automatically extract candidate information from resume text

Use an NER model for intelligent entity detection

Apply custom logic to clean and refine extracted data

Build a simple UI to upload resumes and display results

Provide an end-to-end working AI application

3. Tech Stack Used
3.1 Programming Language

Python 

3.2 Libraries & Frameworks

spaCy (for NER)

re (Regular Expressions)

Flask (Backend API)

HTML, CSS(Frontend UI)

PyPDF2 / pdfplumber 


4. System Architecture

Flow:

User uploads resume via UI

Resume file is sent to Flask backend

Text is extracted from resume (PDF/DOCX)

Text is passed to NER model

Entities are extracted and cleaned

Final data is displayed on UI

5. Resume Text Extraction
5.1 Supported Formats
Multiples types

5.2 PDF Extraction Logic

Extract text page by page

Combine into a single string

5.3 DOCX Extraction Logic

Read all paragraphs

Merge into clean text

6. NER Model Implementation
6.1 Model Description

Custom-trained / Pre-trained spaCy NER model

Identifies entities like:

NAME, EMAIL, PHONE, SKILLS, EDUCATION, EXPERIENCE

6.2 NER Processing Flow

Raw resume text → spaCy NLP pipeline

Entity detection using trained model

Store extracted entities in structured format

7. Name Extraction Logic
Problem

NER sometimes extracts noisy values like:

NAME: David Kim 91
Solution

Custom regex-based cleaning function applied after NER.

Final Logic

Remove prefixes like NAME:

Remove numbers (age, IDs)

Allow only alphabetic words

This ensures accurate name extraction.

8. Other Entity Extraction Rules
8.1 Email Extraction

Regex-based detection

Validates standard email patterns

8.2 Phone Number Extraction

Supports 10-digit and country-code formats

Removes unwanted symbols

8.3 Skills Extraction

Matches against predefined skill list

Removes duplicates

9. Frontend UI Design
9.1 UI Features

Resume upload button

Clean and simple interface

Result display section

9.2 UI Technologies

HTML for structure

CSS for styling

9.3 Displayed Output

Name, Email, Phone, Skills, Education, Experience


10. Output Example

Input: Resume PDF

Output:

Name: David Kim

Email: david.kim@email.com

Phone: 9876543210

Skills: Python, SQL, Machine Learning


11. Conclusion

This project demonstrates a complete AI-powered resume parsing system, combining:

NLP (NER)

Regex-based data cleaning

Backend API development

Frontend UI integration

It is suitable for:

Academic projects

Internships

AI/ML portfolio showcase

12. Future Enhancements

Add database storage

Improve NER accuracy

Multi-language resume support

Role-based candidate filtering

Admin dashboard
