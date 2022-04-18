import requests
base_url = "http://127.0.0.1:5000/"

def pred_price(OverallQual, FullBath, GarageArea, LotArea):
    # Construct the input to our Flask API using a Python dictionary
    api_input = {
        "OverallQual": OverallQual,
        "FullBath": FullBath,
        "GarageArea": GarageArea,
        "LotArea": LotArea
    }
    
    # Post a request to our flask API's /predict route using the input we just created and store the result in "response"
    response = requests.post(url=f"{base_url}predict", json=api_input)
    
    # Convert the response to a dictionary 
    response = response.json()
    
    # Return only the Price value
    return response["response"]

def hello_world():
    # Get request to the base url route
    response = requests.get(url=f"{base_url}")
    
    # Convert the response to a dictionary 
    response = response.json()
    
    # Return only the Price value
    return response["response"]

def html_page():
    # Get request to the base url route
    response = requests.get(url=f"{base_url}hc_page")
    
    # Convert the response to a dictionary 
    response = response.json()
    
    # Return only the Price value
    return response["response"]