import requests
import pandas as pd
import json

# Function to query the Cosmicflows API
def get_cosmicflows_data(alpha, delta, system='supergalactic', parameter='distance', value=20, calculator='NAM'):
    """
    Query the Cosmicflows API and retrieve distance and velocity data.
    
    Parameters:
    - alpha: (float) First coordinate (RA, Glon, SGL) in degrees
    - delta: (float) Second coordinate (Dec, Glat, SGB) in degrees
    - system: (str) Coordinate system ("equatorial", "galactic", or "supergalactic")
    - parameter: (str) Quantity ("distance" or "velocity")
    - value: (float) Value of the parameter (distance in Mpc or velocity in km/s)
    - calculator: (str) Cosmicflows calculator to use ("NAM" or "CF3")
    
    Returns:
    - dict: A dictionary containing distance, velocity, and coordinate data
    """
    API_url = f'http://edd.ifa.hawaii.edu/{calculator}calculator/api.php'
    query = {
        'coordinate': [float(alpha), float(delta)],
        'system': system,
        'parameter': parameter,
        'value': float(value)
    }
    headers = {'Content-type': 'application/json'}
    
    try:
        response = requests.get(API_url, data=json.dumps(query), headers=headers)
        response.raise_for_status()
        return response.json()  # returns data as a Python dictionary
    except Exception as e:
        print("Error:", e)
        return None

# Sample data to query (list of coordinates)
coordinates = [
    {'alpha': 192.25, 'delta': 27.4},   # Example coordinate 1
    {'alpha': 13.3, 'delta': -44.5},    # Example coordinate 2
    {'alpha': 75.3, 'delta': 60.7}      # Example coordinate 3
]

# Query data for each coordinate and store results
data = []
for coord in coordinates:
    result = get_cosmicflows_data(alpha=coord['alpha'], delta=coord['delta'])
    if result:
        data.append(result)

# Convert the data into a Pandas DataFrame
df = pd.DataFrame(data)
print(df)
