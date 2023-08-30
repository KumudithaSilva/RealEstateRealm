# 1. Read the artifacts fils and access the json file and get the locations
import json
import pickle
import numpy as np
import warnings
import os

warnings.filterwarnings("ignore", category=UserWarning)

# Get the absolute path of the server directory
artifacts_directory = os.path.dirname(os.path.abspath(__file__))

# Construct the absolute path to files
location_file_path = os.path.join(artifacts_directory, "artifacts", "columns.json")
model_file_path = os.path.join(artifacts_directory, "artifacts", "real_estate_model.pickle")

# Variables to hold loaded data
__location = None
__data_columns = None
__model = None

# Get the estimated price using the trained model
def get_estimated_price(location, sqft, bhk, bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk

    if loc_index >= 0:
        x[loc_index] = 1
    
    return round(__model.predict(x.reshape(1, -1))[0], 2)


# Get the list of locations
def get_location_name():
    return __location

# Load artifacts files
def load_saved_artifacts():
    print("Loading saved artifacts...start")
    global __data_columns
    global __location
    global __model

    # Read the JSON file
    with open(location_file_path, 'r') as file:
        __data_columns = json.load(file)['data_columns']
        __location = [column.title() for column in __data_columns[3:]]

    # Load the pickle file
    with open(model_file_path, 'rb') as file:
        __model = pickle.load(file)
    
    print("Successfull loaded the artifacts...")


if __name__ == "__main__":
    load_saved_artifacts()
    print(get_location_name())
    print(get_estimated_price("anjanapura", 1000, 3 , 3))
    print(get_estimated_price('1st Phase JP Nagar', 2000, 2 , 2))
