# 1. Read the artifacts fils and access the json file and get the locations
import json
import pickle
import numpy as np
import warnings

warnings.filterwarnings("ignore", category=UserWarning)

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
    with open("./columns.json", 'r') as file:
        __data_columns = json.load(file)['data_columns']
        __location = __data_columns[3:]

    # Load the pickle file
    with open("./real_estate_best_model.pickle", 'rb') as file:
        __model = pickle.load(file)
    
    print("Successfull loaded the artifacts...")


if __name__ == "__main__":
    load_saved_artifacts()
    print(get_location_name())
    print(get_estimated_price("anjanapura", 1000, 3 , 3))
    print(get_estimated_price('1st Phase JP Nagar', 2000, 2 , 2))
