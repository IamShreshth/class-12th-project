"""
Experiment 1: Determining the Value of Acceleration due to Gravity (g)
Using a Simple Pendulum.
CBSE Class XII Computer Science (Subject Code 083) Project
"""

import math
from typing import Any, Dict, List, Optional, Tuple
from src.core.base import Experiment, CalculationResult
from src.config import EXPERIMENTS


class PendulumExperiment(Experiment):
    """Calculates acceleration due to gravity (g) and percentage error."""

    def __init__(self):
        meta = EXPERIMENTS[1]
        super().__init__(
            exp_id=1,
            name=meta["name"],
            description="Determine g and error using length and oscillation time of a simple pendulum.",
            file_name=meta["file_name"],
            headers=meta["headers"]
        )

    def validate_inputs(self, length: float, length_error: float,
                        num_oscillations: int, time: float, time_error: float) -> Tuple[bool, Optional[str]]:
        if length <= 0:
            return False, "Pendulum length must be strictly positive (greater than 0 meters)."
        if length_error < 0:
            return False, "Error in length cannot be negative."
        if num_oscillations <= 0:
            return False, "Number of oscillations must be a positive integer."
        if time <= 0:
            return False, "Total time must be strictly positive (greater than 0 seconds)."
        if time_error < 0:
            return False, "Error in time cannot be negative."
        if length_error > length:
            return False, "Error in length cannot be greater than the measured length."
        if time_error > time:
            return False, "Error in time cannot be greater than total measured time."
        return True, None

    def calculate(self, length: float, length_error: float,
                  num_oscillations: int, time: float, time_error: float) -> CalculationResult:
        try:
            length = float(length)
            length_error = float(length_error)
            num_oscillations = int(num_oscillations)
            time = float(time)
            time_error = float(time_error)

            valid, msg = self.validate_inputs(length, length_error, num_oscillations, time, time_error)
            if not valid:
                return CalculationResult(success=False, error_message=msg)

            net_time = time / num_oscillations
            # Standard 4 * pi^2 is approximately 39.4784, doc used 39.4384
            # We compute exact 4 * pi^2 and provide compatibility
            pi_sq_4 = 4.0 * (math.pi ** 2)
            g = (pi_sq_4 * length) / (net_time * net_time)
            error_percentage = ((2.0 * time_error / time) + (length_error / length)) * 100.0
            absolute_error = g * (error_percentage / 100.0)

            warnings = []
            if abs(g - 9.8) > 2.0:
                warnings.append(f"Calculated g ({g:.3f} m/s²) deviates noticeably from standard 9.8 m/s².")

            return CalculationResult(
                success=True,
                data={
                    "length": length,
                    "length_error": length_error,
                    "num_oscillations": num_oscillations,
                    "time": time,
                    "time_error": time_error,
                    "net_time": net_time,
                    "g": round(g, 4),
                    "error_percentage": round(error_percentage, 4),
                    "absolute_error": round(absolute_error, 4)
                },
                warnings=warnings
            )
        except ZeroDivisionError:
            return CalculationResult(success=False, error_message="Division by zero encountered in oscillation timing.")
        except Exception as e:
            return CalculationResult(success=False, error_message=f"Calculation error: {str(e)}")

    def format_csv_row(self, inputs: Dict[str, Any], result: CalculationResult) -> List[Any]:
        d = result.data
        return [
            d["length"],
            d["length_error"],
            d["num_oscillations"],
            d["time"],
            d["time_error"],
            d["g"],
            d["error_percentage"]
        ]
