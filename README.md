# 🫀 Classification of Arrhythmia using Deep Learning with 2D ECG Spectral Image Representation

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Flask](https://img.shields.io/badge/Flask-Web%20App-lightgrey.svg)
![TensorFlow](https://img.shields.io/badge/TensorFlow-CNN-orange.svg)
![Keras](https://img.shields.io/badge/Keras-Deep%20Learning-red.svg)

## 📌 Project Overview

This project builds an **ECG Arrhythmia Classification** system using a **Convolutional Neural Network (CNN)**. It classifies ECG images into **6 categories** of arrhythmia and deploys the model as a **Flask web application** where users can upload an ECG image and get an instant prediction.

> **Team ID:** LTVIP2023TMID04419  
> **Guided by:** SmartInternz

### 👥 Team Members
- Pilli Dileep Reddy
- Chamantula Pradeepkumar
- Bandi Saikumar
- Ketharajupalli Praveenkumar
- Muppidi Dhanush

---

## 🔬 Arrhythmia Classes

The model classifies ECG images into the following **6 classes**:

| # | Class |
|---|-------|
| 1 | Left Bundle Branch Block (LBBB) |
| 2 | Normal |
| 3 | Premature Atrial Contraction (PAC) |
| 4 | Premature Ventricular Contractions (PVC) |
| 5 | Right Bundle Branch Block (RBBB) |
| 6 | Ventricular Fibrillation (VF) |

---

## 🗂️ Project Structure

```
Classification Of Arrhythmia/
│
├── Dataset/
│   ├── Train/
│   │   ├── Left Bundle Branch Block/
│   │   ├── Normal/
│   │   ├── Premature Atrial Contraction/
│   │   ├── Premature Ventricular Contractions/
│   │   ├── Right Bundle Branch Block/
│   │   └── Ventricular Fibrillation/
│   └── Test/
│       └── (same structure as Train)
│
└── Flask/
    ├── static/
    │   ├── css/
    │   │   └── main.css
    │   ├── js/
    │   │   └── main.js
    │   ├── lbbb.png
    │   ├── normal.png
    │   ├── pac.png
    │   ├── pvc.png
    │   ├── rbbb.png
    │   └── vf.png
    ├── templates/
    │   ├── about.html
    │   ├── base.html
    │   ├── index6.html
    │   └── info.html
    ├── uploads/
    ├── app.py
    ├── ECG arrhythmia classification.ipynb
    ├── ECG Flask.ipynb
    └── ECG.h5
```

---

## ⚙️ Prerequisites

Make sure you have the following installed on your system:

- Python 3.x
- pip (Python package manager)
- Anaconda Navigator (recommended)

---

## 🛠️ Installation & Setup

### Step 1 — Clone the Repository

```bash
git clone https://github.com/Dileep0509/Classification-of-Arrhythmia-by-Using-Deep-Learning-with-2-D-ECG-Spectral-Image-Representation.git
cd Classification-of-Arrhythmia-by-Using-Deep-Learning-with-2-D-ECG-Spectral-Image-Representation
```

### Step 2 — Install Required Libraries

```bash
pip install tensorflow keras flask numpy pillow
```

### Step 3 — Download the Trained Model

> ⚠️ The `ECG.h5` model file is large (66MB) and is **not included** in this repository due to GitHub's file size limits.

You can either:
- **Train the model yourself** using the `ECG arrhythmia classification.ipynb` notebook
- **Download the model** from the link below and place it inside the `Flask/` folder as `ECG.h5`

---

## 🚀 How to Run the Project Locally

### Step 1 — Navigate to the Flask folder

```bash
cd Flask
```

### Step 2 — Run the Flask App

```bash
python app.py
```

### Step 3 — Open in Browser

Once the server starts, you will see:

```
* Running on http://127.0.0.1:5000
```

Open your browser and go to:
```
http://127.0.0.1:5000
```

---

## 🌐 Web App Pages

| Page | URL | Description |
|------|-----|-------------|
| Home | `/about` | Project overview and information about Arrhythmia |
| Info | `/info` | Details about each type of Arrhythmia with ECG images |
| Predict | `/upload` | Upload an ECG image to get a prediction |

---

## 🧠 How to Train the Model (Optional)

If you want to train the model from scratch:

1. Open `ECG arrhythmia classification.ipynb` in **Jupyter Notebook** or **Google Colab**
2. Upload the dataset to Google Drive or your local machine
3. Run all cells step by step:
   - Data Preprocessing (ImageDataGenerator)
   - Model Building (CNN layers)
   - Model Training (25 epochs)
   - Save the model as `ECG.h5`
4. Place the saved `ECG.h5` file inside the `Flask/` folder

---

## 🧪 Model Architecture

The CNN model uses the following layers in sequential order:

1. **Convolutional Layer 2D** — Feature extraction using sliding filters
2. **MaxPooling Layer** — Reduces feature map dimensions
3. **Flatten Layer** — Converts 2D features to 1D
4. **Dense Hidden Layers** — 200 and 300 units with ReLU activation
5. **Dropout Layer** — Prevents overfitting
6. **Output Layer** — 6 units with Softmax activation

```python
model = Sequential()
model.add(Conv2D(32, (3,3), input_shape=(64,64,3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Flatten())
model.add(Dense(units=200, activation='relu'))
model.add(Dense(units=300, activation='relu'))
model.add(Dense(units=6, activation='softmax'))
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
```

---

## 📊 Model Performance

| Metric | Value |
|--------|-------|
| Training Accuracy | ~99.5% |
| Validation Accuracy | ~85% |
| Total Epochs | 25 |
| Input Image Size | 64 x 64 |

---

## ✅ Advantages

- Predicts Arrhythmia with a high accuracy of nearly **96%**
- Early detection enables better understanding of disease causes
- Supports therapeutic interventions and treatment planning

## ⚠️ Limitations

- Not useful for identifying **different stages** of Arrhythmia
- Not useful for monitoring motor symptoms

---

## 🔮 Future Scope

- Apply **optimization techniques** to further improve model performance
- Extend classification to detect **different severity stages** of Arrhythmia
- Deploy the application to a **cloud platform** for public access

---

## 🔗 Project Links

- 🐙 **GitHub:** [Classification of Arrhythmia Repository](https://github.com/Dileep0509/Classification-of-Arrhythmia-by-Using-Deep-Learning-with-2-D-ECG-Spectral-Image-Representation)
- 🎥 **Demo Video:** [YouTube Demo](https://youtu.be/u8bpsNchyxQ)

---

## 📚 References

- [Convolutional Neural Networks - Analytics Vidhya](https://www.analyticsvidhya.com/blog/2021/05/convolutional-neural-networks-cnn/)
- [MathWorks - Convolution 2D Layer](https://www.mathworks.com/help/deeplearning/ref/nnet.cnn.layer.convolution2dlayer.html)
- [SmartInternz - Artificial Intelligence](https://smartinternz.com/externship_dyn/1/artificial-intelligence)

---

## 📄 License

This project was developed as part of the **SmartInternz Guided Project** program.

---

<p align="center">Made with ❤️ by Team LTVIP2023TMID04419</p>
