import os
import numpy as np

from flask import Flask, request, render_template

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

# Flask App
app = Flask(__name__)

# Load Model
model = load_model('ECG.h5')

# Upload Folder
UPLOAD_FOLDER = 'uploads'

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# ---------------------------------------
# HOME PAGE
# ---------------------------------------

@app.route("/")
@app.route("/about")
def about():
    return render_template("about.html")


# ---------------------------------------
# INFO PAGE
# ---------------------------------------

@app.route("/info")
def information():
    return render_template("info.html")


# ---------------------------------------
# UPLOAD PAGE
# ---------------------------------------

@app.route("/upload")
def upload_page():
    return render_template("index6.html")


# ---------------------------------------
# PREDICTION ROUTE
# ---------------------------------------

@app.route("/predict", methods=["POST"])
def predict():

    try:

        # Check if file exists
        if 'file' not in request.files:
            return "No file uploaded"

        file = request.files['file']

        if file.filename == '':
            return "No selected file"

        # Save uploaded file
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)

        file.save(filepath)

        # Load image
        img = image.load_img(filepath, target_size=(64, 64))

        # Convert image to array
        x = image.img_to_array(img)

        # Normalize image
        x = x / 255.0

        # Expand dimensions
        x = np.expand_dims(x, axis=0)

        # Prediction
        pred = model.predict(x)

        y_pred = np.argmax(pred)

        print("Prediction:", y_pred)

        # Labels
        index = [
            'Left Bundle Branch Block',
            'Normal',
            'Premature Atrial Contraction',
            'Premature Ventricular Contractions',
            'Right Bundle Branch Block',
            'Ventricular Fibrillation'
        ]

        result = index[y_pred]

        return result

    except Exception as e:

        print("Error:", e)

        return "Prediction Failed"


# ---------------------------------------
# RUN APP
# ---------------------------------------

if __name__ == "__main__":

    app.run(debug=True)