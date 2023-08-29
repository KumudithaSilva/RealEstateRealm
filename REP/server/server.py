from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/get_location_names')
def get_location_names():
    # Retrieve and return the list of locations
    response = jsonify({
        'locations': util.get_location_name()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
    try:
        # Extract input parameters from the POST request
        total_sqft = float(request.form['total_sqft'])
        location = request.form['location']
        bhk = int(request.form['bhk'])
        bath = float(request.form['bath'])

        # Get the estimated price
        estimated_price = "{:.2f}".format(util.get_estimated_price(location, total_sqft, bhk, bath))

        # Create a response with the estimated price
        response = jsonify({
            'estimated_price': estimated_price
        })
        response.headers.add('Access-Control-Allow-Origin', "*")

        return response
    
    except Exception as e:
    # Log the error
        print("Error", str(e))
        response = jsonify({
            'error': str(e)
        })
        return response


if __name__ == "__main__":
    print("Starting Python Flask Server For Real Estate Prediction")
    # Load the artifacts
    util.load_saved_artifacts()
    app.run()
