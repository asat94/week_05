from flask import Flask, request, jsonify
import pickle
import numpy as np

# Load the trained model from the pickle file
with open('titanic_model.pkl', 'rb') as f:
    model = pickle.load(f)

app = Flask(__name__)


# Home route for the web app
@app.route('/')
def home():
    return "Welcome to the Titanic Survival Prediction API!"


# API route to make predictions
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()  # Get data from the POST request

    # Extract features from the JSON data
    features = np.array([[data['Pclass'], data['Age'], data['Sex'], data['Fare']]])

    # Make the prediction
    prediction = model.predict(features)

    # Return the prediction result
    survival = "Survived" if prediction[0] == 1 else "Not Survived"
    return jsonify({"prediction": survival})


if __name__ == "__main__":
    app.run(debug=True)
