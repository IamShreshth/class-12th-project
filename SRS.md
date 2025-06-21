# Software Requirements Specification (SRS)
## Physics Experiment Helper (CBSE Class XII - Subject Code 083)

**Document Reference:** SRS-CBSE-PHY-2024-25  
**Version:** 2.0.0  
**Status:** Approved / Release  
**Authors:** Shreshth Dhimole, Prudhvi Kasinedi, Hrishikesh Khanna  
**Project Guide:** Ms. Vimlesh Agrawal, PGT (Computer Science)  
**Institution:** Narayana E-Techno School, Andheri East, Mumbai, Maharashtra  
**Academic Session:** 2024–25  

---

## 1. Introduction

### 1.1 Purpose
This Software Requirements Specification (SRS) defines the functional, non-functional, mathematical, and architectural requirements for the **Physics Experiment Helper** software. The system is engineered to assist secondary and senior secondary students (specifically CBSE Class XI and XII Physics practical curricula) in conducting laboratory calculations autonomously, computing scientific measurement error propagations, persisting experimental observation data to structured databases (CSV files), and retrieving historical laboratory logs with tabular formatting and descriptive statistical summaries.

### 1.2 Document Conventions
- This document conforms to the **IEEE Std 830-1998 Recommended Practice for Software Requirements Specifications**.
- All mathematical formulas follow standard SI units unless explicitly noted otherwise.
- Priority levels:
  - **[M]** = Mandatory (Core CBSE syllabus compliance)
  - **[D]** = Desirable (Enhanced usability and safety)
  - **[O]** = Optional (Future enhancement)

### 1.3 Intended Audience
- **CBSE Practical Examiners & Teachers:** To inspect syllabus conformance, algorithmic correctness, and code organization.
- **Students & Lab Assistants:** To compute physical properties without calculation arithmetic errors and verify experimental observations against theoretical bounds.
- **Software Developers & Evaluators:** To maintain, verify, and extend the computational models.

### 1.4 Project Scope
The software covers ten mandatory physics experiments from Mechanics, Optics, Thermodynamics, Electricity, and Fluid Dynamics, accompanied by an atomic CSV persistence engine, tabular retrieval system, and dual presentation interfaces (Terminal CLI and Tkinter GUI):
1. Acceleration due to Gravity ($g$) using a Simple Pendulum.
2. Potentiometer Potential Gradient and Voltage Determination.
3. Conversion of Galvanometer into Ammeter and Voltmeter.
4. Convex Lens Focal Length using Two-Pin Displacement Method.
5. Speed of Sound and End Correction using Resonance Tube.
6. Calorimetric Heat Exchange and Specific Heat (Principle of Mixtures).
7. Coefficient of Static Friction and Propagated Error.
8. Young's Modulus of Elasticity using Searle's Apparatus / Stretched Wire.
9. Metre Bridge Unknown Resistance via Wheatstone Bridge Principle.
10. Coefficient of Viscosity via Stoke's Terminal Velocity Method (with Ladenburg Wall Correction).
11. Historical Observation Record Retrieval and Statistical Analysis.

### 1.5 References
- CBSE Senior School Curriculum, Computer Science (Code 083), Python & Data Management.
- NCERT Physics Laboratory Manual for Class XI and Class XII.
- IEEE Std 830-1998: *IEEE Recommended Practice for Software Requirements Specifications*.

---

## 2. Overall Description

### 2.1 Product Perspective
In traditional school laboratories, students record raw observations manually and spend substantial practical exam time performing repetitive manual calculations and estimating instrumental errors. Human calculation errors in log tables or manual division often distort experimental conclusions. 

**Physics Experiment Helper** is an autonomous standalone educational software system. It bridges the gap between laboratory instrumentation and computational verification:

```
[ Student Measurements ] 
         │
         ▼
[ Physics Experiment Helper ] ──> [ Scientific Calculation Engine ]
         │                                   │
         ├──> [ Physical Domain Validator ]  ├──> [ Error Propagation ]
         │                                   │
         ▼                                   ▼
[ Formatted Presentation (CLI/GUI) ] <── [ Tabular & Statistical Engine ]
         │
         ▼
[ Persistent Observation Store (CSV) ]
```

### 2.2 Product Functions
- **Autonomous Calculation:** Executes rigorous physics equations across 10 experiments.
- **Instrumental Error Propagation:** Evaluates absolute, fractional, and percentage errors according to standard calculus-based error propagation rules.
- **Physical Domain Validation:** Prohibits impossible inputs (negative lengths, negative masses, zero frequencies, impossible optical distances) and alerts users when outputs deviate from standard room conditions.
- **Observation Persistence:** Appends valid laboratory trials to organized CSV data stores with timestamps and appropriate column headers.
- **Data Retrieval & Statistical Insights:** Displays stored observations in ASCII tables with computed sample count, mean, minimum, and maximum for continuous variables.

### 2.3 User Classes and Characteristics
- **Student User:** High school student with basic computer literacy. Requires intuitive prompts, clear units, and robust protection against accidental typing mistakes.
- **Teacher / Evaluator:** Expert evaluating student practicals. Requires transparent access to mathematical formulas, intermediate variables, and audit logs of student observations.

### 2.4 Operating Environment
- **Operating System:** Platform independent (Windows 10/11, macOS Monterey+, Linux Ubuntu 20.04+).
- **Runtime:** Python 3.8 or higher (Standard Library only; zero third-party pip dependencies required).
- **Display Resolution:** Minimum 1024x768 pixels for GUI; 80-column terminal for CLI.

### 2.5 Design and Implementation Constraints
- **Zero Third-Party Dependencies:** To guarantee execution on school computers restricted from internet access or `pip install`, all modules must strictly utilize Python Standard Library (`math`, `csv`, `tkinter`, `unittest`, `dataclasses`, `typing`).
- **Data Portability:** Data stores must be standard comma-separated values (CSV) openable in Microsoft Excel, LibreOffice Calc, or Google Sheets.

---

## 3. Specific Functional Requirements

### 3.1 Experiment 1: Acceleration due to Gravity (Simple Pendulum)
- **FR-1.1:** System shall accept Pendulum Length $L$ (m), Length Error $\Delta L$ (m), Number of Oscillations $n$, Time $t$ (s), and Time Error $\Delta t$ (s).
- **FR-1.2:** System shall compute effective time period $T = t / n$.
- **FR-1.3:** System shall calculate $g = \frac{4\pi^2 L}{T^2}$.
- **FR-1.4:** System shall calculate percentage error:
  $$\frac{\Delta g}{g} \times 100\% = \left(\frac{\Delta L}{L} + 2\frac{\Delta t}{t}\right) \times 100\%$$
- **FR-1.5:** System shall alert user if computed $g$ deviates by more than $2.0\text{ m/s}^2$ from standard $9.8\text{ m/s}^2$.

### 3.2 Experiment 2: Potentiometer Voltage & EMF Comparison
- **FR-2.1:** System shall accept Known EMF $E$ (V), Total Wire Length $L$ (m), Error in Wire Length $\Delta L$ (m), Balancing Length $l$ (m), and Error in Balancing Length $\Delta l$ (m).
- **FR-2.2:** System shall enforce condition $0 < l \le L$.
- **FR-2.3:** System shall compute Potential Gradient $k = E / L$ and Voltage $V = k \cdot l$.
- **FR-2.4:** System shall compute propagated error:
  $$\Delta V = V \left(\frac{\Delta l}{l} + \frac{\Delta L}{L}\right)$$

### 3.3 Experiment 3: Galvanometer Conversion (Ammeter & Voltmeter)
- **FR-3.1:** System shall accept Galvanometer Resistance $G$ ($\Omega$) and Full Scale Deflection Current $I_g$ (A).
- **FR-3.2:** System shall support three modes: Mode 1 (Ammeter), Mode 2 (Voltmeter), Mode 3 (Both).
- **FR-3.3 (Ammeter):** Given target current $I > I_g$, system shall calculate required parallel Shunt Resistance:
  $$S = \frac{I_g \cdot G}{I - I_g}$$
- **FR-3.4 (Voltmeter):** Given target voltage $V > (I_g \cdot G)$, system shall calculate required series Multiplier Resistance:
  $$R = \frac{V}{I_g} - G$$

### 3.4 Experiment 4: Convex Lens Focal Length (Displacement Method)
- **FR-4.1:** System shall accept Object-to-Screen distance $D$ (cm) and Inter-lens displacement $x$ (cm).
- **FR-4.2:** System shall validate that $x < D$ and $D > 0$.
- **FR-4.3:** System shall calculate focal length:
  $$f = \frac{D^2 - x^2}{4D}$$
- **FR-4.4:** System shall warn the user if $D < 4f$ (condition required for real images on screen).

### 3.5 Experiment 5: Speed of Sound (Resonance Tube)
- **FR-5.1:** System shall accept Tuning Fork Frequency $f$ (Hz), First Resonance Length $l_1$ (cm), and Second Resonance Length $l_2$ (cm).
- **FR-5.2:** System shall enforce $l_2 > l_1 > 0$.
- **FR-5.3:** System shall calculate velocity of sound:
  $$v = 2f(l_2 - l_1) \quad [\text{cm/s and m/s}]$$
- **FR-5.4:** System shall calculate acoustic end correction:
  $$e = \frac{l_2 - 3l_1}{2} \quad [\text{cm}]$$

### 3.6 Experiment 6: Calorimetric Calculations (Principle of Mixtures)
- **FR-6.1:** System shall model heat balance:
  $$m_1 s_1 \Delta T_1 + m_2 s_2 \Delta T_2 = m_f s_f \Delta T_f$$
- **FR-6.2:** System shall allow user to compute:
  - Specific heat capacity $s_f = \frac{m_1 s_1 \Delta T_1 + m_2 s_2 \Delta T_2}{m_f \Delta T_f}$
  - Mass $m_f = \frac{m_1 s_1 \Delta T_1 + m_2 s_2 \Delta T_2}{s_f \Delta T_f}$
  - Temperature change $\Delta T_f = \frac{m_1 s_1 \Delta T_1 + m_2 s_2 \Delta T_2}{m_f s_f}$
- **FR-6.3:** System shall prevent division-by-zero if product of denominator terms equals zero.

### 3.7 Experiment 7: Coefficient of Friction
- **FR-7.1:** System shall accept Mass $m$ (kg), Limiting Frictional Force $F_{max}$ (N), Local Gravity $g$ (m/s²), and measurement errors $\Delta m$, $\Delta F$.
- **FR-7.2:** System shall compute coefficient of static friction:
  $$\mu = \frac{F_{max}}{m \cdot g}$$
- **FR-7.3:** System shall calculate error propagation:
  $$\Delta \mu = \mu \left(\frac{\Delta m}{m} + \frac{\Delta F}{F_{max}}\right)$$

### 3.8 Experiment 8: Young's Modulus of Elasticity (Searle's Apparatus)
- **FR-8.1:** System shall accept Test Mass $M$ (kg), Local Gravity $g$ (m/s²), Original Wire Length $L$ (m), Wire Radius $r_w$ (m), and Extension $\Delta l$ (m).
- **FR-8.2:** System shall enforce $0 < \Delta l < L$ and $r_w > 0$.
- **FR-8.3:** System shall calculate cross-sectional area $A = \pi r_w^2$, Tensile Stress $\sigma = \frac{Mg}{A}$, Tensile Strain $\varepsilon = \frac{\Delta l}{L}$, and Young's Modulus:
  $$Y = \frac{\sigma}{\varepsilon} = \frac{M \cdot g \cdot L}{\pi \cdot r_w^2 \cdot \Delta l} \quad [\text{N/m}^2]$$

### 3.9 Experiment 9: Metre Bridge (Wheatstone Bridge Unknown Resistance)
- **FR-9.1:** System shall accept Known Resistance $R$ ($\Omega$), Balancing Segments $l_1$ (cm) and $l_2$ (cm), Resistance Error $\Delta R$ ($\Omega$), and Meter Scale Least Count $lc$ (cm).
- **FR-9.2:** System shall compute unknown resistance:
  $$X = R \cdot \frac{l_1}{l_2}$$
- **FR-9.3:** System shall compute fractional and absolute measurement error:
  $$\Delta X = X \left(\frac{lc}{l_1} + \frac{lc}{l_2} + \frac{\Delta R}{R}\right)$$
  *(Fixes legacy defect where fractional error was erroneously reported as absolute resistance).*

### 3.10 Experiment 10: Coefficient of Viscosity (Stoke's Method)
- **FR-10.1:** System shall accept Sphere Radius $r$ (m), Vessel Tube Radius $R$ (m), Local Gravity $g$ (m/s²), Sphere Density $\rho_s$ (kg/m³), Liquid Density $\rho_l$ (kg/m³), and Terminal Velocity $v_t$ (m/s).
- **FR-10.2:** System shall enforce physical conditions $r < R$ and $\rho_s > \rho_l$.
- **FR-10.3:** System shall compute dynamic viscosity incorporating Ladenburg's cylindrical wall correction:
  $$\eta = \frac{2 r^2 g (\rho_s - \rho_l)}{9 v_t \left(1 + 2.4 \frac{r}{R}\right)} \quad [\text{Pa}\cdot\text{s}]$$
- **FR-10.4:** System shall store records in `experiment_data_viscosity.csv` *(Fixes legacy defect where viscosity observations overwrote friction observations).*

### 3.11 Data Persistence & Schema Management
- **FR-11.1:** System shall prompt user whether to store calculated results after each experiment run.
- **FR-11.2:** If the target CSV file does not exist, the system shall initialize it with exact standardized headers before writing row records.
- **FR-11.3:** The persistence engine shall perform thread-safe and non-destructive appending (`mode='a'`).

### 3.12 Tabular Retrieval and Statistics
- **FR-12.1:** System shall allow user to select any of the 10 experiments to inspect stored observations.
- **FR-12.2:** System shall render tabular data in an aligned ASCII box format in CLI mode and a searchable scrollable `Treeview` in GUI mode.
- **FR-12.3:** System shall automatically compute and print sample count, mean, minimum, and maximum for all continuous numeric columns.

---

## 4. Non-Functional Requirements

### 4.1 Performance & Latency
- All physics calculations and error propagations shall complete in under **10 milliseconds** on standard school computer hardware.
- Table retrieval and statistical analysis for databases of up to 5,000 records shall render in under **200 milliseconds**.

### 4.2 Reliability & Fault Tolerance
- Zero unhandled crash policy: The system shall gracefully catch `ValueError`, `ZeroDivisionError`, `KeyboardInterrupt`, and `FileNotFoundError`.
- If an invalid string is entered where a number is expected, the system shall display an explanatory error and re-prompt the user without losing current context.

### 4.3 Usability & Human Factors
- Dual interfaces: Accessible via standard interactive terminal CLI (for minimal classroom setups) and a modern visual Tkinter GUI (with real-time formulas and visual data tables).
- Clear input hints specifying physical units (m, cm, kg, N, Hz, $\Omega$, V, °C).

### 4.4 Portability & Maintainability
- 100% compliant with standard Python 3.8+ across Windows, macOS, and Linux.
- Object-oriented architecture decoupling calculation logic (`src/core/`), persistence (`src/storage/`), and user presentation (`src/ui/`, `src/gui/`).

---

## 5. Verification Matrix

| Requirement ID | Description | Test Case Reference |
| :--- | :--- | :--- |
| **FR-1.1 - 1.5** | Simple Pendulum $g$ & error | `tests/test_experiments.py::test_pendulum_calculation` |
| **FR-2.1 - 2.4** | Potentiometer voltage & error | `tests/test_experiments.py::test_potentiometer_calculation` |
| **FR-3.1 - 3.4** | Galvanometer Ammeter/Voltmeter | `tests/test_experiments.py::test_galvanometer_conversion` |
| **FR-4.1 - 4.4** | Convex lens displacement | `tests/test_experiments.py::test_optics_displacement` |
| **FR-5.1 - 5.4** | Resonance tube speed of sound | `tests/test_experiments.py::test_resonance_sound` |
| **FR-6.1 - 6.3** | Calorimetry heat exchange | `tests/test_experiments.py::test_calorimetry` |
| **FR-7.1 - 7.3** | Friction coefficient & error | `tests/test_experiments.py::test_friction` |
| **FR-8.1 - 8.3** | Young's Modulus & stress/strain | `tests/test_experiments.py::test_youngs_modulus` |
| **FR-9.1 - 9.3** | Metre bridge resistance & error | `tests/test_experiments.py::test_metre_bridge` |
| **FR-10.1 - 10.4** | Stoke's viscosity & Ladenburg factor | `tests/test_experiments.py::test_viscosity` |
| **FR-11.1 - 11.3** | CSV schema & append operations | `tests/test_storage.py::test_save_and_retrieve_records` |
| **FR-12.1 - 12.3** | Tabular formatting & statistics | `tests/test_storage.py::test_ascii_table_formatting` |
