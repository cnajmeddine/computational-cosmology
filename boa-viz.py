import numpy as np
import pandas as pd
import requests
import json
from mayavi import mlab
from sklearn.cluster import DBSCAN

# Step 1: Retrieve Data from the Cosmicflows API
def get_cosmicflows_data(alpha, delta, system='supergalactic', parameter='distance', value=20, calculator='NAM'):
    """
    Query the Cosmicflows API and retrieve distance and velocity data.
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
        return response.json()
    except Exception as e:
        print("Error:", e)
        return None

# Step 2: Generate Random Galaxy Coordinates for Simulation
coordinates = [
    {'alpha': np.random.uniform(0, 360), 'delta': np.random.uniform(-90, 90)} 
    for _ in range(100)  # Retrieve data for 100 galaxies
]

# Step 3: Retrieve Data and Organize in a DataFrame
data = []
for coord in coordinates:
    result = get_cosmicflows_data(alpha=coord['alpha'], delta=coord['delta'])
    if result and result['message'] == 'Success':
        data.append(result)

# Convert data to DataFrame
df = pd.DataFrame(data)
df[['SG_Vx', 'SG_Vy', 'SG_Vz']] = df['peculiar_velocity'].apply(
    lambda x: pd.Series(x) if isinstance(x, dict) else pd.Series([None, None, None]))

# Convert distance to a numeric type, handling lists by taking the first element
df['distance'] = df['distance'].apply(lambda x: x[0] if isinstance(x, list) else x)
df['distance'] = pd.to_numeric(df['distance'], errors='coerce')

# Step 4: Convert RA/Dec to 3D Coordinates (x, y, z)
df['x'] = np.cos(np.radians(df['RA'])) * np.cos(np.radians(df['Dec'])) * df['distance']
df['y'] = np.sin(np.radians(df['RA'])) * np.cos(np.radians(df['Dec'])) * df['distance']
df['z'] = np.sin(np.radians(df['Dec'])) * df['distance']

# Step 5: Cluster Identification (simulate basins of attraction)
coords = df[['x', 'y', 'z']].values
clustering = DBSCAN(eps=10, min_samples=3).fit(coords)
df['cluster'] = clustering.labels_

# Step 6: Visualization
fig = mlab.figure(size=(800, 600), bgcolor=(0, 0, 0))

# Plot clusters with different colors
for cluster_id in set(df['cluster']):
    cluster_data = df[df['cluster'] == cluster_id]
    color = (np.random.rand(), np.random.rand(), np.random.rand()) if cluster_id != -1 else (1, 1, 1)
    mlab.points3d(cluster_data['x'], cluster_data['y'], cluster_data['z'], color=color, scale_factor=1.5)

# Plot velocity vectors for each galaxy
for i in range(len(df)):
    if pd.notnull(df.at[i, 'SG_Vx']):
        mlab.quiver3d(df['x'].iloc[i], df['y'].iloc[i], df['z'].iloc[i],
                      df['SG_Vx'].iloc[i], df['SG_Vy'].iloc[i], df['SG_Vz'].iloc[i],
                      color=(1, 0, 0), scale_factor=0.5, line_width=0.5, mode='arrow')

# Finalize and display
mlab.title('3D Simulation of Galaxy Clusters and Basins of Attraction', color=(1, 1, 1), size=0.5)
mlab.xlabel('X')
mlab.ylabel('Y')
mlab.zlabel('Z')
mlab.show()
