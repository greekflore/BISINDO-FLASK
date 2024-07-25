from flask import Flask, request, render_template, redirect, url_for
from PIL import Image
import os
from werkzeug.utils import secure_filename
from model import model, predict, class_names

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads/'

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'png', 'jpg', 'jpeg', 'gif'}

@app.route('/', methods=['GET'])
def landing_page():
    return render_template('landing.html')

@app.route('/predict', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            # Load and preprocess the image
            image = Image.open(filepath)
            predicted_class, confidence = predict(image)

            return render_template('result.html', class_name=predicted_class, confidence=confidence, filename=filename)
    return render_template('index.html')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return redirect(url_for('static', filename='uploads/' + filename), code=301)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
