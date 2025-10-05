from flask import Flask, jsonify
from flask_cors import CORS

# Initialize the Flask app
app = Flask(__name__)
# CORS allows your frontend to request data from your backend
CORS(app)

# Our sample data from the prototype
sample_data = [
    {
        "location": "Los Angeles-North Main Street",
        "coordinates": { "latitude": 34.06659, "longitude": -118.23666 },
        "measurements": [ { "parameter": "pm25", "value": 12.5 } ]
    },
    {
        "location": "Pasadena-S. Wilson Ave",
        "coordinates": { "latitude": 34.1366, "longitude": -118.1227 },
        "measurements": [
            {
                "parameter": "pm25", "value": 38.9,
                "forecast": [38.9, 39.1, 39.5, 40.2, 41.0, 42.1, 42.5, 41.8, 41.0, 39.9, 38.5, 37.0, 36.0, 35.5, 35.8, 36.5, 37.5, 39.0, 40.5, 41.5, 42.0, 42.3, 42.1, 41.8]
            }
        ]
    },
    {
        "location": "Glendora-Laurel",
        "coordinates": { "latitude": 34.1363, "longitude": -117.8229 },
        "measurements": [ { "parameter": "pm25", "value": 45.1 } ]
    }
]

# Create an API "endpoint" that will serve our data
@app.route("/api/air-quality-data")
def get_air_quality_data():
    # jsonify converts our Python list of dictionaries into JSON format
    return jsonify(sample_data)

# This makes the server run when you execute the script
if __name__ == "__main__":
    app.run(debug=True)