"""
Experiment 5: Calculation of Speed of Sound using Resonance Tube
CBSE Class XII Computer Science (Subject Code 083) Project
"""

from typing import Any, Dict, List, Optional, Tuple
from src.core.base import Experiment, CalculationResult
from src.config import EXPERIMENTS


class ResonanceTubeExperiment(Experiment):
    """Calculates speed of sound and end correction using resonance tube."""

    def __init__(self):
        meta = EXPERIMENTS[5]
        super().__init__(
            exp_id=5,
            name=meta["name"],
            description="Measure speed of sound and tube end correction using two resonance positions.",
            file_name=meta["file_name"],
            headers=meta["headers"]
        )

    def validate_inputs(self, frequency: float, l1: float, l2: float) -> Tuple[bool, Optional[str]]:
        if frequency <= 0:
            return False, "Tuning fork frequency must be greater than 0 Hz."
        if l1 <= 0:
            return False, "First resonance length (l1) must be strictly positive (greater than 0 cm)."
        if l2 <= 0:
            return False, "Second resonance length (l2) must be strictly positive (greater than 0 cm)."
        if l2 <= l1:
            return False, f"Second resonance length ({l2} cm) must be greater than first resonance length ({l1} cm)."
        return True, None

    def calculate(self, frequency: float, l1: float, l2: float) -> CalculationResult:
        try:
            frequency = float(frequency)
            l1 = float(l1)
            l2 = float(l2)

            valid, msg = self.validate_inputs(frequency, l1, l2)
            if not valid:
                return CalculationResult(success=False, error_message=msg)

            # v = 2 * f * (l2 - l1) in cm/s
            velocity_cm_s = 2.0 * frequency * (l2 - l1)
            velocity_m_s = velocity_cm_s / 100.0

            # End correction e = (l2 - 3 * l1) / 2
            end_correction = (l2 - 3.0 * l1) / 2.0

            warnings = []
            if velocity_m_s < 300.0 or velocity_m_s > 380.0:
                warnings.append(
                    f"Speed of sound ({velocity_m_s:.2f} m/s) deviates from expected room temperature range (330-350 m/s)."
                )

            return CalculationResult(
                success=True,
                data={
                    "frequency": frequency,
                    "l1": l1,
                    "l2": l2,
                    "velocity_cm_s": round(velocity_cm_s, 2),
                    "velocity_m_s": round(velocity_m_s, 2),
                    "end_correction": round(end_correction, 4)
                },
                warnings=warnings
            )
        except Exception as e:
            return CalculationResult(success=False, error_message=f"Calculation error: {str(e)}")

    def format_csv_row(self, inputs: Dict[str, Any], result: CalculationResult) -> List[Any]:
        d = result.data
        return [
            d["frequency"],
            d["l1"],
            d["l2"],
            d["velocity_cm_s"],
            d["velocity_m_s"],
            d["end_correction"]
        ]
