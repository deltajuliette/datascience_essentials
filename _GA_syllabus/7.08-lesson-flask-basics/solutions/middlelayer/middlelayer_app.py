import pickle
import pandas as pd
from flask import Flask, request

app = Flask('myApp')

# Load in pickled model outside any route so that we load the model only once
# Loading the model takes time (especially deep learning models)
# So if you happen to load the model inside a route, it'll load every single time a request is received
# This is very inefficient
model = pickle.load(open('model.p', 'rb'))

# route 1: hello world
@app.route('/') #decorator
def home():
    # return a simple string
    return {"response": "Hello, world!"}

# route 2: return a 'web page'
@app.route('/hc_page')
def hc_page():
    # return some hard-coded html
    return {"response": "<html><body><h1>This is a hard coded page!</h1><p>Here is some hard-coded content. Isn\'t it pretty?</p></body></html>"}

# route 3: accept the form submission and do something fancy with it
# Post method is used when we want to receive some data from the frontend
@app.route('/predict', methods = ['POST'])
def make_predictions():
    # Get the data sent from the frontend
    user_input = request.get_json(force=True)
    
    # manipulate data into a format that we pass to our model
    data = pd.DataFrame(user_input, index=[0])
    
    # Our model was trained with columns [OverallQual, FullBath, GarageArea, LotArea]
    # Thus from our frontend we need to ensure the data follows the same columns and same order
    # And in the API, we need to ensure our columns are in the order the model expects!
    data = data[['OverallQual', 'FullBath', 'GarageArea', 'LotArea']]
    print(data)

    # make predictions
    prediction = model.predict(data.values)[0]

    # return the results template with our prediction value filled in
    return {"response": int(prediction)}


if __name__ == '__main__':
    # Run the App!
    app.run(debug=True)