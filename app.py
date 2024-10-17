from flask import Flask, render_template, request, redirect, url_for, flash, send_file
import os
from PyPDF2 import PdfReader, PdfWriter
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['UNLOCKED_FOLDER'] = os.path.join('static', 'unlocked')
app.config['ALLOWED_EXTENSIONS'] = {'pdf'}
app.secret_key = '70113185'  # Change this to a random secret key

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part', 'error')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file', 'error')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            return redirect(url_for('enter_password', filename=filename))
        else:
            flash('Invalid file type. Please upload a PDF file.', 'error')
    return render_template('upload.html')

@app.route('/enter_password/<filename>', methods=['GET', 'POST'])
def enter_password(filename):
    if request.method == 'POST':
        password = request.form['password']
        input_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        output_filename = f"{os.path.splitext(filename)[0]}-unlocked.pdf"
        output_path = os.path.join(app.config['UNLOCKED_FOLDER'], output_filename)
        
        try:
            reader = PdfReader(input_path)
            if reader.is_encrypted:
                reader.decrypt(password)
            
            writer = PdfWriter()
            for page in reader.pages:
                writer.add_page(page)
            
            with open(output_path, 'wb') as output_file:
                writer.write(output_file)
            
            flash('PDF unlocked successfully!', 'success')
            return redirect(url_for('view_pdf', filename=output_filename))
        except Exception as e:
            flash(f'Error unlocking PDF: {str(e)}', 'error')
            return redirect(url_for('enter_password', filename=filename))
    
    return render_template('enter_password.html', filename=filename)

@app.route('/view/<filename>')
def view_pdf(filename):
    return render_template('view_pdf.html', filename=filename)

@app.route('/download/<filename>')
def download_pdf(filename):
    return send_file(os.path.join(app.config['UNLOCKED_FOLDER'], filename), as_attachment=True)

if __name__ == '__main__':
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    os.makedirs(app.config['UNLOCKED_FOLDER'], exist_ok=True)
    app.run(debug=True)