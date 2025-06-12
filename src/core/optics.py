"""
Experiment 4: Displacement Method for Focal Length of Convex Lens
CBSE Class XII Computer Science (Subject Code 083) Project
"""

from typing import Any, Dict, List, Optional, Tuple
from src.core.base import Experiment, CalculationResult
from src.config import EXPERIMENTS


class ConvexLensDisplacementExperiment(Experiment):
    """Calculates focal length of a convex lens using the displacement method."""

    def __init__(self):
        meta = EXPERIMENTS[4]
        super().__init__(
            exp_id=4,
            name=meta["name"],
            description="Find focal length of convex lens using two pin displacement method.",
            file_name=meta["file_name"],
            headers=meta["headers"]
        )

    def validate_inputs(self, D: float, x: float) -> Tuple[bool, Optional[str]]:
        if D <= 0:
            return False, "Distance D between object and screen must be strictly positive (greater than 0 cm)."
        if x < 0:
            return False, "Displacement x between lens positions cannot be negative."
        if x >= D:
            return False, f"Displacement x ({x} cm) must be strictly less than screen distance D ({D} cm)."
        return True, None

    def calculate(self, D: float, x: float) -> CalculationResult:
        try:
            D = float(D)
            x = float(x)

            valid, msg = self.validate_inputs(D, x)
            if not valid:
                return CalculationResult(success=False, error_message=msg)

            # Formula: f = (D^2 - x^2) / (4 * D)
            focal_length = (D ** 2 - x ** 2) / (4.0 * D)

            warnings = []
            if D < 4.0 * focal_length:
                warnings.append("Note: For real images on screen, optical condition requires D >= 4f.")

            return CalculationResult(
                success=True,
                data={
                    "D": D,
                    "x": x,
                    "focal_length": round(focal_length, 4)
                },
                warnings=warnings
            )
        except ZeroDivisionError:
            return CalculationResult(success=False, error_message="Division by zero: D is zero.")
        except Exception as e:
            return CalculationResult(success=False, error_message=f"Calculation error: {str(e)}")

    def format_csv_row(self, inputs: Dict[str, Any], result: CalculationResult) -> List[Any]:
        d = result.data
        return [
            d["D"],
            d["x"],
            d["focal_length"]
        ]
