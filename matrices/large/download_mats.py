#!/usr/bin/env python

import os
import requests

# List of matrix names and their corresponding group names
matrices = {
    "af_0_k101": "Schenk_AFE",
    "af_1_k101": "Schenk_AFE",
    "af_2_k101": "Schenk_AFE",
    "af_3_k101": "Schenk_AFE",
    "af_4_k101": "Schenk_AFE",
    "af_5_k101": "Schenk_AFE",
    "analytics": "Precima",
    "atmosmodd": "Bourchtein",
    "atmosmodj": "Bourchtein",
    "atmosmodl": "Bourchtein",
    "atmosmodm": "Bourchtein",
    "BenElechi1": "BenElechi",
    "boyd2": "GHS_indef",
    "Chevron3": "Chevron",
    "Chevron4": "Chevron",
    "circuit5M": "Freescale",
    "CO": "PARSEC",
    "cont-300": "GHS_indef",
    "crashbasis": "QLi",
    "CurlCurl_3": "Bodendiek",
    "d_pretok": "GHS_indef",
    "dc1": "IBM_EDA",
    "dc2": "IBM_EDA",
    "dc3": "IBM_EDA",
    "ecology1": "McRae",
    "ecology2": "McRae",
    "FEM_3D_thermal2": "Botonakis",
    "Ga10As10H30": "PARSEC",
    "Ga19As19H42": "PARSEC",
    "Ge99H100": "PARSEC",
    "Goodwin_095": "Goodwin",
    "Goodwin_127": "Goodwin",
    "Hamrle3": "Hamrle",
    "Hardesty1": "Hardesty",
    "hcircuit": "Hamm",
    "iChem_Jacobian": "Meng",
    "kim2": "Kim",
    "Lin": "Lin",
    "lung2": "Norris",
    "mac_econ_fwd500": "Williams",
    "majorbasis": "QLi",
    "mc2depi": "Williams",
    "parabolic_fem": "Wissgott",
    "PR02R": "Fluorem",
    "rajat31": "Rajat",
    "RM07R": "Fluorem",
    "Si41Ge41H72": "PARSEC",
    "ss": "VLSI",
    "ss1": "VLSI",
    "stomach": "Norris",
    "t2em": "CEMW",
    "tmt_unsym": "CEMW",
    "torso1": "Norris",
    "torso2": "Norris",
    "turon_m": "GHS_indef",
    "vas_stokes_1M": "VLSI",
    "vas_stokes_2M": "VLSI",
    "xenon2": "Ronis"
}

# Base URL for downloading matrices
base_url = "https://sparse.tamu.edu/mat/"

# Download each matrix
for matrix, group in matrices.items():
    filename = f"{matrix}.mat"
    if os.path.exists(filename):
        print(f"Skipping {filename} - file already exists")
        continue
        
    url = f"{base_url}{group}/{matrix}.mat"
    print(f"Downloading {matrix} from group {group}...")
    print(f"URL: {url}")
    response = requests.get(url)
    if response.status_code == 200:  # 200 means request was successful
        with open(filename, "wb") as file:
            file.write(response.content)
        print(f"Downloaded {filename} successfully.")
    else:
        print(f"Status code: {response.status_code}")
        print(f"Failed to download {filename}.")

print("All downloads completed.")