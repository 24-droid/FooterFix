from flask import Flask,request,render_template,redirect,url_for
form docx import Document
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER']='uploads'
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])
@app.route('/', methods=['GET','POST'])
def index():
    if request.method=='POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file=request.files['file']
        if file.filename=='':
            return redirect(request.url)
        if file and file.filename.endswith('docx'):
            file_path=os.path.join(app.config['UPLOAD_FOLDER'],file.filename)
            file.save(file_path)
        new_name=request.form.get('name','')
        updated_file_path=replace_footer(file_path,new_name)
        return render_template('result.html',updated_file=updated_file_path)
    return render_template('index.html')

def replace_footer(file_path,new_name)
    doc=Document(file_path)
    for section in doc.sections:  
        footer=section.footer
        for paragraph in footer.paragraphs:
            if paragraph.text.strip():
                paragraph.text=new_name
    updated_file_path=file_path.replace('.docx','_updated.docx')
    doc.save(updated_file_path) 
    return updated_file_path

if __name__=='__main__':
    app.run(debug=True)                    
