import requests
import json

# Your Railway Cloud app URL
url = "https://web-production-a6fc.up.railway.app/predict"

# Create the JSON data
data = {
    "Pclass": 3,
    "Sex": 0,
    "Age": 22.0,
    "Fare": 7.25
}

# Convert the dictionary to a JSON string
json_data = json.dumps(data)

# Set the headers to indicate that you're sending JSON data
headers = {'Content-type': 'application/json'}

# Send the POST request
try:
    response = requests.post(url, data=json_data, headers=headers)

    # Check the response status code
    if response.status_code == 200:
        # Parse the JSON response
        prediction = response.json()
        print("Prediction:", prediction)
    else:
        print("Error:", response.status_code, response.text)  # Print the error message
except requests.exceptions.RequestException as e:
    print("Connection Error:", e)