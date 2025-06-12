"""
Experiment 10: Coefficient of Viscosity using Stoke's Method
With Ladenburg's Cylindrical Wall Correction.
CBSE Class XII Computer Science (Subject Code 083) Project
"""

from typing import Any, Dict, List, Optional, Tuple
from src.core.base import Experiment, CalculationResult
from src.config import EXPERIMENTS, STANDARD_G


class ViscosityExperiment(Experiment):
    """Calculates dynamic coefficient of viscosity (eta) using terminal velocity of a falling sphere."""

    def __init__(self):
        meta = EXPERIMENTS[10]
        super().__init__(
            exp_id=10,
            name=meta["name"],
            description="Measure coefficient of viscosity using Stoke's terminal velocity with wall correction.",
            file_name=meta["file_name"],
            headers=meta["headers"]
        )

    def validate_inputs(self, rsph: float, rves: float, g: float,
                        dsph: float, dliq: float, vt: float) -> Tuple[bool, Optional[str]]:
        if rsph <= 0:
            return False, "Radius of sphere must be strictly positive (greater than 0 meters)."
        if rves <= 0:
            return False, "Radius of vessel must be strictly positive (greater than 0 meters)."
        if rsph >= rves:
            return False, f"Sphere radius ({rsph}m) must be strictly smaller than vessel radius ({rves}m)."
        if g <= 0:
            return False, "Gravitational acceleration g must be positive."
        if dsph <= 0 or dliq <= 0:
            return False, "Densities must be strictly positive."
        if dsph <= dliq:
            return False, f"Sphere density ({dsph} kg/m³) must exceed liquid density ({dliq} kg/m³) for sinking terminal velocity."
        if vt <= 0:
            return False, "Terminal velocity vt must be strictly positive (greater than 0 m/s)."
        return True, None

    def calculate(self, rsph: float, rves: float, g: float = STANDARD_G,
                  dsph: float = 0.0, dliq: float = 0.0, vt: float = 0.0) -> CalculationResult:
        try:
            rsph = float(rsph)
            rves = float(rves)
            g = float(g)
            dsph = float(dsph)
            dliq = float(dliq)
            vt = float(vt)

            valid, msg = self.validate_inputs(rsph, rves, g, dsph, dliq, vt)
            if not valid:
                return CalculationResult(success=False, error_message=msg)

            # Ladenburg correction factor: 1 + 2.4 * (rsph / rves)
            wall_correction = 1.0 + (2.4 * (rsph / rves))

            # Stoke's formula: eta = [2 * rsph^2 * g * (dsph - dliq)] / [9 * vt * (1 + 2.4 * rsph / rves)]
            numerator = 2.0 * (rsph ** 2) * g * (dsph - dliq)
            denominator = 9.0 * vt * wall_correction

            coeff_viscosity = numerator / denominator

            return CalculationResult(
                success=True,
                data={
                    "rsph": rsph,
                    "rves": rves,
                    "g": g,
                    "dsph": dsph,
                    "dliq": dliq,
                    "vt": vt,
                    "wall_correction_factor": round(wall_correction, 4),
                    "coeff_viscosity": round(coeff_viscosity, 6)
                }
            )
        except ZeroDivisionError:
            return CalculationResult(success=False, error_message="Division by zero in viscosity calculation.")
        except Exception as e:
            return CalculationResult(success=False, error_message=f"Calculation error: {str(e)}")

    def format_csv_row(self, inputs: Dict[str, Any], result: CalculationResult) -> List[Any]:
        d = result.data
        return [
            d["rsph"],
            d["rves"],
            d["g"],
            d["dsph"],
            d["dliq"],
            d["vt"],
            d["coeff_viscosity"]
        ]
