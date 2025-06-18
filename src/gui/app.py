"""
Tkinter Graphical User Interface for Physics Experiment Helper
CBSE Class XII Computer Science (Subject Code 083) Project
"""

import tkinter as tk
from tkinter import ttk, messagebox
from typing import Dict, List, Optional
from src.config import EXPERIMENTS, STANDARD_G
from src.core.factory import get_experiment
from src.storage.csv_handler import CSVRepository


class PhysicsGUIApp:
    """Modern Desktop GUI for calculating and managing physics practical experiments."""

    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Physics Experiment Helper - CBSE Class XII (083)")
        self.root.geometry("980x720")
        self.root.minsize(850, 600)

        self.repo = CSVRepository()
        self.current_exp_id = 1
        self.current_result = None
        self.input_entries: Dict[str, ttk.Entry] = {}

        self._setup_styles()
        self._build_ui()
        self._load_experiment_form(1)

    def _setup_styles(self):
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Header.TLabel", font=("Helvetica", 15, "bold"), foreground="#1a365d")
        style.configure("Subheader.TLabel", font=("Helvetica", 11, "bold"), foreground="#2d3748")
        style.configure("Formula.TLabel", font=("Courier", 10, "italic"), foreground="#2b6cb0")
        style.configure("Accent.TButton", font=("Helvetica", 10, "bold"), background="#3182ce", foreground="white")

    def _build_ui(self):
        notebook = ttk.Notebook(self.root)
        notebook.pack(fill=tk.BOTH, expand=True, padx=12, pady=12)

        # Tab 1: Experiment Calculator
        self.calc_tab = ttk.Frame(notebook)
        notebook.add(self.calc_tab, text="  🧪 Perform Experiment  ")

        # Tab 2: Database Viewer
        self.data_tab = ttk.Frame(notebook)
        notebook.add(self.data_tab, text="  📊 View Stored Records  ")

        self._build_calc_tab()
        self._build_data_tab()

    def _build_calc_tab(self):
        # Top Selector Frame
        selector_frame = ttk.LabelFrame(self.calc_tab, text=" Select Physics Experiment ", padding=10)
        selector_frame.pack(fill=tk.X, padx=10, pady=5)

        ttk.Label(selector_frame, text="Experiment:", font=("Helvetica", 10, "bold")).pack(side=tk.LEFT, padx=5)

        exp_names = [f"{i}. {EXPERIMENTS[i]['name']}" for i in range(1, 11)]
        self.exp_combo = ttk.Combobox(selector_frame, values=exp_names, state="readonly", width=65)
        self.exp_combo.current(0)
        self.exp_combo.pack(side=tk.LEFT, padx=10, fill=tk.X, expand=True)
        self.exp_combo.bind("<<ComboboxSelected>>", self._on_experiment_change)

        # Content split: Left = Inputs, Right = Results & Theory
        content_pane = ttk.PanedWindow(self.calc_tab, orient=tk.HORIZONTAL)
        content_pane.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        # Left: Inputs Frame
        self.inputs_frame = ttk.LabelFrame(content_pane, text=" Input Parameters ", padding=12)
        content_pane.add(self.inputs_frame, weight=1)

        # Right: Output Frame
        self.results_frame = ttk.LabelFrame(content_pane, text=" Calculated Results & Physics Insights ", padding=12)
        content_pane.add(self.results_frame, weight=1)

        self._build_results_panel()

    def _build_results_panel(self):
        self.formula_label = ttk.Label(self.results_frame, text="", style="Formula.TLabel", wraplength=400)
        self.formula_label.pack(anchor=tk.W, pady=5)

        self.res_text = tk.Text(self.results_frame, height=14, wrap=tk.WORD, font=("Courier", 10), state=tk.DISABLED)
        self.res_text.pack(fill=tk.BOTH, expand=True, pady=8)

        btn_box = ttk.Frame(self.results_frame)
        btn_box.pack(fill=tk.X, pady=5)

        self.save_btn = ttk.Button(btn_box, text="💾 Save to Database (CSV)", command=self._save_current_result, state=tk.DISABLED)
        self.save_btn.pack(side=tk.RIGHT, padx=5)

    def _on_experiment_change(self, event=None):
        idx = self.exp_combo.current() + 1
        self._load_experiment_form(idx)

    def _load_experiment_form(self, exp_id: int):
        self.current_exp_id = exp_id
        self.current_result = None
        self.save_btn.config(state=tk.DISABLED)
        self._clear_results_display()

        # Clear old input widgets
        for widget in self.inputs_frame.winfo_children():
            widget.destroy()

        self.input_entries.clear()

        # Build dynamic fields based on exp_id
        exp_meta = EXPERIMENTS[exp_id]
        ttk.Label(self.inputs_frame, text=exp_meta["name"], style="Subheader.TLabel", wraplength=380).pack(anchor=tk.W, pady=(0, 10))

        if exp_id == 1:
            self._add_field("length", "Pendulum Length (L in meters):", "0.992")
            self._add_field("length_error", "Error in Length (ΔL in meters):", "0.001")
            self._add_field("num_oscillations", "Number of Oscillations (n):", "20")
            self._add_field("time", "Total Time (t in seconds):", "40.0")
            self._add_field("time_error", "Error in Time (Δt in seconds):", "0.2")
            self.formula_label.config(text="Theory: g = (4π²·L) / (t/n)² | Δg/g = ΔL/L + 2Δt/t")

        elif exp_id == 2:
            self._add_field("emf", "Known EMF (E in Volts):", "4.0")
            self._add_field("wire_length", "Total Wire Length (L in meters):", "2.0")
            self._add_field("error_wire_length", "Error in Wire Length (ΔL in meters):", "0.01")
            self._add_field("balance_length", "Balancing Length (l in meters):", "1.2")
            self._add_field("error_balance_length", "Error in Balance Length (Δl in meters):", "0.01")
            self.formula_label.config(text="Theory: V = E·(l/L) | ΔV = V·(Δl/l + ΔL/L)")

        elif exp_id == 3:
            self._add_field("G", "Galvanometer Resistance (G in Ω):", "50.0")
            self._add_field("ig", "Max Current through Galvanometer (Ig in A):", "0.002")
            self._add_field("mode", "Conversion Mode (1=Ammeter, 2=Voltmeter, 3=Both):", "3")
            self._add_field("i_target", "Ammeter Target Current (I in A):", "3.0")
            self._add_field("v_target", "Voltmeter Target Voltage (V in Volts):", "10.0")
            self.formula_label.config(text="Shunt: S = (Ig·G)/(I - Ig) | Multiplier: R = (V/Ig) - G")

        elif exp_id == 4:
            self._add_field("D", "Distance Object to Screen (D in cm):", "100.0")
            self._add_field("x", "Distance between 2 Lens Positions (x in cm):", "20.0")
            self.formula_label.config(text="Theory: f = (D² - x²) / (4D)")

        elif exp_id == 5:
            self._add_field("frequency", "Tuning Fork Frequency (f in Hz):", "512.0")
            self._add_field("l1", "1st Resonance Air Column Length (l1 in cm):", "16.0")
            self._add_field("l2", "2nd Resonance Air Column Length (l2 in cm):", "49.0")
            self.formula_label.config(text="v = 2f·(l2 - l1) cm/s | End correction: e = (l2 - 3l1)/2 cm")

        elif exp_id == 6:
            self._add_field("mode", "Calculate (1=Specific Heat, 2=Mass, 3=Temp Change):", "1")
            self._add_field("m1", "Mass of component 1 (kg):", "0.2")
            self._add_field("s1", "Specific heat of component 1 (J/kg·K):", "4186.0")
            self._add_field("dt1", "Change in temp of component 1 (°C):", "15.0")
            self._add_field("m2", "Mass of component 2 (kg):", "0.1")
            self._add_field("s2", "Specific heat of component 2 (J/kg·K):", "385.0")
            self._add_field("dt2", "Change in temp of component 2 (°C):", "10.0")
            self._add_field("param_target_1", "Target component Known Mass/SpecHeat (kg or J/kg·K):", "0.15")
            self._add_field("param_target_2", "Target component Known Temp Change (°C):", "25.0")
            self.formula_label.config(text="Principle of Mixtures: m1·s1·ΔT1 + m2·s2·ΔT2 = mf·sf·ΔTf")

        elif exp_id == 7:
            self._add_field("mass", "Testing Mass (m in kg):", "0.5")
            self._add_field("max_f", "Limiting Frictional Force (Fmax in N):", "1.47")
            self._add_field("g", "Gravitational Acceleration (m/s²):", str(STANDARD_G))
            self._add_field("e_mass", "Error in Mass (kg):", "0.005")
            self._add_field("e_max_f", "Error in Force (N):", "0.02")
            self.formula_label.config(text="Theory: μ = Fmax / (m·g) | Δμ = μ·(Δm/m + ΔF/Fmax)")

        elif exp_id == 8:
            self._add_field("M", "Applied Test Mass (M in kg):", "2.0")
            self._add_field("g", "Gravitational Acceleration (m/s²):", str(STANDARD_G))
            self._add_field("L", "Original Length of Wire (L in meters):", "2.5")
            self._add_field("rw", "Radius of Wire (rw in meters):", "0.00025")
            self._add_field("dl", "Extension of Wire (Δl in meters):", "0.0012")
            self.formula_label.config(text="Theory: Y = (M·g·L) / (π·rw²·Δl) N/m²")

        elif exp_id == 9:
            self._add_field("R", "Known Resistance (R in Ω):", "10.0")
            self._add_field("l1", "Length on Side of Known Res (l1 in cm):", "48.5")
            self._add_field("l2", "Length on Side of Unknown Res (l2 in cm):", "51.5")
            self._add_field("error_in_R", "Error in Known Resistance (ΔR in Ω):", "0.05")
            self._add_field("lc", "Instrument Least Count (cm):", "0.1")
            self.formula_label.config(text="Theory: X = R·(l1/l2) | ΔX = X·(lc/l1 + lc/l2 + ΔR/R)")

        elif exp_id == 10:
            self._add_field("rsph", "Radius of Falling Sphere (m):", "0.003")
            self._add_field("rves", "Radius of Cylindrical Vessel (m):", "0.025")
            self._add_field("g", "Gravitational Acceleration (m/s²):", str(STANDARD_G))
            self._add_field("dsph", "Density of Sphere (kg/m³):", "7800.0")
            self._add_field("dliq", "Density of Liquid (kg/m³):", "1260.0")
            self._add_field("vt", "Terminal Velocity (vt in m/s):", "0.15")
            self.formula_label.config(text="Stoke's Law: η = [2·r²·g·(dsph - dliq)] / [9·vt·(1 + 2.4·r/R)]")

        calc_btn = ttk.Button(self.inputs_frame, text="⚡ Calculate Results", style="Accent.TButton", command=self._execute_calculation)
        calc_btn.pack(pady=15, fill=tk.X)

    def _add_field(self, key: str, label_text: str, default_val: str = ""):
        f = ttk.Frame(self.inputs_frame)
        f.pack(fill=tk.X, pady=3)
        ttk.Label(f, text=label_text, width=32, anchor=tk.W).pack(side=tk.LEFT)
        entry = ttk.Entry(f)
        entry.insert(0, default_val)
        entry.pack(side=tk.RIGHT, fill=tk.X, expand=True)
        self.input_entries[key] = entry

    def _execute_calculation(self):
        exp = get_experiment(self.current_exp_id)
        if not exp:
            messagebox.showerror("Error", "Invalid experiment selection.")
            return

        try:
            # Parse inputs according to experiment
            res = None
            if self.current_exp_id == 1:
                res = exp.calculate(
                    length=float(self.input_entries["length"].get()),
                    length_error=float(self.input_entries["length_error"].get()),
                    num_oscillations=int(self.input_entries["num_oscillations"].get()),
                    time=float(self.input_entries["time"].get()),
                    time_error=float(self.input_entries["time_error"].get())
                )
            elif self.current_exp_id == 2:
                res = exp.calculate(
                    emf=float(self.input_entries["emf"].get()),
                    wire_length=float(self.input_entries["wire_length"].get()),
                    error_wire_length=float(self.input_entries["error_wire_length"].get()),
                    balance_length=float(self.input_entries["balance_length"].get()),
                    error_balance_length=float(self.input_entries["error_balance_length"].get())
                )
            elif self.current_exp_id == 3:
                mode = int(self.input_entries["mode"].get())
                res = exp.calculate(
                    G=float(self.input_entries["G"].get()),
                    ig=float(self.input_entries["ig"].get()),
                    mode=mode,
                    i_target=float(self.input_entries["i_target"].get()) if mode in (1, 3) else None,
                    v_target=float(self.input_entries["v_target"].get()) if mode in (2, 3) else None
                )
            elif self.current_exp_id == 4:
                res = exp.calculate(
                    D=float(self.input_entries["D"].get()),
                    x=float(self.input_entries["x"].get())
                )
            elif self.current_exp_id == 5:
                res = exp.calculate(
                    frequency=float(self.input_entries["frequency"].get()),
                    l1=float(self.input_entries["l1"].get()),
                    l2=float(self.input_entries["l2"].get())
                )
            elif self.current_exp_id == 6:
                mode = int(self.input_entries["mode"].get())
                p1 = float(self.input_entries["param_target_1"].get())
                p2 = float(self.input_entries["param_target_2"].get())
                res = exp.calculate(
                    mode=mode,
                    m1=float(self.input_entries["m1"].get()),
                    s1=float(self.input_entries["s1"].get()),
                    dt1=float(self.input_entries["dt1"].get()),
                    m2=float(self.input_entries["m2"].get()),
                    s2=float(self.input_entries["s2"].get()),
                    dt2=float(self.input_entries["dt2"].get()),
                    mf=p1 if mode in (1, 3) else None,
                    sf=p1 if mode == 2 else None,
                    dtf=p2
                )
            elif self.current_exp_id == 7:
                res = exp.calculate(
                    mass=float(self.input_entries["mass"].get()),
                    max_f=float(self.input_entries["max_f"].get()),
                    g=float(self.input_entries["g"].get()),
                    e_mass=float(self.input_entries["e_mass"].get()),
                    e_max_f=float(self.input_entries["e_max_f"].get())
                )
            elif self.current_exp_id == 8:
                res = exp.calculate(
                    M=float(self.input_entries["M"].get()),
                    g=float(self.input_entries["g"].get()),
                    L=float(self.input_entries["L"].get()),
                    rw=float(self.input_entries["rw"].get()),
                    dl=float(self.input_entries["dl"].get())
                )
            elif self.current_exp_id == 9:
                res = exp.calculate(
                    R=float(self.input_entries["R"].get()),
                    l1=float(self.input_entries["l1"].get()),
                    l2=float(self.input_entries["l2"].get()),
                    error_in_R=float(self.input_entries["error_in_R"].get()),
                    lc=float(self.input_entries["lc"].get())
                )
            elif self.current_exp_id == 10:
                res = exp.calculate(
                    rsph=float(self.input_entries["rsph"].get()),
                    rves=float(self.input_entries["rves"].get()),
                    g=float(self.input_entries["g"].get()),
                    dsph=float(self.input_entries["dsph"].get()),
                    dliq=float(self.input_entries["dliq"].get()),
                    vt=float(self.input_entries["vt"].get())
                )

            if res and res.success:
                self.current_result = res
                self._display_results(res)
                self.save_btn.config(state=tk.NORMAL)
            else:
                msg = res.error_message if res else "Calculation failed."
                messagebox.showerror("Validation Error", msg)

        except ValueError as ve:
            messagebox.showerror("Input Error", f"Please check your input values: {ve}")
        except Exception as e:
            messagebox.showerror("Calculation Error", f"Unexpected error: {e}")

    def _display_results(self, res):
        self.res_text.config(state=tk.NORMAL)
        self.res_text.delete("1.0", tk.END)

        self.res_text.insert(tk.END, "✓ CALCULATION SUCCESSFUL\n")
        self.res_text.insert(tk.END, "=" * 45 + "\n\n")

        for k, v in res.data.items():
            self.res_text.insert(tk.END, f"  • {k.replace('_', ' ').capitalize()}: {v}\n")

        if res.warnings:
            self.res_text.insert(tk.END, "\n[Physics Warnings]:\n")
            for w in res.warnings:
                self.res_text.insert(tk.END, f"  ⚠️ {w}\n")

        self.res_text.config(state=tk.DISABLED)

    def _clear_results_display(self):
        self.res_text.config(state=tk.NORMAL)
        self.res_text.delete("1.0", tk.END)
        self.res_text.config(state=tk.DISABLED)

    def _save_current_result(self):
        if not self.current_result:
            return
        exp = get_experiment(self.current_exp_id)
        row = exp.format_csv_row(self.current_result.data, self.current_result)
        if self.repo.save_record(exp.file_name, exp.headers, row):
            messagebox.showinfo("Success", f"Data record successfully saved to {exp.file_name}!")
            self.save_btn.config(state=tk.DISABLED)
        else:
            messagebox.showerror("Error", f"Failed to save record to {exp.file_name}.")

    # -------------------------------------------------------------------------
    # Tab 2: Database Viewer
    # -------------------------------------------------------------------------

    def _build_data_tab(self):
        top_bar = ttk.Frame(self.data_tab, padding=10)
        top_bar.pack(fill=tk.X)

        ttk.Label(top_bar, text="View Records For:", font=("Helvetica", 10, "bold")).pack(side=tk.LEFT, padx=5)
        exp_names = [f"{i}. {EXPERIMENTS[i]['name']}" for i in range(1, 11)]
        self.data_exp_combo = ttk.Combobox(top_bar, values=exp_names, state="readonly", width=55)
        self.data_exp_combo.current(0)
        self.data_exp_combo.pack(side=tk.LEFT, padx=10)

        load_btn = ttk.Button(top_bar, text="🔄 Refresh Table", command=self._load_table_data)
        load_btn.pack(side=tk.LEFT, padx=5)

        # Table with scrollbars
        table_frame = ttk.Frame(self.data_tab, padding=5)
        table_frame.pack(fill=tk.BOTH, expand=True)

        self.tree = ttk.Treeview(table_frame, show="headings", selectmode="browse")
        vsb = ttk.Scrollbar(table_frame, orient="vertical", command=self.tree.yview)
        hsb = ttk.Scrollbar(table_frame, orient="horizontal", command=self.tree.xview)
        self.tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        vsb.pack(side=tk.RIGHT, fill=tk.Y)
        hsb.pack(side=tk.BOTTOM, fill=tk.X)

        # Bottom summary label
        self.summary_label = ttk.Label(self.data_tab, text="", font=("Courier", 9), padding=8)
        self.summary_label.pack(fill=tk.X)

        self._load_table_data()

    def _load_table_data(self):
        idx = self.data_exp_combo.current() + 1
        exp = get_experiment(idx)
        if not exp:
            return

        success, headers, rows, msg = self.repo.retrieve_records(exp.file_name)

        # Reset Treeview
        self.tree.delete(*self.tree.get_children())
        self.tree["columns"] = headers

        for h in headers:
            self.tree.heading(h, text=h)
            self.tree.column(h, width=120, anchor=tk.CENTER)

        if success and rows:
            for row in rows:
                self.tree.insert("", tk.END, values=row)
            self.summary_label.config(text=f"Total Records: {len(rows)} in {exp.file_name}")
        else:
            self.summary_label.config(text=msg)


def launch_gui():
    root = tk.Tk()
    app = PhysicsGUIApp(root)
    root.mainloop()
