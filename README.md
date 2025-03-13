# Footer Fixer

## Description
Footer Fixer is a web application that allows users to upload a `.docx` file and replace or add a footer with their name. The app is built using **Flask** (a Python web framework) and **python-docx** (for working with `.docx` files). It’s designed to be simple, efficient, and user-friendly.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Live Link](#live-link)

## Installation
Follow these steps to set up the project locally:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/footer-fixer.git
2. **Navigate to the project directory**:
    ``bash
      cd footer-fixer
      Create a virtual environment (optional but recommended):
      python -m venv venv
      source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
      Install dependencies:
      pip install -r requirements.txt
      Run the app:
      python app.py
      Access the app:
3. **Open your browser and go to http://localhost:5000**.

## Usage
Upload a .docx File:
On the home page, click the "Choose File" button to upload a .docx file.
Enter Your Name:
Enter your name in the input field.
Replace or Add Footer:
Click the "Upload and Replace Footer" button. The app will process the file and replace or add a footer with your name.
Download the Updated File:
Once the file is processed, you’ll see a download link for the updated .docx file.

## Features
Upload .docx Files: Users can upload .docx files to the app.
Replace or Add Footers: The app replaces existing footers or adds a new footer with the user’s name.
Download Updated Files: Users can download the updated .docx file with the new footer.
Error Handling: The app gracefully handles corrupted or invalid files and notifies the user.

## Technologies Used
Flask: A lightweight Python web framework for building the app.
python-docx: A Python library for working with .docx files.
HTML/CSS: For the frontend design.
Git: For version control.

## Live Link
https://footerfix-4.onrender.com/

