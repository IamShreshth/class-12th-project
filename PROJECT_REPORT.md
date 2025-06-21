# CBSE Class XII Computer Science (Subject Code 083)
## Project Report: Physics Experiment Helper (Academic Year 2024–25)

---

```
             NARAYANA E-TECHNO SCHOOL
          Andheri East, Mumbai, Maharashtra
            ACADEMIC SESSION: 2024 - 2025

                   PROJECT WORK IN
              COMPUTER SCIENCE (CODE: 083)

                       TITLE:
              PHYSICS EXPERIMENT HELPER

                     SUBMITTED BY:
                  1. Shreshth Dhimole
                  2. Prudhvi Kasinedi
                  3. Hrishikesh Khanna

                     CLASS: XII
                     STREAM: Science (PCM with CS)

                   UNDER THE GUIDANCE OF:
                    Ms. Vimlesh Agrawal
                 PGT (Computer Science), M-Tech CS
```

---

## Certificate

This is to certify that **Shreshth Dhimole**, **Prudhvi Kasinedi**, and **Hrishikesh Khanna**, students of Class XII (Science), have successfully completed the project work entitled **"PHYSICS EXPERIMENT HELPER"** in the subject **Computer Science (083)** laid down in the regulations of the **Central Board of Secondary Education (CBSE)** for the purpose of the All India Senior School Certificate Examination (AISSCE) Practical Examination held at **Narayana E-Techno School, Mumbai**.

The project embodies original work carried out under our guidance and supervision.

<br><br>

___________________________ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ___________________________  
**Internal Examiner / Project Guide** &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **External Examiner**  
(Ms. Vimlesh Agrawal, PGT CS)  

<br>

___________________________  
**Principal's Signature**  
Narayana E-Techno School, Mumbai  

---

## Acknowledgement

Apart from our efforts, the success of this project depends largely on the encouragement and guidelines of many others. We take this opportunity to express our gratitude to the people who have been instrumental in the successful completion of this project.

We express our heartfelt gratitude to our parents for their constant encouragement, moral support, and provisions while carrying out this project.

We gratefully acknowledge the contribution of the individuals who contributed in bringing this project up to this level.

We express our deep sense of gratitude to our respected **Principal, Narayana E-Techno School**, who has been continuously motivating us and extending a helping hand whenever required.

Our sincere thanks to **Ms. Vimlesh Agrawal**, Master In-charge, guide, mentor, and teacher, who critically reviewed our project, guided our architectural decisions, and helped in troubleshooting problems during the design and implementation of this software.

The guidance and support received from all faculty members and fellow students was vital for the success of the project. We are truly grateful for their constant support and help.

---

## Table of Contents

| Sr. No. | Section Description | Page Reference |
| :---: | :--- | :---: |
| **01** | Certificate | Page 02 |
| **02** | Acknowledgement | Page 03 |
| **03** | Introduction | Page 05 |
| **04** | Objectives of the Project | Page 06 |
| **05** | System Development Life Cycle (SDLC) | Page 07 |
| **06** | Detailed Phases of SDLC | Page 08 - 14 |
| **07** | System Architecture & Data Flow | Page 15 - 17 |
| **08** | Flowchart of the System | Page 18 - 19 |
| **09** | Detailed Scientific & Mathematical Formulations | Page 20 - 24 |
| **10** | Modular Python Source Code Listing | Page 25 - 38 |
| **11** | Sample Terminal & Graphical User Interface Outputs | Page 39 - 44 |
| **12** | Hardware and Software Requirements | Page 45 |
| **13** | Testing, Verification & Test Suite Results | Page 46 - 47 |
| **14** | Conclusion & Future Enhancements | Page 48 |
| **15** | Bibliography & Web References | Page 49 |

---

## 1. Introduction

**Physics Experiment Helper** is an integrated software system developed in Python to streamline and automate scientific calculations for physics laboratory experiments in secondary and senior secondary schools (specifically adhering to the CBSE Class XI & XII Physics Practical Syllabus).

In a conventional physics laboratory setting, students perform manual experiments using various physical apparatus (such as a simple pendulum, potentiometer wire, resonance tube, or Searle's apparatus). Afterward, students must manually substitute raw observations into intricate algebraic and trigonometric equations, compute fractions using logarithmic tables or pocket calculators, and calculate instrumental measurement errors (due to apparatus least counts). This manual process frequently introduces arithmetic inaccuracies, obscures the underlying physical principles, and consumes valuable practical examination time.

This project delivers an autonomous computational solution:
- It accepts experimental observations entered by the student through either an interactive console CLI or a desktop GUI.
- It performs mathematical calculations autonomously according to theoretical physical laws.
- It propagates instrumental errors (least counts, scale uncertainties) to calculate absolute and percentage errors.
- It records and persists observations to structured CSV databases in the `data/` directory.
- It provides a historical retrieval engine that displays stored records in formatted tables alongside descriptive statistics (mean, minimum, maximum).

---

## 2. Objectives of the Project

The principal objective of this project is to apply computer science and software engineering principles to solve real-world educational and laboratory problems:

1. **Practical Application of Python Programming:** Utilize procedural, modular, and object-oriented programming techniques taught in CBSE Class XII Computer Science (Subject Code 083).
2. **Elimination of Computational Error:** Prevent calculation discrepancies in laboratory assessments through automated high-precision arithmetic.
3. **Application of Error Propagation Theory:** Implement differential calculus error estimation for physical measurements ($\Delta g/g$, $\Delta V$, $\Delta \mu$, $\Delta X$).
4. **Data Persistence using Standard File Handling:** Demonstrate effective usage of Python's `csv` module for non-volatile storage, schema initialization, and record parsing.
5. **Robust Input Validation:** Shield software execution against runtime crashes caused by invalid data types, negative physical parameters, or zero divisions.
6. **Code Modularity and Maintainability:** Implement clean architectural separation between mathematical calculation engines, storage handlers, and user presentation interfaces.

---

## 3. System Development Life Cycle (SDLC)

The **Systems Development Life Cycle (SDLC)** is a structured project management methodology that partitions complex software engineering projects into well-defined sequential and iterative stages. Applying SDLC ensures that requirements are validated, risks are mitigated, and verification occurs before final deployment.

```mermaid
graph LR
    A[1. Initiation & Concept] --> B[2. Planning]
    B --> C[3. Requirements Analysis]
    C --> D[4. System Design]
    D --> E[5. Development / Coding]
    E --> F[6. Testing & Integration]
    F --> G[7. Implementation & Maintenance]
```

### Detailed SDLC Phases Applied to Physics Experiment Helper:

#### Phase 1: Initiation & Concept Development
- **Opportunity Identification:** Observed that students in physics practical exams lose time and make arithmetic slips while evaluating formulas.
- **Feasibility Study:** Verified that standard school lab computers have Python installed and can run script-based tools without external internet connections or third-party package managers.

#### Phase 2: Planning Phase
- **Scope Definition:** Selected 10 mandatory physics practical experiments spanning mechanics, optics, thermodynamics, electricity, and fluid dynamics.
- **Resource Allocation:** Divided tasks among team members (algorithm design, CSV storage handling, UI/CLI design, and automated testing).

#### Phase 3: Requirements Analysis (SRS)
- **Functional Requirements:** Formally specified input parameters, output metrics, physical validation bounds, and error propagation formulas for each of the 10 experiments.
- **Non-Functional Requirements:** Fast execution (<10ms per calculation), crash-proof input validation, platform independence, and zero external library dependencies.

#### Phase 4: Design Phase
- **Modular Architecture:** Designed a layered architecture separating calculation engines (`src/core/`), persistence (`src/storage/`), presentation (`src/ui/`, `src/gui/`), and automated testing (`tests/`).
- **Data Models:** Designed CSV schemas for each experiment and established standardized headers.
- **Design Patterns:** Selected Strategy Pattern for physics calculations, Factory Pattern for experiment instantiation, and Repository Pattern for file I/O.

#### Phase 5: Development Phase
- **Implementation:** Programmed modules in clean Python 3 with type hints, docstrings, and defensive validation checks.
- **Defect Resolution:** Corrected defects identified in early monolithic prototypes (e.g. viscosity file naming collision, calorimetry mode dispatching, and metre bridge error calculations).

#### Phase 6: Integration & Testing Phase
- **Unit Testing:** Constructed an automated test suite comprising 20 unit tests with standard library `unittest`.
- **Validation:** Tested edge cases including boundary conditions, negative inputs, zero divisors, and non-existent files.

#### Phase 7: Implementation & Maintenance Phase
- **Packaging:** Assembled standalone runnable entry points (`main.py` and `gui_main.py`).
- **Documentation:** Authored comprehensive SRS, Architectural blueprints, Flowchart manuals, and README guides.

---

## 4. Hardware and Software Requirements

### Hardware Requirements
- **Processor:** Dual-Core x86_64 or Apple Silicon CPU (minimum 1.5 GHz)
- **Memory (RAM):** 2 GB RAM minimum (4 GB recommended)
- **Storage:** 50 MB of free hard disk space
- **Input Devices:** Standard Keyboard and Mouse / Trackpad
- **Display Monitor:** Minimum resolution $1024 \times 768$ pixels

### Software Requirements
- **Operating System:** Windows 10/11, macOS (10.15+), or Linux (Ubuntu 18.04+)
- **Interpreter:** Python 3.8, 3.9, 3.10, 3.11, 3.12, or higher
- **Development Environment:** Python IDLE, VS Code, or PyCharm
- **Required Libraries:** Standard Library only (`csv`, `math`, `tkinter`, `unittest`, `dataclasses`, `typing`, `argparse`, `pathlib`)

---

## 5. Mathematical & Scientific Formulations

### 1. Simple Pendulum ($g$ Determination)
$$T = \frac{t}{n}, \quad g = \frac{4\pi^2 L}{T^2}$$
$$\frac{\Delta g}{g} \times 100\% = \left(\frac{\Delta L}{L} + 2\frac{\Delta t}{t}\right) \times 100\%$$

### 2. Potentiometer Experiment
$$k = \frac{E}{L}, \quad V = k \cdot l = E \cdot \frac{l}{L}$$
$$\Delta V = V \left(\frac{\Delta l}{l} + \frac{\Delta L}{L}\right)$$

### 3. Galvanometer Conversion
- **Shunt Resistance for Ammeter:**
  $$S = \frac{I_g \cdot G}{I - I_g} \quad (\text{connected in parallel})$$
- **Multiplier Resistance for Voltmeter:**
  $$R = \frac{V}{I_g} - G \quad (\text{connected in series})$$

### 4. Convex Lens Displacement Method
$$f = \frac{D^2 - x^2}{4D} \quad (\text{valid for } D \ge 4f)$$

### 5. Speed of Sound (Resonance Tube)
$$v = 2f(l_2 - l_1) \quad [\text{cm/s}], \quad e = \frac{l_2 - 3l_1}{2} \quad [\text{cm}]$$

### 6. Calorimetry (Principle of Mixtures)
$$m_1 s_1 \Delta T_1 + m_2 s_2 \Delta T_2 = m_f s_f \Delta T_f$$

### 7. Coefficient of Static Friction
$$\mu = \frac{F_{max}}{m \cdot g}, \quad \Delta \mu = \mu \left(\frac{\Delta m}{m} + \frac{\Delta F}{F_{max}}\right)$$

### 8. Young's Modulus of Elasticity (Searle's Apparatus)
$$Y = \frac{\text{Stress}}{\text{Strain}} = \frac{M \cdot g \cdot L}{\pi \cdot r_w^2 \cdot \Delta l}$$

### 9. Metre Bridge (Wheatstone Bridge)
$$X = R \cdot \frac{l_1}{l_2}, \quad \Delta X = X \left(\frac{lc}{l_1} + \frac{lc}{l_2} + \frac{\Delta R}{R}\right)$$

### 10. Stoke's Viscosity with Wall Correction
$$\eta = \frac{2 r^2 g (\rho_s - \rho_l)}{9 v_t \left(1 + 2.4 \frac{r}{R}\right)}$$

---

## 6. Testing & Quality Assurance Summary

The test suite (`tests/`) runs automatically with standard Python:
```bash
python3 main.py --test
```

### Test Results Breakdown:
- **Experiment Calculations:** 11 tests verifying numerical accuracy against NCERT standard laboratory data.
- **Physical Boundary Validation:** 5 tests verifying that negative lengths, inverted balance points, and out-of-range current values are rejected.
- **Storage & Schema Verification:** 4 tests verifying CSV header generation, atomic record appending, ASCII table generation, and descriptive statistical calculation.
- **Result:** 20 of 20 tests pass with 0 failures and 0 errors in 0.004 seconds.

---

## 7. Conclusion & Future Enhancements

The **Physics Experiment Helper** project successfully fulfills all objectives set forth by the CBSE Class XII Computer Science curriculum. It combines mathematical precision, defensive software engineering, persistent database storage, and accessible user interface design.

### Potential Future Enhancements:
1. **Interactive Graphical Plotting:** Integrate standard canvas or SVG generation to plot resonance curves and stress-strain lines.
2. **Direct Hardware Interfacing:** Interface with Arduino or Raspberry Pi ultrasonic and photo-gate sensors for automated timing acquisition.
3. **Multi-Language Localization:** Provide UI prompt translations in Hindi and other regional Indian languages.

---

## 8. Bibliography
1. CBSE Senior School Curriculum 2024–25: Computer Science (Code 083).
2. NCERT Physics Laboratory Manual for Classes XI and XII.
3. *Computer Science with Python* by Sumita Arora (Dhanpat Rai & Co.).
4. Python Official Documentation: Standard Library Modules (`csv`, `math`, `tkinter`, `unittest`).
