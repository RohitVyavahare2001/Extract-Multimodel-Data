# 📄 PDF Question & Solution Extractor

## 🚀 Problem Statement
Many educational PDFs contain math problems and solutions, but extracting them manually is time-consuming. The goal of this project is to **automatically extract questions, solutions, and images** from a given PDF and save them in a structured **JSON format**.

## 🛠️ Solution Approach
We use **Python and PyMuPDF (fitz)** to:
- 📖 Read the PDF file and extract text.
- 🔍 Identify sections labeled **"Example"** and **"Solution"** to separate questions and answers.
- 🖼️ Extract images from the PDF and save them as separate files.
- 📂 Store the extracted data (**text + images**) in a **JSON file** for easy access.

## 📂 Project Structure
│── extracted_images/ # Folder where extracted images are stored
│── static/ # (Optional) Folder for static files
│── answer.py # Main script to extract data
│── extracted_examples.json # Output JSON file with extracted data
│── pre_algebra_sample.pdf # Input PDF file
│── requirements.txt # Python dependencies


## 📌 How to Run

### 1️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 2️⃣ Run the Script
```bash
python answer.py
```
3️⃣ Output
✅ Extracted questions & solutions: extracted_examples.json
✅ Extracted images: Stored in extracted_images/


📜 Example JSON Output
```bash
[
    {
        "example_id": 1,
        "question_text": "Example: What is 5 + 3?",
        "question_images": ["extracted_images/example_1_0.png"],
        "solution_text": "Solution: The answer is 8.",
        "solution_images": ["extracted_images/example_1_0.png"]
    }
]
```

## 🎯 Key Features
✅ Automatically detects and extracts questions & solutions
✅ Saves images separately for better clarity
✅ Outputs structured JSON for further use


You can directly **copy-paste** this into your project. Let me know if you need any modifications! 🚀
