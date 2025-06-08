"""
Global Configuration and Constants for Physics Experiment Helper
CBSE Class XII Computer Science (Subject Code 083) Project
"""

import os
from pathlib import Path

# Base Paths
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data"

# Ensure data directory exists
os.makedirs(DATA_DIR, exist_ok=True)

# Physical Constants
STANDARD_G = 9.80665  # Standard acceleration due to gravity in m/s^2
PI = 3.141592653589793

# Experiment Metadata Catalog
EXPERIMENTS = {
    1: {
        "id": 1,
        "name": "Determining the value of g (Simple Pendulum)",
        "short_name": "Simple Pendulum (g)",
        "file_name": "experiment_data_g.csv",
        "headers": [
            "Length (m)",
            "Error in Length (m)",
            "Number of Oscillations",
            "Time (s)",
            "Error in Time (s)",
            "Value of g (m/s²)",
            "Error (%)"
        ]
    },
    2: {
        "id": 2,
        "name": "Potentiometer Experiment (Voltage & EMF)",
        "short_name": "Potentiometer",
        "file_name": "experiment_data_potentiometer.csv",
        "headers": [
            "EMF (V)",
            "Wire Length (m)",
            "Error in Length (m)",
            "Balance Length (m)",
            "Error in Balance Length (m)",
            "Voltage (V)",
            "Error in Voltage (V)"
        ]
    },
    3: {
        "id": 3,
        "name": "Changing a Galvanometer to an Ammeter or a Voltmeter",
        "short_name": "Galvanometer Conversion",
        "file_name": "experiment_data_galvanometer.csv",
        "headers": [
            "Galvanometer Resistance (ohm)",
            "Max current through Galvanometer (ampere)",
            "Max current through Ammeter (ampere)",
            "Resistance for Ammeter (ohm)",
            "Max voltage across Voltmeter (volt)",
            "Resistance for voltmeter (ohm)"
        ]
    },
    4: {
        "id": 4,
        "name": "Displacement Method for Determining Focal Length of Convex Lens",
        "short_name": "Lens Displacement Method",
        "file_name": "experiment_data_displacement.csv",
        "headers": [
            "D (cm)",
            "x (cm)",
            "Focal length (cm)"
        ]
    },
    5: {
        "id": 5,
        "name": "Calculation of the Speed of Sound using a Resonance Tube",
        "short_name": "Resonance Tube (Sound)",
        "file_name": "experiment_data_sound.csv",
        "legacy_file_name": "experiment_data_soundofsound.csv",
        "headers": [
            "Frequency of tuning fork (Hz)",
            "Length (first resonance) (cm)",
            "Length (second resonance) (cm)",
            "Speed of sound (cm/s)",
            "Speed of sound (m/s)",
            "End correction (cm)"
        ]
    },
    6: {
        "id": 6,
        "name": "Calorimetric Calculations (Principle of Mixtures)",
        "short_name": "Calorimetry",
        "file_name": "experiment_data_calorimetry.csv",
        "legacy_file_name": "experiment_data_Calorimetry.csv",
        "headers": [
            "Value to be calculated",
            "mass-1 (kg)",
            "mass-2 (kg)",
            "mass final (kg)",
            "specific heat-1 (J/kg·K)",
            "specific heat-2 (J/kg·K)",
            "specific heat final (J/kg·K)",
            "Change in temperature-1 (°C)",
            "Change in temperature-2 (°C)",
            "Change in temperature final (°C)"
        ]
    },
    7: {
        "id": 7,
        "name": "Coefficient of Friction Calculation",
        "short_name": "Coefficient of Friction",
        "file_name": "experiment_data_friction.csv",
        "legacy_file_name": "experiment_data_CoefficientOfFriction.csv",
        "headers": [
            "Mass (kg)",
            "Max force taken (N)",
            "Gravitational acceleration (m/s²)",
            "Error in mass measurement (kg)",
            "Error in force measurement (N)",
            "Coefficient of friction",
            "Error in coefficient of friction"
        ]
    },
    8: {
        "id": 8,
        "name": "Young's Modulus Experiment (Searle's Apparatus)",
        "short_name": "Young's Modulus",
        "file_name": "experiment_data_youngs_modulus.csv",
        "legacy_file_name": "experiment_data_Young'sModulus.csv",
        "headers": [
            "Mass (kg)",
            "Gravitational acceleration (m/s²)",
            "Length of wire (m)",
            "Radius of wire (m)",
            "Change in length of wire (m)",
            "Young's Modulus (N/m²)"
        ]
    },
    9: {
        "id": 9,
        "name": "Metre Bridge Experiment (Unknown Resistance)",
        "short_name": "Metre Bridge",
        "file_name": "experiment_data_metre_bridge.csv",
        "legacy_file_name": "experiment_data_MetreBridge.csv",
        "headers": [
            "Known Resistance (ohm)",
            "Length on side of known resistance (cm)",
            "Length on side of unknown resistance (cm)",
            "Error in resistance (ohm)",
            "Least count of measuring instrument (cm)",
            "Value of unknown Resistance (ohm)",
            "Error in resistance (ohm)"
        ]
    },
    10: {
        "id": 10,
        "name": "Coefficient of Viscosity (Stoke's Method)",
        "short_name": "Viscosity (Stoke's Law)",
        "file_name": "experiment_data_viscosity.csv",
        "legacy_file_name": "experiment_data_Coeff_of_friction.csv",  # Fixed bug from original doc
        "headers": [
            "Radius of sphere (m)",
            "Radius of vessel (m)",
            "Gravitational acceleration (m/s²)",
            "Density of sphere (kg/m³)",
            "Density of liquid (kg/m³)",
            "Terminal velocity (m/s)",
            "Coefficient of Viscosity (Pa·s)"
        ]
    }
}
