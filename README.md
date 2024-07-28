
# Atopic Dermatitis Skin Diseases Prediction using Machine Learning

This project aims to predict atopic dermatitis using a machine learning model. The project includes training a model with image data, deploying the model using a Flask web application, and providing a user-friendly interface for uploading images and getting predictions.

## Project Structure

```
Atopic_Dermatitis_Prediction/
├── dataset/
│   ├── train/
│   │   ├── atopic_dermatitis/
│   │   └── not_atopic_dermatitis/
│   ├── validation/
│   │   ├── atopic_dermatitis/
│   │   └── not_atopic_dermatitis/
│   ├── test/
│       ├── atopic_dermatitis/
│       └── not_atopic_dermatitis/
├── app.py
├── model.py
├── predict.py
├── requirements.txt
├── atopic_dermatitis_model.pkl
├── templates/
│   └── index.html
└── static/
    └── (uploaded files and static assets)
```

## Setup

### Prerequisites

Ensure you have Python 3.6+ installed. 

### Installation

1. Clone the repository:

```bash
git clone https://github.com/your_username/Atopic_Dermatitis_Prediction.git
cd Atopic_Dermatitis_Prediction
```

2. Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

3. Install the required packages:

```bash
pip install -r requirements.txt
```

### Dataset

Organize your dataset as follows:

```
dataset/
├── train/
│   ├── atopic_dermatitis/
│   └── not_atopic_dermatitis/
├── validation/
│   ├── atopic_dermatitis/
│   └── not_atopic_dermatitis/
├── test/
    ├── atopic_dermatitis/
    └── not_atopic_dermatitis/
```

### Training the Model

To train the model, run:

```bash
python model.py
```

### Running the Web Application

To start the Flask web application, run:

```bash
python app.py
```

Then open your browser and navigate to `http://127.0.0.1:5000/`.

### Predicting Images

Upload an image through the web interface, and the model will predict whether the image shows atopic dermatitis or not.

## Files

- **app.py**: Flask web application to serve the model and provide a user interface.
- **model.py**: Script to train the machine learning model.
- **predict.py**: Script to load the model and make predictions.
- **requirements.txt**: List of required Python packages.
- **templates/index.html**: HTML template for the web interface.
- **static/**: Directory for static files and uploaded images.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Special thanks to the contributors of TensorFlow and Keras for providing the tools necessary to create this project.

---
