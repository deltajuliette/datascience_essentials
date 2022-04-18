from flask import Flask, request
import numpy as np
import os
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.models import load_model

app = Flask('myApp')

# Load in the model outside any route so that we load the model only once
# Loading the model takes time (especially deep learning models)
# So if you happen to load the model inside a route, it'll load every single time a request is received which is very inefficient
trf_model = load_model('cats_vs_dogs.h5')

# route 1: Return Success status
@app.route('/')
def home():
    # return a simple string
    return {"success": True}, 200

# route 2: accept input data
# Post method is used when we want to receive some data from the user
@app.route('/predict', methods = ['POST'])
def make_predictions():
    # Get the data sent over the API
    user_input = request.get_json(force=True)
    data = user_input['X']
    
    # Preprocess
    data = preprocess_input(np.array(data))

    # Make predictions
    result = trf_model.predict(data)

    # Convert the probability to actual predictions
    predictions = ['Dog' if pred[0]>0.5 else 'Cat' for pred in result]

    # return the results with our predictions
    return {'response': predictions}


if __name__ == '__main__':
    # Run the App!
    app.run(host='0.0.0.0', debug=True, port=int(os.environ.get("PORT", 8080)))