"""
Mechanics Experiments:
- Experiment 7: Coefficient of Friction Calculation
- Experiment 8: Young's Modulus of Elasticity (Searle's Apparatus)
CBSE Class XII Computer Science (Subject Code 083) Project
"""

import math
from typing import Any, Dict, List, Optional, Tuple
from src.core.base import Experiment, CalculationResult
from src.config import EXPERIMENTS, STANDARD_G


class FrictionExperiment(Experiment):
    """Calculates coefficient of friction and propagated measurement error."""

    def __init__(self):
        meta = EXPERIMENTS[7]
        super().__init__(
            exp_id=7,
            name=meta["name"],
            description="Determine coefficient of static/limiting friction and propagated error.",
            file_name=meta["file_name"],
            headers=meta["headers"]
        )

    def validate_inputs(self, mass: float, max_f: float, g: float,
                        e_mass: float, e_max_f: float) -> Tuple[bool, Optional[str]]:
        if mass <= 0:
            return False, "Mass must be strictly positive (greater than 0 kg)."
        if max_f <= 0:
            return False, "Frictional force must be strictly positive (greater than 0 N)."
        if g <= 0:
            return False, "Gravitational acceleration g must be positive."
        if e_mass < 0:
            return False, "Error in mass cannot be negative."
        if e_max_f < 0:
            return False, "Error in force cannot be negative."
        if e_mass >= mass:
            return False, "Measurement error in mass cannot equal or exceed measured mass."
        if e_max_f >= max_f:
            return False, "Measurement error in force cannot equal or exceed measured force."
        return True, None

    def calculate(self, mass: float, max_f: float, g: float = STANDARD_G,
                  e_mass: float = 0.0, e_max_f: float = 0.0) -> CalculationResult:
        try:
            mass = float(mass)
            max_f = float(max_f)
            g = float(g)
            e_mass = float(e_mass)
            e_max_f = float(e_max_f)

            valid, msg = self.validate_inputs(mass, max_f, g, e_mass, e_max_f)
            if not valid:
                return CalculationResult(success=False, error_message=msg)

            # Normal reaction N = mass * g
            # mu = max_f / (mass * g)
            coeff = max_f / (mass * g)
            fractional_error = (e_mass / mass) + (e_max_f / max_f)
            e_coeff = fractional_error * coeff
            error_percentage = fractional_error * 100.0

            warnings = []
            if coeff > 1.5:
                warnings.append(f"Unusually high friction coefficient ({coeff:.3f}) for typical solid surfaces.")

            return CalculationResult(
                success=True,
                data={
                    "mass": mass,
                    "max_f": max_f,
                    "g": g,
                    "e_mass": e_mass,
                    "e_max_f": e_max_f,
                    "coeff_friction": round(coeff, 6),
                    "error_coeff": round(e_coeff, 6),
                    "error_percentage": round(error_percentage, 3)
                },
                warnings=warnings
            )
        except ZeroDivisionError:
            return CalculationResult(success=False, error_message="Division by zero in friction calculation.")
        except Exception as e:
            return CalculationResult(success=False, error_message=f"Calculation error: {str(e)}")

    def format_csv_row(self, inputs: Dict[str, Any], result: CalculationResult) -> List[Any]:
        d = result.data
        return [
            d["mass"],
            d["max_f"],
            d["g"],
            d["e_mass"],
            d["e_max_f"],
            d["coeff_friction"],
            d["error_coeff"]
        ]


class YoungsModulusExperiment(Experiment):
    """Calculates Young's Modulus of elasticity of a stretched wire."""

    def __init__(self):
        meta = EXPERIMENTS[8]
        super().__init__(
            exp_id=8,
            name=meta["name"],
            description="Determine Young's modulus of elasticity using wire tension and extension.",
            file_name=meta["file_name"],
            headers=meta["headers"]
        )

    def validate_inputs(self, M: float, g: float, L: float, rw: float, dl: float) -> Tuple[bool, Optional[str]]:
        if M <= 0:
            return False, "Applied mass M must be strictly positive (greater than 0 kg)."
        if g <= 0:
            return False, "Gravitational acceleration g must be positive."
        if L <= 0:
            return False, "Original length of wire L must be strictly positive (greater than 0 meters)."
        if rw <= 0:
            return False, "Radius of wire rw must be strictly positive (greater than 0 meters)."
        if dl <= 0:
            return False, "Extension of wire dl must be strictly positive (greater than 0 meters)."
        if dl >= L:
            return False, "Extension dl cannot be greater than original wire length L."
        return True, None

    def calculate(self, M: float, g: float, L: float, rw: float, dl: float) -> CalculationResult:
        try:
            M = float(M)
            g = float(g)
            L = float(L)
            rw = float(rw)
            dl = float(dl)

            valid, msg = self.validate_inputs(M, g, L, rw, dl)
            if not valid:
                return CalculationResult(success=False, error_message=msg)

            # Area A = pi * rw^2
            area = math.pi * (rw ** 2)
            stress = (M * g) / area
            strain = dl / L

            # Y = (M * g * L) / (pi * rw^2 * dl)
            Y = (M * g * L) / (area * dl)

            warnings = []
            # Typical metals (Copper, Steel, Brass) are in range 5e10 to 2.5e11 N/m^2
            if Y < 1e9 or Y > 1e12:
                warnings.append(f"Young's modulus ({Y:.3e} N/m²) is outside typical engineering metal ranges.")

            return CalculationResult(
                success=True,
                data={
                    "mass": M,
                    "g": g,
                    "length": L,
                    "radius": rw,
                    "extension": dl,
                    "cross_sectional_area": round(area, 10),
                    "stress": round(stress, 4),
                    "strain": round(strain, 8),
                    "youngs_modulus": round(Y, 4),
                    "youngs_modulus_scientific": f"{Y:.4e}"
                },
                warnings=warnings
            )
        except ZeroDivisionError:
            return CalculationResult(success=False, error_message="Division by zero: wire radius or extension is zero.")
        except Exception as e:
            return CalculationResult(success=False, error_message=f"Calculation error: {str(e)}")

    def format_csv_row(self, inputs: Dict[str, Any], result: CalculationResult) -> List[Any]:
        d = result.data
        return [
            d["mass"],
            d["g"],
            d["length"],
            d["radius"],
            d["extension"],
            d["youngs_modulus"]
        ]
