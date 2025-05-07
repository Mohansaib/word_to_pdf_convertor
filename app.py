from flask import Flask, render_template, request, send_from_directory
from docx2pdf import convert
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "outputs"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['OUTPUT_FOLDER'] = OUTPUT_FOLDER

# Ensure folders exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert_file():
    if 'word_file' not in request.files:
        return "No file uploaded", 400

    word_file = request.files['word_file']
    if word_file.filename == '':
        return "No selected file", 400

    filename = secure_filename(word_file.filename)
    input_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    word_file.save(input_path)

    # Convert to PDF
    output_filename = filename.rsplit('.', 1)[0] + ".pdf"
    output_path = os.path.join(app.config['OUTPUT_FOLDER'], output_filename)

    convert(input_path, output_path)

    return send_from_directory(app.config['OUTPUT_FOLDER'], output_filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
