# Galaxy Supercluster and Basins of Attraction Simulation

This repository provides a simulation of galaxy flows and basins of attraction based on the **Cosmicflows-4 (CF4) dataset** and scientific techniques used to study large-scale cosmic structures. Inspired by the recent paper on **basins of attraction** within the local universe, this project simulates how galaxies gravitate toward regions of dense matter, forming structures like superclusters.

## Project Overview

The paper used in this project discusses large-scale cosmic structures and identifies "basins of attraction" (BoAs) in the local universe. BoAs are gravitational domains that influence galaxy movement across space. Using galaxy redshift, peculiar velocities, and clustering methods, researchers model these basins as regions where gravitational potential funnels galaxies toward dense cores, like the **Laniakea supercluster**.

This project aims to simulate:
- **3D visualizations of galaxies and clusters**
- **Velocity flows toward attractors**, representing BoAs
- **Clustering** of galaxies into basins, where each cluster gravitates toward a common center.

## Theoretical Background

### Galaxy Redshift and Peculiar Velocity
In cosmology, galaxies have two main types of velocities:
1. **Cosmic Expansion (Hubble Flow)**: Due to universal expansion, galaxies appear to move away from us, with speed proportional to their distance.
2. **Peculiar Velocity**: Independent of cosmic expansion, peculiar velocities result from gravitational forces between galaxies and large structures like clusters or superclusters. These are critical for mapping how galaxies are gravitationally attracted toward dense regions in space.

### Basins of Attraction
BoAs represent zones where galaxies follow specific gravitational flows due to nearby large-scale structures. Each BoA centers around a dense region that acts as an attractor, pulling nearby galaxies toward it. Analogous to watersheds, these "gravitational basins" delineate domains where galaxies cluster and flow toward common density minima.

### Mathematical Model
The gravitational flow of galaxies toward these attractors can be represented mathematically by:

   **v<sub>pec</sub>=−∇Φ**

where:
- **v<sub>pec</sub>** is the peculiar velocity,
- **∇Φ** is the gradient of the gravitational potential \( \Phi \), guiding the flow toward density centers.

The peculiar velocity data from CF4 is modeled in 3D space with directional vectors pointing galaxies toward attractors.

## Code Overview

### Dependencies
The project requires the following libraries, specified in `requirements.txt`:
- `numpy`, `pandas`: For numerical operations and data handling.
- `requests`: To query the CF4 dataset API.
- `mayavi`: For 3D visualization.
- `scikit-learn`: For clustering and DBSCAN algorithm.
- `PyQt5`: GUI support for `mayavi`.

### Files
- `simulation.py`: Main script that queries data, processes it, and generates a 3D visualization.
- `requirements.txt`: Specifies required packages for running the code.

### Data Retrieval
The CF4 dataset provides galaxy distances and peculiar velocities. The Cosmicflows API fetches data, where:
- **RA** and **Dec** (right ascension and declination) are used to define galaxy coordinates,
- **Peculiar velocity components** (SG_Vx, SG_Vy, SG_Vz) illustrate galaxy motion toward attractors.

### Code Flow
1. **Data Retrieval**: The script queries the API to get galaxy information for 100 sample points.
2. **Data Preprocessing**:
   - Converts RA/Dec to Cartesian coordinates (x, y, z).
   - Extracts peculiar velocities to represent gravitational flows.
3. **Clustering**:
   - Uses DBSCAN to group galaxies into clusters, simulating BoAs.
   - Clusters represent regions where galaxies share a common attractor.
4. **3D Visualization**:
   - Plots galaxies as blue points in 3D space.
   - Adds red velocity vectors to represent peculiar motion toward attractors.
   - Colors clusters differently to visualize distinct basins of attraction.

### Running the Code
Clone the repository, install the dependencies, and execute `simulation.py`:
```bash
git clone https://github.com/cnajmeddine/computational-cosmology.git
cd GalaxySuperclusterSimulation
pip install -r requirements.txt
python simulation.py
```

## Results and Interpretation

This simulation visualizes galaxy flows within gravitational basins. Each cluster demonstrates the following:
- **Gravitational Influence**: Red vectors show how galaxies are moving within their BoAs.
- **Laniakea Representation**: With adjusted parameters, the cluster containing our galaxy can represent the Laniakea supercluster.

### Example Visualization
The following elements are represented in the visualization:
- **Blue Dots**: Galaxies positioned by their 3D coordinates.
- **Red Lines**: Velocity vectors pointing galaxies toward attractor points.
- **Clusters**: Represented by different colors, each cluster indicates a unique basin.

## Future Work
Possible improvements include:
- Increasing the sample size and refining data resolution.
- Implementing real-time simulation of galaxy motion over time within BoAs.
- Expanding to other known superclusters beyond Laniakea.

## References
1. **Cosmicflows-4 Database**: [EDD Cosmicflows-4](http://edd.ifa.hawaii.edu/CF4)
2. **Basins of Attraction Paper**: *Identification of Basins of Attraction in the Local Universe*

This simulation demonstrates how gravitational flows shape the universe's large-scale structure and provides a foundation for further exploration of cosmic phenomena.
