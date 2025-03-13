from flask import Flask, request, render_template, redirect
from docx import Document
import os
import shutil
import time
import logging
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['STATIC_FOLDER'] = 'static'
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'default_secret_key')


logging.basicConfig(level=logging.DEBUG)


if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

if not os.path.exists(app.config['STATIC_FOLDER']):
    os.makedirs(app.config['STATIC_FOLDER'])

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        
        if file and file.filename.endswith('.docx'):
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)

            new_name = request.form.get('name', '')
            updated_file_name = replace_footer(file_path, new_name)

            if updated_file_name:
                return render_template('result.html', updated_file=updated_file_name)
            else:
                return "Error: The file could not be processed. Please upload a valid .docx file."
    
    return render_template('index.html')

def replace_footer(file_path, new_name):
    try:
        doc = Document(file_path)
        
        for section in doc.sections:
            footer = section.footer
            for paragraph in footer.paragraphs:
                if paragraph.text.strip():
                    paragraph.text = new_name
        
       
        updated_file_name = os.path.basename(file_path).replace('.docx', '_updated.docx')
        updated_file_path = os.path.join(app.config['STATIC_FOLDER'], updated_file_name)
        doc.save(updated_file_path)
        
        return updated_file_name  
    except Exception as e:
        logging.error(f"Error processing file: {e}")
        return None

def cleanup_folders():
    current_time = time.time()
    for folder in [app.config['UPLOAD_FOLDER'], app.config['STATIC_FOLDER']]:
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    file_age = current_time - os.path.getmtime(file_path)
                    if file_age > 86400:  
                        os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print(f"Failed to delete {file_path}. Reason: {e}")

if __name__ == '__main__':
   
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)