"""
Experiment 2: Potentiometer Experiment
Determination of Potential Difference / EMF Comparison and Error Analysis.
CBSE Class XII Computer Science (Subject Code 083) Project
"""

from typing import Any, Dict, List, Optional, Tuple
from src.core.base import Experiment, CalculationResult
from src.config import EXPERIMENTS


class PotentiometerExperiment(Experiment):
    """Calculates potential difference (Voltage) and propagated error."""

    def __init__(self):
        meta = EXPERIMENTS[2]
        super().__init__(
            exp_id=2,
            name=meta["name"],
            description="Measure voltage and error using potentiometer balance length.",
            file_name=meta["file_name"],
            headers=meta["headers"]
        )

    def validate_inputs(self, emf: float, wire_length: float, error_wire_length: float,
                        balance_length: float, error_balance_length: float) -> Tuple[bool, Optional[str]]:
        if emf <= 0:
            return False, "EMF must be greater than 0 volts."
        if wire_length <= 0:
            return False, "Total wire length must be strictly positive (greater than 0 meters)."
        if balance_length <= 0:
            return False, "Balance length must be strictly positive."
        if balance_length > wire_length:
            return False, f"Balance length ({balance_length}m) cannot exceed total wire length ({wire_length}m)."
        if error_wire_length < 0:
            return False, "Error in wire length cannot be negative."
        if error_balance_length < 0:
            return False, "Error in balance length cannot be negative."
        return True, None

    def calculate(self, emf: float, wire_length: float, error_wire_length: float,
                  balance_length: float, error_balance_length: float) -> CalculationResult:
        try:
            emf = float(emf)
            wire_length = float(wire_length)
            error_wire_length = float(error_wire_length)
            balance_length = float(balance_length)
            error_balance_length = float(error_balance_length)

            valid, msg = self.validate_inputs(emf, wire_length, error_wire_length, balance_length, error_balance_length)
            if not valid:
                return CalculationResult(success=False, error_message=msg)

            potential_gradient = emf / wire_length
            voltage = emf * (balance_length / wire_length)
            fractional_error = (error_balance_length / balance_length) + (error_wire_length / wire_length)
            error_v = voltage * fractional_error
            percentage_error = fractional_error * 100.0

            return CalculationResult(
                success=True,
                data={
                    "emf": emf,
                    "wire_length": wire_length,
                    "error_wire_length": error_wire_length,
                    "balance_length": balance_length,
                    "error_balance_length": error_balance_length,
                    "potential_gradient": round(potential_gradient, 6),
                    "voltage": round(voltage, 4),
                    "error_voltage": round(error_v, 6),
                    "percentage_error": round(percentage_error, 3)
                }
            )
        except ZeroDivisionError:
            return CalculationResult(success=False, error_message="Division by zero: wire length or balance length is zero.")
        except Exception as e:
            return CalculationResult(success=False, error_message=f"Calculation error: {str(e)}")

    def format_csv_row(self, inputs: Dict[str, Any], result: CalculationResult) -> List[Any]:
        d = result.data
        return [
            d["emf"],
            d["wire_length"],
            d["error_wire_length"],
            d["balance_length"],
            d["error_balance_length"],
            d["voltage"],
            d["error_voltage"]
        ]
