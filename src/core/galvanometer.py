"""
Experiment 3: Conversion of Galvanometer into Ammeter and Voltmeter
CBSE Class XII Computer Science (Subject Code 083) Project
"""

from typing import Any, Dict, List, Optional, Tuple
from src.core.base import Experiment, CalculationResult
from src.config import EXPERIMENTS


class GalvanometerConversionExperiment(Experiment):
    """Calculates shunt resistance for ammeter and multiplier resistance for voltmeter."""

    def __init__(self):
        meta = EXPERIMENTS[3]
        super().__init__(
            exp_id=3,
            name=meta["name"],
            description="Calculate shunt resistance (ammeter) and series resistance (voltmeter).",
            file_name=meta["file_name"],
            headers=meta["headers"]
        )

    def validate_inputs(self, G: float, ig: float,
                        mode: int,
                        i_target: Optional[float] = None,
                        v_target: Optional[float] = None) -> Tuple[bool, Optional[str]]:
        if G <= 0:
            return False, "Galvanometer resistance must be greater than 0 ohms."
        if ig <= 0:
            return False, "Galvanometer full-scale current (Ig) must be greater than 0 amperes."

        if mode in (1, 3):
            if i_target is None or i_target <= 0:
                return False, "Ammeter target current must be greater than 0 amperes."
            if i_target <= ig:
                return False, f"Target current ({i_target}A) must be strictly greater than galvanometer current Ig ({ig}A)."

        if mode in (2, 3):
            if v_target is None or v_target <= 0:
                return False, "Voltmeter target voltage must be greater than 0 volts."
            galv_voltage_drop = ig * G
            if v_target <= galv_voltage_drop:
                return False, f"Target voltage ({v_target}V) must be greater than intrinsic galvanometer drop ({galv_voltage_drop:.4f}V)."

        return True, None

    def calculate(self, G: float, ig: float, mode: int,
                  i_target: Optional[float] = None,
                  v_target: Optional[float] = None) -> CalculationResult:
        try:
            G = float(G)
            ig = float(ig)
            mode = int(mode)
            if i_target is not None:
                i_target = float(i_target)
            if v_target is not None:
                v_target = float(v_target)

            valid, msg = self.validate_inputs(G, ig, mode, i_target, v_target)
            if not valid:
                return CalculationResult(success=False, error_message=msg)

            r_shunt = None
            r_series = None

            if mode in (1, 3):
                # S = (Ig * G) / (I - Ig)
                r_shunt = (ig * G) / (i_target - ig)

            if mode in (2, 3):
                # R = (V / Ig) - G
                r_series = (v_target / ig) - G

            return CalculationResult(
                success=True,
                data={
                    "galvanometer_resistance": G,
                    "ig": ig,
                    "mode": mode,
                    "target_current": i_target if mode in (1, 3) else None,
                    "target_voltage": v_target if mode in (2, 3) else None,
                    "r_shunt": round(r_shunt, 6) if r_shunt is not None else "NA",
                    "r_series": round(r_series, 6) if r_series is not None else "NA"
                }
            )
        except ZeroDivisionError:
            return CalculationResult(success=False, error_message="Division by zero in resistance calculation.")
        except Exception as e:
            return CalculationResult(success=False, error_message=f"Calculation error: {str(e)}")

    def format_csv_row(self, inputs: Dict[str, Any], result: CalculationResult) -> List[Any]:
        d = result.data
        return [
            d["galvanometer_resistance"],
            d["ig"],
            d["target_current"] if d["target_current"] is not None else "NA",
            d["r_shunt"],
            d["target_voltage"] if d["target_voltage"] is not None else "NA",
            d["r_series"]
        ]
