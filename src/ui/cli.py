"""
Command-Line Interface (CLI) for Physics Experiment Helper
CBSE Class XII Computer Science (Subject Code 083) Project
"""

import sys
from typing import Optional
from src.config import EXPERIMENTS, STANDARD_G
from src.core.factory import get_experiment
from src.storage.csv_handler import CSVRepository
from src.storage.formatter import format_table, format_statistics
from src.ui.validator import InputValidator


class PhysicsCLI:
    """Coordinates menu dispatching, experiment input collection, and result display."""

    def __init__(self):
        self.repo = CSVRepository()
        self.validator = InputValidator()

    def print_banner(self):
        print("\n" + "=" * 70)
        print("          PHYSICS EXPERIMENT HELPER - CBSE CLASS XII (083)")
        print("       Narayana E-Techno School | Academic Session 2024-25")
        print("=" * 70)
        print("Hello! Welcome to your physics experiment helper")

    def display_main_menu(self):
        print("\nHere are a list of tasks we can help you with:")
        print("  1. Determining the value of g.")
        print("  2. Potentiometer experiment.")
        print("  3. Changing a galvanometer to an ammeter or a voltmeter.")
        print("  4. Displacement method for determining the focal length of a convex lens.")
        print("  5. Calculation of the speed of sound using a resonance tube.")
        print("  6. Calorimetric calculations.")
        print("  7. Coefficient of friction calculation.")
        print("  8. Young's Modulus Experiment.")
        print("  9. Meter Bridge Experiment.")
        print(" 10. Coefficient of viscosity.")
        print(" 11. Retrieve data of a particular experiment")
        print(" 12. Exit")

    def run(self):
        """Main event loop matching the project flowchart."""
        self.print_banner()

        while True:
            self.display_main_menu()
            try:
                choice = self.validator.get_int("Enter the corresponding number for the task you want to perform", min_val=1, max_val=12)
            except (KeyboardInterrupt, EOFError):
                print("\n\nExiting application. Goodbye!")
                break

            if choice == 1:
                self.handle_pendulum()
            elif choice == 2:
                self.handle_potentiometer()
            elif choice == 3:
                self.handle_galvanometer()
            elif choice == 4:
                self.handle_optics()
            elif choice == 5:
                self.handle_sound()
            elif choice == 6:
                self.handle_calorimetry()
            elif choice == 7:
                self.handle_friction()
            elif choice == 8:
                self.handle_youngs_modulus()
            elif choice == 9:
                self.handle_metre_bridge()
            elif choice == 10:
                self.handle_viscosity()
            elif choice == 11:
                self.handle_retrieval()
            elif choice == 12:
                print("\nExiting the application... Thank you for using Physics Experiment Helper!")
                break

    # -------------------------------------------------------------------------
    # Experiment Handlers (1 - 10)
    # -------------------------------------------------------------------------

    def handle_pendulum(self):
        print("\n--- [ Task 1: Determining the Value of g ] ---")
        exp = get_experiment(1)
        length = self.validator.get_float("Enter the length of the pendulum (in meters)", min_val=0.001)
        length_error = self.validator.get_float("Enter the error in length (in meters)", min_val=0.0)
        num_oscillations = self.validator.get_int("Enter the number of oscillations", min_val=1)
        time = self.validator.get_float("Enter the time taken for the oscillations (in seconds)", min_val=0.001)
        time_error = self.validator.get_float("Enter the error in time (in seconds)", min_val=0.0)

        res = exp.calculate(length=length, length_error=length_error,
                            num_oscillations=num_oscillations, time=time, time_error=time_error)

        if not res.success:
            print(f"Error: {res.error_message}")
            return

        print(f"\nThe value of g is approximately: {res.get('g')} m/s².")
        print(f"The error in the measurement is approximately: {res.get('error_percentage')} %")
        print(f"Absolute error in g: ±{res.get('absolute_error')} m/s²")
        for w in res.warnings:
            print(f"  [Warning] {w}")

        if self.validator.get_yes_no("Do you want to store this data for the 'g' experiment?"):
            row = exp.format_csv_row(res.data, res)
            if self.repo.save_record(exp.file_name, exp.headers, row):
                print(f"✓ Data successfully saved to '{exp.file_name}'.")

    def handle_potentiometer(self):
        print("\n--- [ Task 2: Potentiometer Experiment ] ---")
        exp = get_experiment(2)
        emf = self.validator.get_float("Enter the known electromotive force (EMF) in volts", min_val=0.001)
        wire_length = self.validator.get_float("Enter the total length of the potentiometer wire in meters", min_val=0.01)
        error_wire_length = self.validator.get_float("Enter the error in wire length measurement in meters", min_val=0.0)
        balance_length = self.validator.get_float("Enter the length of the wire where balance is achieved in meters", min_val=0.001)
        error_balance_length = self.validator.get_float("Enter the error in balance length measurement in meters", min_val=0.0)

        res = exp.calculate(emf=emf, wire_length=wire_length, error_wire_length=error_wire_length,
                            balance_length=balance_length, error_balance_length=error_balance_length)

        if not res.success:
            print(f"Error: {res.error_message}")
            return

        print(f"\nVoltage (V): {res.get('voltage')} V")
        print(f"Error in Voltage: {res.get('error_voltage')} V ({res.get('percentage_error')} %)")
        print(f"Potential Gradient (k): {res.get('potential_gradient')} V/m")

        if self.validator.get_yes_no("Do you want to store this data for the potentiometer experiment?"):
            row = exp.format_csv_row(res.data, res)
            if self.repo.save_record(exp.file_name, exp.headers, row):
                print(f"✓ Data successfully saved to '{exp.file_name}'.")

    def handle_galvanometer(self):
        print("\n--- [ Task 3: Changing Galvanometer to Ammeter / Voltmeter ] ---")
        exp = get_experiment(3)
        G = self.validator.get_float("Enter the resistance of the galvanometer (in ohms)", min_val=0.001)
        ig = self.validator.get_float("Enter the maximum possible current through the galvanometer (in ampere)", min_val=0.000001)

        print("Options:\n  1. Convert to Ammeter\n  2. Convert to Voltmeter\n  3. Convert to Both")
        needwhat = self.validator.get_int("Enter 1 for ammeter, 2 for voltmeter, or 3 for both", min_val=1, max_val=3)

        i_target = None
        v_target = None

        if needwhat in (1, 3):
            i_target = self.validator.get_float("Enter the maximum possible current you want to measure with the ammeter (in ampere)", min_val=ig * 1.0001)
        if needwhat in (2, 3):
            v_target = self.validator.get_float("Enter the maximum possible voltage you want the voltmeter to measure (in volts)", min_val=(ig * G) * 1.0001)

        res = exp.calculate(G=G, ig=ig, mode=needwhat, i_target=i_target, v_target=v_target)
        if not res.success:
            print(f"Error: {res.error_message}")
            return

        if needwhat in (1, 3):
            print(f"\nThe resistance you need to connect in parallel (Shunt S) is: {res.get('r_shunt')} ohms")
        if needwhat in (2, 3):
            print(f"The resistance you need to connect in series (Multiplier R) is: {res.get('r_series')} ohms")

        if self.validator.get_yes_no("Do you want to store this data for the galvanometer experiment?"):
            row = exp.format_csv_row(res.data, res)
            if self.repo.save_record(exp.file_name, exp.headers, row):
                print(f"✓ Data successfully saved to '{exp.file_name}'.")

    def handle_optics(self):
        print("\n--- [ Task 4: Displacement Method for Focal Length of Convex Lens ] ---")
        exp = get_experiment(4)
        D = self.validator.get_float("Enter the measured distance between object and screen when sharp image is formed (in cm)", min_val=1.0)
        x = self.validator.get_float("Enter the measured distance between two positions of the lens for sharp images (in cm)", min_val=0.0, max_val=D - 0.001)

        res = exp.calculate(D=D, x=x)
        if not res.success:
            print(f"Error: {res.error_message}")
            return

        print(f"\nThe approximate focal length is: {res.get('focal_length')} cm")
        for w in res.warnings:
            print(f"  [Warning] {w}")

        if self.validator.get_yes_no("Do you want to store this data for the displacement method for focal length experiment?"):
            row = exp.format_csv_row(res.data, res)
            if self.repo.save_record(exp.file_name, exp.headers, row):
                print(f"✓ Data successfully saved to '{exp.file_name}'.")

    def handle_sound(self):
        print("\n--- [ Task 5: Calculation of Speed of Sound using Resonance Tube ] ---")
        exp = get_experiment(5)
        freq = self.validator.get_float("Enter the frequency of the tuning fork (in Hz)", min_val=1.0)
        l1 = self.validator.get_float("Enter the measured length of the air column corresponding to first resonance (in cm)", min_val=0.1)
        l2 = self.validator.get_float("Enter the measured length of the air column corresponding to second resonance (in cm)", min_val=l1 + 0.1)

        res = exp.calculate(frequency=freq, l1=l1, l2=l2)
        if not res.success:
            print(f"Error: {res.error_message}")
            return

        print(f"\nThe approximate speed of sound is: {res.get('velocity_cm_s')} cm/s ({res.get('velocity_m_s')} m/s)")
        print(f"The end correction is: {res.get('end_correction')} cm")
        for w in res.warnings:
            print(f"  [Warning] {w}")

        if self.validator.get_yes_no("Do you want to store this data for the speed of sound experiment?"):
            row = exp.format_csv_row(res.data, res)
            if self.repo.save_record(exp.file_name, exp.headers, row):
                print(f"✓ Data successfully saved to '{exp.file_name}'.")

    def handle_calorimetry(self):
        print("\n--- [ Task 6: Calorimetric Calculations ] ---")
        exp = get_experiment(6)
        print("Please enter what you need to calculate (only index number):")
        print("  1. Specific heat capacity")
        print("  2. Mass")
        print("  3. Change in temperature")
        mode = self.validator.get_int("Enter option (1-3)", min_val=1, max_val=3)

        m1 = self.validator.get_float("Enter mass of component 1 in kg", min_val=0.0001)
        m2 = self.validator.get_float("Enter mass of component 2 in kg", min_val=0.0001)
        dt1 = self.validator.get_float("Enter change in temperature of component 1 (°C)")
        dt2 = self.validator.get_float("Enter change in temperature of component 2 (°C)")

        mf = None
        sf = None
        dtf = None

        if mode == 1:
            mf = self.validator.get_float("Enter mass of the component of which specific heat has to be found in kg", min_val=0.0001)
            dtf = self.validator.get_float("Enter change in temperature of component of which specific heat has to be found (°C)")
            s1 = self.validator.get_float("Enter specific heat of component 1 (J/kg·K)", min_val=0.1)
            s2 = self.validator.get_float("Enter specific heat of component 2 (J/kg·K)", min_val=0.1)
        elif mode == 2:
            sf = self.validator.get_float("Enter specific heat of component of which mass has to be found (J/kg·K)", min_val=0.1)
            dtf = self.validator.get_float("Enter change in temperature of component of which mass has to be found (°C)")
            s1 = self.validator.get_float("Enter specific heat of component 1 (J/kg·K)", min_val=0.1)
            s2 = self.validator.get_float("Enter specific heat of component 2 (J/kg·K)", min_val=0.1)
        else:
            mf = self.validator.get_float("Enter mass of component of which change in temperature has to be found in kg", min_val=0.0001)
            sf = self.validator.get_float("Enter specific heat of component of which change in temperature has to be found (J/kg·K)", min_val=0.1)
            s1 = self.validator.get_float("Enter specific heat of component 1 (J/kg·K)", min_val=0.1)
            s2 = self.validator.get_float("Enter specific heat of component 2 (J/kg·K)", min_val=0.1)

        res = exp.calculate(mode=mode, m1=m1, s1=s1, dt1=dt1, m2=m2, s2=s2, dt2=dt2, mf=mf, sf=sf, dtf=dtf)
        if not res.success:
            print(f"Error: {res.error_message}")
            return

        print(f"\nThe {res.get('target_type')} of the component is: {res.get('calculated_value')}")

        if self.validator.get_yes_no("Do you want to store the data for this experiment?"):
            row = exp.format_csv_row(res.data, res)
            if self.repo.save_record(exp.file_name, exp.headers, row):
                print(f"✓ Data successfully saved to '{exp.file_name}'.")

    def handle_friction(self):
        print("\n--- [ Task 7: Coefficient of Friction Calculation ] ---")
        exp = get_experiment(7)
        mass = self.validator.get_float("Enter mass by which testing was done (in kg)", min_val=0.001)
        max_f = self.validator.get_float("Enter maximum force by which mass was stationary (in N)", min_val=0.001)
        g = self.validator.get_float("Enter the value of gravitational acceleration (in m/s²)", min_val=0.1, default=STANDARD_G)
        e_mass = self.validator.get_float("Enter error in calculation of mass (in kg)", min_val=0.0)
        e_max_f = self.validator.get_float("Enter error in calculation of force (in N)", min_val=0.0)

        res = exp.calculate(mass=mass, max_f=max_f, g=g, e_mass=e_mass, e_max_f=e_max_f)
        if not res.success:
            print(f"Error: {res.error_message}")
            return

        print(f"\nThe coefficient of friction is: {res.get('coeff_friction')}")
        print(f"The error in coefficient friction is: {res.get('error_coeff')} ({res.get('error_percentage')} %)")
        for w in res.warnings:
            print(f"  [Warning] {w}")

        if self.validator.get_yes_no("Do you want to store the data for this experiment?"):
            row = exp.format_csv_row(res.data, res)
            if self.repo.save_record(exp.file_name, exp.headers, row):
                print(f"✓ Data successfully saved to '{exp.file_name}'.")

    def handle_youngs_modulus(self):
        print("\n--- [ Task 8: Young's Modulus Experiment ] ---")
        exp = get_experiment(8)
        m = self.validator.get_float("Enter mass of test weight (in kg)", min_val=0.001)
        g = self.validator.get_float("Enter value of gravitational acceleration (in m/s²)", min_val=0.1, default=STANDARD_G)
        L = self.validator.get_float("Enter length of wire (in meters)", min_val=0.01)
        rw = self.validator.get_float("Enter radius of wire (in meters)", min_val=0.000001)
        dl = self.validator.get_float("Enter change in length of wire (in meters)", min_val=0.0000001)

        res = exp.calculate(M=m, g=g, L=L, rw=rw, dl=dl)
        if not res.success:
            print(f"Error: {res.error_message}")
            return

        print(f"\nYoung's modulus for this wire is: {res.get('youngs_modulus')} N/m² ({res.get('youngs_modulus_scientific')} N/m²)")
        print(f"Applied Stress: {res.get('stress')} N/m² | Longitudinal Strain: {res.get('strain')}")
        for w in res.warnings:
            print(f"  [Warning] {w}")

        if self.validator.get_yes_no("Do you want to store the data for this experiment?"):
            row = exp.format_csv_row(res.data, res)
            if self.repo.save_record(exp.file_name, exp.headers, row):
                print(f"✓ Data successfully saved to '{exp.file_name}'.")

    def handle_metre_bridge(self):
        print("\n--- [ Task 9: Meter Bridge Experiment ] ---")
        exp = get_experiment(9)
        R = self.validator.get_float("Enter value of resistance known (in ohms)", min_val=0.001)
        l1 = self.validator.get_float("Enter length of first segment of wire on side of known resistance (in cm)", min_val=0.1)
        l2 = self.validator.get_float("Enter length of second segment of wire on side of unknown resistance (in cm)", min_val=0.1)
        error_in_R = self.validator.get_float("Enter error in value of resistance (in ohms)", min_val=0.0)
        lc = self.validator.get_float("Enter least count of instrument used to measure length of wire (in cm)", min_val=0.0, default=0.1)

        res = exp.calculate(R=R, l1=l1, l2=l2, error_in_R=error_in_R, lc=lc)
        if not res.success:
            print(f"Error: {res.error_message}")
            return

        print(f"\nValue of unknown resistance X = {res.get('unknown_resistance')} ohms")
        print(f"Error in resistance dx = ±{res.get('absolute_error')} ohms ({res.get('error_percentage')} %)")
        for w in res.warnings:
            print(f"  [Warning] {w}")

        if self.validator.get_yes_no("Do you want to store the data for this experiment?"):
            row = exp.format_csv_row(res.data, res)
            if self.repo.save_record(exp.file_name, exp.headers, row):
                print(f"✓ Data successfully saved to '{exp.file_name}'.")

    def handle_viscosity(self):
        print("\n--- [ Task 10: Coefficient of Viscosity ] ---")
        exp = get_experiment(10)
        rsph = self.validator.get_float("Enter radius of sphere (in meters)", min_val=0.0001)
        rves = self.validator.get_float("Enter radius of vessel (in meters)", min_val=rsph * 1.05)
        g = self.validator.get_float("Enter value of gravitational acceleration (in m/s²)", min_val=0.1, default=STANDARD_G)
        dsph = self.validator.get_float("Enter density of sphere (in kg/m³)", min_val=1.0)
        dliq = self.validator.get_float("Enter density of liquid (in kg/m³)", min_val=1.0, max_val=dsph - 0.1)
        vt = self.validator.get_float("Enter terminal velocity of sphere (in m/s)", min_val=0.0001)

        res = exp.calculate(rsph=rsph, rves=rves, g=g, dsph=dsph, dliq=dliq, vt=vt)
        if not res.success:
            print(f"Error: {res.error_message}")
            return

        print(f"\nCoefficient of viscosity (eta): {res.get('coeff_viscosity')} Pa·s (N·s/m²)")
        print(f"Ladenburg wall correction factor: {res.get('wall_correction_factor')}")

        if self.validator.get_yes_no("Do you want to store the data for this experiment?"):
            row = exp.format_csv_row(res.data, res)
            if self.repo.save_record(exp.file_name, exp.headers, row):
                print(f"✓ Data successfully saved to '{exp.file_name}'.")

    # -------------------------------------------------------------------------
    # Data Retrieval (Task 11)
    # -------------------------------------------------------------------------

    def handle_retrieval(self):
        print("\n--- [ Task 11: Retrieve Experiment Records ] ---")
        print("Which experiment's data do you want to retrieve (enter index number):")
        for i in range(1, 11):
            print(f"  {i}. {EXPERIMENTS[i]['name']}")

        choice = self.validator.get_int("Enter experiment number (1-10)", min_val=1, max_val=10)
        exp = get_experiment(choice)
        if not exp:
            print("Invalid experiment selection.")
            return

        success, headers, rows, msg = self.repo.retrieve_records(exp.file_name)
        if not success:
            print(f"\n[!] {msg}")
            return

        print("\n" + format_table(headers, rows, title=f"Records for {exp.name}"))
        stats_text = format_statistics(headers, rows)
        if stats_text:
            print(stats_text)
