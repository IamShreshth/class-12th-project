"""
Experiment 9: Metre Bridge Experiment (Unknown Resistance & Error Analysis)
Wheatstone Bridge Principle.
CBSE Class XII Computer Science (Subject Code 083) Project
"""

from typing import Any, Dict, List, Optional, Tuple
from src.core.base import Experiment, CalculationResult
from src.config import EXPERIMENTS


class MetreBridgeExperiment(Experiment):
    """Calculates unknown resistance and measurement error using a metre bridge."""

    def __init__(self):
        meta = EXPERIMENTS[9]
        super().__init__(
            exp_id=9,
            name=meta["name"],
            description="Measure unknown resistance using Wheatstone bridge principle with error propagation.",
            file_name=meta["file_name"],
            headers=meta["headers"]
        )

    def validate_inputs(self, R: float, l1: float, l2: float,
                        error_in_R: float, lc: float) -> Tuple[bool, Optional[str]]:
        if R <= 0:
            return False, "Known resistance R must be strictly positive (greater than 0 ohms)."
        if l1 <= 0:
            return False, "Balancing length l1 must be strictly positive (greater than 0 cm)."
        if l2 <= 0:
            return False, "Balancing length l2 must be strictly positive (greater than 0 cm)."
        if error_in_R < 0:
            return False, "Error in resistance cannot be negative."
        if lc < 0:
            return False, "Instrument least count cannot be negative."
        return True, None

    def calculate(self, R: float, l1: float, l2: float,
                  error_in_R: float, lc: float) -> CalculationResult:
        try:
            R = float(R)
            l1 = float(l1)
            l2 = float(l2)
            error_in_R = float(error_in_R)
            lc = float(lc)

            valid, msg = self.validate_inputs(R, l1, l2, error_in_R, lc)
            if not valid:
                return CalculationResult(success=False, error_message=msg)

            # Formula: X = (l1 / l2) * R
            X = (l1 / l2) * R

            # Relative / fractional error
            fractional_error = (lc / l1) + (lc / l2) + (error_in_R / R)
            # Absolute error in ohms: dx = X * fractional_error
            # (Fixing bug in original doc where dx was left as fractional error)
            absolute_error_X = X * fractional_error
            error_percentage = fractional_error * 100.0

            warnings = []
            if abs((l1 + l2) - 100.0) > 2.0:
                warnings.append(f"Sum of segment lengths ({l1 + l2:.2f} cm) deviates from standard 100 cm wire length.")

            return CalculationResult(
                success=True,
                data={
                    "known_resistance": R,
                    "l1": l1,
                    "l2": l2,
                    "error_in_R": error_in_R,
                    "least_count": lc,
                    "unknown_resistance": round(X, 4),
                    "absolute_error": round(absolute_error_X, 4),
                    "fractional_error": round(fractional_error, 6),
                    "error_percentage": round(error_percentage, 3)
                },
                warnings=warnings
            )
        except ZeroDivisionError:
            return CalculationResult(success=False, error_message="Division by zero: l2 or R is zero.")
        except Exception as e:
            return CalculationResult(success=False, error_message=f"Calculation error: {str(e)}")

    def format_csv_row(self, inputs: Dict[str, Any], result: CalculationResult) -> List[Any]:
        d = result.data
        return [
            d["known_resistance"],
            d["l1"],
            d["l2"],
            d["error_in_R"],
            d["least_count"],
            d["unknown_resistance"],
            d["absolute_error"]
        ]
