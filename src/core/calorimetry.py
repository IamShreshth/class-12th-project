"""
Experiment 6: Calorimetric Calculations (Principle of Mixtures)
CBSE Class XII Computer Science (Subject Code 083) Project
"""

from typing import Any, Dict, List, Optional, Tuple
from src.core.base import Experiment, CalculationResult
from src.config import EXPERIMENTS


class CalorimetryExperiment(Experiment):
    """Calculates specific heat capacity, mass, or temperature change using principle of mixtures."""

    def __init__(self):
        meta = EXPERIMENTS[6]
        super().__init__(
            exp_id=6,
            name=meta["name"],
            description="Calorimetric heat exchange calculations based on Principle of Mixtures.",
            file_name=meta["file_name"],
            headers=meta["headers"]
        )

    def validate_inputs(self, mode: int, m1: float, s1: float, dt1: float,
                        m2: float, s2: float, dt2: float,
                        known_param: float, dt_or_s_or_m: float) -> Tuple[bool, Optional[str]]:
        if mode not in (1, 2, 3):
            return False, "Target calculation mode must be 1 (Specific Heat), 2 (Mass), or 3 (Temperature Change)."
        if m1 <= 0 or m2 <= 0:
            return False, "Component masses m1 and m2 must be strictly positive (greater than 0 kg)."
        if s1 <= 0 or s2 <= 0:
            return False, "Specific heats s1 and s2 must be strictly positive."
        if dt1 == 0 and dt2 == 0:
            return False, "Temperature changes for both components cannot both be zero."
        if known_param <= 0:
            return False, "The known parameter (mass/specific heat) must be strictly positive."
        if dt_or_s_or_m == 0:
            return False, "Denominator component cannot be zero."
        return True, None

    def calculate(self, mode: int, m1: float, s1: float, dt1: float,
                  m2: float, s2: float, dt2: float,
                  mf: Optional[float] = None,
                  sf: Optional[float] = None,
                  dtf: Optional[float] = None) -> CalculationResult:
        try:
            m1 = float(m1)
            s1 = float(s1)
            dt1 = float(dt1)
            m2 = float(m2)
            s2 = float(s2)
            dt2 = float(dt2)

            heat_numerator = (m1 * s1 * dt1) + (m2 * s2 * dt2)

            calc_type = ""
            result_val = 0.0

            if mode == 1:
                # Calculate Specific Heat: sf = numerator / (mf * dtf)
                calc_type = "Specific heat"
                if mf is None or dtf is None:
                    return CalculationResult(success=False, error_message="mf and dtf are required to calculate specific heat.")
                valid, msg = self.validate_inputs(mode, m1, s1, dt1, m2, s2, dt2, mf, dtf)
                if not valid:
                    return CalculationResult(success=False, error_message=msg)
                denominator = mf * dtf
                if denominator == 0:
                    return CalculationResult(success=False, error_message="Division by zero: (mf * dtf) is zero.")
                result_val = heat_numerator / denominator
                sf = result_val

            elif mode == 2:
                # Calculate Mass: mf = numerator / (sf * dtf)
                calc_type = "Mass"
                if sf is None or dtf is None:
                    return CalculationResult(success=False, error_message="sf and dtf are required to calculate mass.")
                valid, msg = self.validate_inputs(mode, m1, s1, dt1, m2, s2, dt2, sf, dtf)
                if not valid:
                    return CalculationResult(success=False, error_message=msg)
                denominator = sf * dtf
                if denominator == 0:
                    return CalculationResult(success=False, error_message="Division by zero: (sf * dtf) is zero.")
                result_val = heat_numerator / denominator
                mf = result_val

            elif mode == 3:
                # Calculate Change in Temperature: dtf = numerator / (mf * sf)
                calc_type = "Change in temperature"
                if mf is None or sf is None:
                    return CalculationResult(success=False, error_message="mf and sf are required to calculate temperature change.")
                valid, msg = self.validate_inputs(mode, m1, s1, dt1, m2, s2, dt2, mf, sf)
                if not valid:
                    return CalculationResult(success=False, error_message=msg)
                denominator = mf * sf
                if denominator == 0:
                    return CalculationResult(success=False, error_message="Division by zero: (mf * sf) is zero.")
                result_val = heat_numerator / denominator
                dtf = result_val

            else:
                return CalculationResult(success=False, error_message="Invalid mode selected.")

            return CalculationResult(
                success=True,
                data={
                    "mode": mode,
                    "target_type": calc_type,
                    "calculated_value": round(result_val, 4),
                    "m1": m1,
                    "m2": m2,
                    "mf": round(mf, 4) if mf is not None else None,
                    "s1": s1,
                    "s2": s2,
                    "sf": round(sf, 4) if sf is not None else None,
                    "dt1": dt1,
                    "dt2": dt2,
                    "dtf": round(dtf, 4) if dtf is not None else None,
                }
            )
        except ZeroDivisionError:
            return CalculationResult(success=False, error_message="Division by zero in calorimetry calculation.")
        except Exception as e:
            return CalculationResult(success=False, error_message=f"Calculation error: {str(e)}")

    def format_csv_row(self, inputs: Dict[str, Any], result: CalculationResult) -> List[Any]:
        d = result.data
        return [
            d["target_type"],
            d["m1"],
            d["m2"],
            d["mf"],
            d["s1"],
            d["s2"],
            d["sf"],
            d["dt1"],
            d["dt2"],
            d["dtf"]
        ]
