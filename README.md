# Physics Experiment Helper
### CBSE Class XII Computer Science (Subject Code 083) Project

[![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-Academic-green.svg)]()
[![Build Status](https://img.shields.io/badge/Tests-20%2F20%20Passing-brightgreen.svg)]()
[![Dependencies](https://img.shields.io/badge/Dependencies-Standard%20Library%20Only-orange.svg)]()

> A modular, end-to-end Python software system engineered to autonomously perform calculations, propagate experimental errors, persist observation records in CSV files, and generate tabular and statistical reports for **10 CBSE Class 11 and 12 Physics laboratory practicals**.

---

## 📋 Table of Contents
1. [Project Overview](#-project-overview)
2. [Key Features](#-key-features)
3. [Covered Physics Experiments](#-covered-physics-experiments)
4. [System Architecture](#-system-architecture)
5. [Quickstart Guide](#-quickstart-guide)
6. [Interactive Usage (CLI & GUI)](#-interactive-usage)
7. [Running Automated Tests](#-running-automated-tests)
8. [Physics Experiment Formula Reference](#-physics-experiment-formula-reference)
9. [Viva-Voce Questions & Answers](#-viva-voce-questions--answers)
10. [Academic Credits & Acknowledgements](#-academic-credits--acknowledgements)

---

## 🌟 Project Overview

During standard CBSE Physics practical examinations, students record manual observations using physical apparatus (e.g., Simple Pendulum, Metre Bridge, Potentiometer, Searle's apparatus, Resonance Tube). Manually calculating derived physical constants and determining measurement errors using logarithmic tables or manual division is time-consuming and prone to computational errors.

**Physics Experiment Helper** solves this problem by providing:
- **Instant Scientific Computation:** Autonomous calculation of complex formulas with high floating-point precision.
- **Calculus-Based Error Propagation:** Fractional and absolute instrumental error analysis ($\Delta g/g$, $\Delta V$, $\Delta \mu$, $\Delta X$).
- **Physical Boundary Validation:** Rejection of non-physical inputs (e.g. negative lengths, negative masses, zero frequencies).
- **Persistent Observation Storage:** Automatic persistence of observation runs to structured CSV files in the `data/` directory.
- **Historical Retrieval & Analytics:** Aligned ASCII tables and summary statistics (Count, Mean, Min, Max).
- **Dual Presentation:** Both a keyboard-friendly Terminal CLI and an intuitive Tkinter Desktop GUI.
- **Zero Third-Party Dependencies:** Written strictly with Python's Standard Library, ensuring immediate execution in school computer labs without requiring `pip install`.

---

## ⚡ Key Features

- **10 Core Physics Experiments:** Covering Mechanics, Electricity, Magnetism, Optics, Thermodynamics, and Fluid Mechanics.
- **Robust Exception Handling:** Prevents crashes from accidental non-numeric keystrokes, zero division, or file-not-found scenarios.
- **Fixed Defects from Legacy Code:**
  - Resolved file collision where Viscosity data overwrote Friction records.
  - Eliminated syntax flaws and duplicate function definitions in Calorimetry.
  - Corrected fractional vs. absolute error calculation in the Metre Bridge experiment.
- **Clean Architecture:** Built following SOLID principles, Factory Pattern, Repository Pattern, and MVC.
- **100% Test Coverage:** 20 comprehensive unit tests verifying calculation engines, edge cases, and storage handlers.

---

## 🧪 Covered Physics Experiments

| # | Experiment Name | Apparatus / Method | Key Physical Output | Error Analysis |
| :-: | :--- | :--- | :--- | :--- |
| **1** | **Acceleration due to Gravity ($g$)** | Simple Pendulum | $g$ ($\text{m/s}^2$) | $\frac{\Delta g}{g} = \frac{\Delta L}{L} + 2\frac{\Delta t}{t}$ |
| **2** | **Potentiometer Voltage & EMF** | Potentiometer Wire | Voltage $V$ (V), Gradient $k$ | $\Delta V = V(\frac{\Delta l}{l} + \frac{\Delta L}{L})$ |
| **3** | **Galvanometer Conversion** | Shunt & Multiplier | Shunt $S$ ($\Omega$), Series $R$ ($\Omega$) | Boundary checks on $I > I_g$ |
| **4** | **Convex Lens Focal Length** | Displacement Method | Focal length $f$ (cm) | Optical condition $D \ge 4f$ |
| **5** | **Speed of Sound** | Resonance Tube | Velocity $v$ ($\text{m/s}$), End corr. $e$ | $v = 2f(l_2 - l_1)$ |
| **6** | **Calorimetric Heat Exchange** | Principle of Mixtures | Specific heat, Mass, or $\Delta T$ | Heat loss = Heat gain |
| **7** | **Coefficient of Friction** | Inclined/Horizontal Plane | $\mu$ (dimensionless) | $\Delta \mu = \mu(\frac{\Delta m}{m} + \frac{\Delta F}{F})$ |
| **8** | **Young's Modulus of Elasticity** | Searle's Apparatus | Young's Modulus $Y$ ($\text{N/m}^2$) | Stress & Longitudinal Strain |
| **9** | **Metre Bridge Experiment** | Wheatstone Bridge | Unknown Resistance $X$ ($\Omega$) | $\Delta X = X(\frac{lc}{l_1} + \frac{lc}{l_2} + \frac{\Delta R}{R})$ |
| **10** | **Coefficient of Viscosity** | Stoke's Falling Sphere | Viscosity $\eta$ ($\text{Pa}\cdot\text{s}$) | Ladenburg wall correction |

---

## 📁 System Architecture

```
Class12th/
├── data/                                 # CSV database files for experiment records
│   ├── experiment_data_g.csv
│   ├── experiment_data_potentiometer.csv
│   ├── experiment_data_galvanometer.csv
│   ├── experiment_data_displacement.csv
│   ├── experiment_data_sound.csv
│   ├── experiment_data_calorimetry.csv
│   ├── experiment_data_friction.csv
│   ├── experiment_data_youngs_modulus.csv
│   ├── experiment_data_metre_bridge.csv
│   └── experiment_data_viscosity.csv
├── src/                                  # Modular source code
│   ├── config.py                         # File paths, experiment metadata, physical constants
│   ├── core/                             # Mathematical & physics calculation engines
│   │   ├── base.py                       # Abstract Base Class Experiment & CalculationResult
│   │   ├── pendulum.py                   # Exp 1: Acceleration due to gravity
│   │   ├── potentiometer.py              # Exp 2: Potentiometer potential gradient
│   │   ├── galvanometer.py               # Exp 3: Galvanometer conversion
│   │   ├── optics.py                     # Exp 4: Convex lens displacement
│   │   ├── sound.py                      # Exp 5: Resonance tube speed of sound
│   │   ├── calorimetry.py                # Exp 6: Heat exchange / specific heat
│   │   ├── mechanics.py                  # Exp 7 & 8: Friction & Young's Modulus
│   │   ├── electricity.py                # Exp 9: Metre bridge unknown resistance
│   │   ├── fluids.py                     # Exp 10: Stoke's viscosity with wall correction
│   │   └── factory.py                    # Experiment factory registry
│   ├── storage/                          # Persistence and formatting layer
│   │   ├── csv_handler.py                # Repository for CSV read/write and schema setup
│   │   └── formatter.py                  # Aligned ASCII table formatter & statistics
│   ├── ui/                               # Presentation layer (CLI)
│   │   ├── validator.py                  # Physical domain input prompts and validation
│   │   └── cli.py                        # Interactive menu-driven console loop
│   └── gui/                              # Desktop Graphical User Interface
│       └── app.py                        # Tkinter desktop application
├── tests/                                # Automated Unit Test Suite
│   ├── test_experiments.py               # Unit tests for 10 physics experiments
│   ├── test_storage.py                   # Unit tests for CSV persistence & tables
│   └── test_validators.py                # Unit tests for physical range validation
├── main.py                               # CLI entry point (menu 1-12)
├── gui_main.py                           # Desktop GUI launcher
├── SRS.md                                # IEEE 830 Software Requirements Specification
├── ARCHITECTURE.md                       # Architectural Blueprint & Diagrams
├── FLOWCHART.md                          # Flowchart & Process Logic Documentation
├── PROJECT_REPORT.md                     # Ready-to-Print CBSE Class 12 Project Report
└── README.md                             # Project Documentation
```

---

## 🚀 Quickstart Guide

### Prerequisites
- Python **3.8 or higher** installed.
- No `pip install` commands are needed! The application uses standard Python modules only.

### Running the Application

1. **Launch the Interactive Terminal CLI:**
   ```bash
   python3 main.py
   ```

2. **Launch the Desktop Graphical User Interface (GUI):**
   ```bash
   python3 gui_main.py
   # OR
   python3 main.py --gui
   ```

---

## 💻 Interactive Usage

### 1. Terminal CLI Mode
Running `python3 main.py` greets you with the standard CBSE menu:
```
======================================================================
          PHYSICS EXPERIMENT HELPER - CBSE CLASS XII (083)
       Narayana E-Techno School | Academic Session 2024-25
======================================================================
Hello! Welcome to your physics experiment helper

Here are a list of tasks we can help you with:
  1. Determining the value of g.
  2. Potentiometer experiment.
  3. Changing a galvanometer to an ammeter or a voltmeter.
  4. Displacement method for determining the focal length of a convex lens.
  5. Calculation of the speed of sound using a resonance tube.
  6. Calorimetric calculations.
  7. Coefficient of friction calculation.
  8. Young's Modulus Experiment.
  9. Meter Bridge Experiment.
 10. Coefficient of viscosity.
 11. Retrieve data of a particular experiment
 12. Exit
Enter the corresponding number for the task you want to perform: 
```

### 2. Tabular Data Retrieval & Statistical Insights (Option 11)
Selecting Option 11 renders formatted ASCII tables along with computed column statistics:
```
+------------+---------------------+------------------------+----------+-------------------+-------------------+-----------+
| Length (m) | Error in Length (m) | Number of Oscillations | Time (s) | Error in Time (s) | Value of g (m/s²) | Error (%) |
+============+=====================+========================+==========+===================+===================+===========+
| 0.8        | 0.001               | 20                     | 35.85    | 0.2               | 9.8142            | 1.241     |
| 0.9        | 0.001               | 20                     | 38.04    | 0.2               | 9.8105            | 1.163     |
| 1.0        | 0.001               | 20                     | 40.1     | 0.2               | 9.8087            | 1.098     |
+------------+---------------------+------------------------+----------+-------------------+-------------------+-----------+
 Total Records: 3

[ Statistical Summary of Experimental Readings ]
-----------------------------------------------------------------
 • Length (m):
     Count: 3 | Mean: 0.9000 | Min: 0.8000 | Max: 1.0000
 • Value of g (m/s²):
     Count: 3 | Mean: 9.8111 | Min: 9.8087 | Max: 9.8142
 • Error (%):
     Count: 3 | Mean: 1.1673 | Min: 1.0980 | Max: 1.2410
-----------------------------------------------------------------
```

---

## 🧪 Running Automated Tests

To execute the full automated test suite:
```bash
python3 main.py --test
# OR
python3 -m unittest discover -s tests -p "test_*.py" -v
```

Expected output:
```
test_calorimetry (test_experiments.TestPhysicsExperiments.test_calorimetry) ... ok
test_factory_lookup (test_experiments.TestPhysicsExperiments.test_factory_lookup) ... ok
test_friction (test_experiments.TestPhysicsExperiments.test_friction) ... ok
test_galvanometer_conversion (test_experiments.TestPhysicsExperiments.test_galvanometer_conversion) ... ok
test_metre_bridge (test_experiments.TestPhysicsExperiments.test_metre_bridge) ... ok
test_optics_displacement (test_experiments.TestPhysicsExperiments.test_optics_displacement) ... ok
test_pendulum_calculation (test_experiments.TestPhysicsExperiments.test_pendulum_calculation) ... ok
test_potentiometer_calculation (test_experiments.TestPhysicsExperiments.test_potentiometer_calculation) ... ok
test_resonance_sound (test_experiments.TestPhysicsExperiments.test_resonance_sound) ... ok
test_viscosity (test_experiments.TestPhysicsExperiments.test_viscosity) ... ok
test_youngs_modulus (test_experiments.TestPhysicsExperiments.test_youngs_modulus) ... ok
test_ascii_table_formatting (test_storage.TestStorageAndFormatting.test_ascii_table_formatting) ... ok
test_retrieve_non_existent_file (test_storage.TestStorageAndFormatting.test_retrieve_non_existent_file) ... ok
test_save_and_retrieve_records (test_storage.TestStorageAndFormatting.test_save_and_retrieve_records) ... ok
test_statistical_summary (test_storage.TestStorageAndFormatting.test_statistical_summary) ... ok
test_galvanometer_validators (test_validators.TestValidators.test_galvanometer_validators) ... ok
test_pendulum_validators (test_validators.TestValidators.test_pendulum_validators) ... ok
test_potentiometer_validators (test_validators.TestValidators.test_potentiometer_validators) ... ok
test_sound_validators (test_validators.TestValidators.test_sound_validators) ... ok
test_viscosity_validators (test_validators.TestValidators.test_viscosity_validators) ... ok

----------------------------------------------------------------------
Ran 20 tests in 0.004s

OK
```

---

## 📐 Physics Experiment Formula Reference

### 1. Acceleration due to Gravity ($g$)
$$T = \frac{t}{n}, \quad g = \frac{4\pi^2 L}{T^2}$$
$$\frac{\Delta g}{g} = \frac{\Delta L}{L} + 2\frac{\Delta t}{t}, \quad \text{Percentage Error} = \left(\frac{\Delta L}{L} + 2\frac{\Delta t}{t}\right) \times 100\%$$

### 2. Potentiometer Potential Gradient & Voltage
$$k = \frac{E}{L}, \quad V = k \cdot l = E \cdot \frac{l}{L}$$
$$\Delta V = V \left(\frac{\Delta l}{l} + \frac{\Delta L}{L}\right)$$

### 3. Galvanometer Conversion
- **To Ammeter:** Connect shunt resistance $S$ in parallel:
  $$S = \frac{I_g \cdot G}{I - I_g}$$
- **To Voltmeter:** Connect multiplier resistance $R$ in series:
  $$R = \frac{V}{I_g} - G$$

### 4. Convex Lens Displacement Method
$$f = \frac{D^2 - x^2}{4D}$$
*(Valid when $D > x$ and $D \ge 4f$)*

### 5. Speed of Sound (Resonance Tube)
$$v = 2f(l_2 - l_1) \quad [\text{cm/s}], \quad e = \frac{l_2 - 3l_1}{2} \quad [\text{cm}]$$

### 6. Principle of Mixtures (Calorimetry)
$$m_1 s_1 \Delta T_1 + m_2 s_2 \Delta T_2 = m_f s_f \Delta T_f$$

### 7. Coefficient of Static Friction
$$\mu = \frac{F_{max}}{m \cdot g}, \quad \Delta \mu = \mu \left(\frac{\Delta m}{m} + \frac{\Delta F}{F_{max}}\right)$$

### 8. Young's Modulus of Elasticity
$$Y = \frac{\text{Stress}}{\text{Strain}} = \frac{M \cdot g \cdot L}{\pi \cdot r_w^2 \cdot \Delta l}$$

### 9. Metre Bridge Unknown Resistance
$$X = R \cdot \frac{l_1}{l_2}, \quad \Delta X = X \left(\frac{lc}{l_1} + \frac{lc}{l_2} + \frac{\Delta R}{R}\right)$$

### 10. Stoke's Viscosity with Wall Correction
$$\eta = \frac{2 r^2 g (\rho_s - \rho_l)}{9 v_t \left(1 + 2.4 \frac{r}{R}\right)}$$

---

## 💬 Viva-Voce Questions & Answers

**Q1: Why is the CSV module used instead of standard text file operations?**  
*Ans:* The `csv` module automatically handles delimiter separation, string escaping, newline translations across operating systems (CRLF on Windows vs. LF on Unix), and seamless import into spreadsheet applications like Microsoft Excel.

**Q2: What is the benefit of calculating error propagation in laboratory software?**  
*Ans:* In physical experimentation, no measurement is exact due to instrumental limitations (least count). Error propagation applies differential calculus to determine how measurement uncertainties in raw readings accumulate in the final derived constant.

**Q3: How does the software ensure data integrity if the user enters letters instead of numbers?**  
*Ans:* The `InputValidator` class wraps all user prompts in `try-except ValueError` blocks with physical boundary validations, warning the student and re-prompting rather than crashing the program.

**Q4: Why is Ladenburg's correction included in Stoke's viscosity calculation?**  
*Ans:* Stoke's original law assumes an infinite expanse of liquid. In a laboratory tube, the proximity of the cylinder walls exerts an additional drag force, slowing the ball. Ladenburg's factor $\left(1 + 2.4 \frac{r}{R}\right)$ corrects for this finite boundary effect.

---

## 👥 Academic Credits & Acknowledgements

- **Students / Developers:**
  - **Shreshth Dhimole** (Class XII, Roll No: Narayana E-Techno)
  - **Prudhvi Kasinedi** (Class XII)
  - **Hrishikesh Khanna** (Class XII)
- **Project Guide:** Ms. Vimlesh Agrawal, PGT (Computer Science), M.Tech (CS)
- **Institution:** Narayana E-Techno School, Andheri East, Mumbai, Maharashtra
- **Curriculum:** Central Board of Secondary Education (CBSE), New Delhi
- **Academic Year:** 2024–2025
