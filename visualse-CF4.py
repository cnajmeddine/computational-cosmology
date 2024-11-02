import requests
import pandas as pd
import json
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Function to get Cosmicflows data
def get_cosmicflows_data(alpha, delta, system='supergalactic', parameter='distance', value=20, calculator='NAM'):
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
        return response.json()
    except Exception as e:
        print("Error:", e)
        return None

# Sample coordinates (generate or modify as needed for around 100 samples)
coordinates = [
    {'alpha': np.random.uniform(0, 360), 'delta': np.random.uniform(-90, 90)} 
    for _ in range(100)
]

# Collect data
data = []
for coord in coordinates:
    result = get_cosmicflows_data(alpha=coord['alpha'], delta=coord['delta'])
    if result:
        data.append(result)

# Create DataFrame
df = pd.DataFrame(data)

# Parse peculiar velocity components if available
df[['SG_Vx', 'SG_Vy', 'SG_Vz']] = df['peculiar_velocity'].apply(lambda x: pd.Series(x) if isinstance(x, dict) else pd.Series([None, None, None]))

# Visualization
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Plot galaxy positions
ax.scatter(df['RA'], df['Dec'], df['velocity'], color='b', label='Galaxies')

# Plot velocity vectors if available
for i in range(len(df)):
    if pd.notnull(df.at[i, 'SG_Vx']):
        ax.quiver(
            df.at[i, 'RA'], df.at[i, 'Dec'], df.at[i, 'velocity'], 
            df.at[i, 'SG_Vx'], df.at[i, 'SG_Vy'], df.at[i, 'SG_Vz'], color='r', length=1000, normalize=True
        )

# Labeling the plot
ax.set_xlabel('RA (deg)')
ax.set_ylabel('Dec (deg)')
ax.set_zlabel('Velocity (km/s)')
plt.legend()
plt.show()
