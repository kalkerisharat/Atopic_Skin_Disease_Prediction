from flask import Flask, request, render_template
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.vgg16 import preprocess_input
from tensorflow.keras.models import load_model
import numpy as np
import os

app = Flask(__name__)
model = load_model('atopic_dermatitis_model.h5')

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ""
    if request.method == 'POST':
        if 'file' not in request.files:
            return render_template('index.html', result="No file part")
        file = request.files['file']
        if file.filename == '':
            return render_template('index.html', result="No selected file")
        if file:
            img_path = os.path.join('static', file.filename)
            file.save(img_path)
            
            # Load and preprocess the image
            img = image.load_img(img_path, target_size=(150, 150))
            img_array = image.img_to_array(img)
            img_array = np.expand_dims(img_array, axis=0)
            img_array = preprocess_input(img_array)
            
            # Predict
            prediction = model.predict(img_array)
            result = "Atopic Dermatitis" if prediction[0][0] > 0.5 else "Not Atopic Dermatitis"
    
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
