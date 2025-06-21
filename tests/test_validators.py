"""
Unit Tests for Physical Domain Validation
CBSE Class XII Computer Science (Subject Code 083) Project
"""

import unittest
from src.core.factory import get_experiment


class TestValidators(unittest.TestCase):
    """Verifies that impossible physical conditions are caught by validators."""

    def test_pendulum_validators(self):
        exp = get_experiment(1)
        # Error in length cannot be greater than length
        val, msg = exp.validate_inputs(length=0.5, length_error=0.6, num_oscillations=20, time=40.0, time_error=0.1)
        self.assertFalse(val)

    def test_potentiometer_validators(self):
        exp = get_experiment(2)
        # Balance length cannot exceed wire length
        val, msg = exp.validate_inputs(emf=4.0, wire_length=2.0, error_wire_length=0.01,
                                       balance_length=2.5, error_balance_length=0.01)
        self.assertFalse(val)

    def test_galvanometer_validators(self):
        exp = get_experiment(3)
        # Target current must exceed galvanometer current
        val, msg = exp.validate_inputs(G=50.0, ig=0.002, mode=1, i_target=0.001)
        self.assertFalse(val)

    def test_sound_validators(self):
        exp = get_experiment(5)
        # 2nd resonance column must be longer than 1st
        val, msg = exp.validate_inputs(frequency=512.0, l1=25.0, l2=20.0)
        self.assertFalse(val)

    def test_viscosity_validators(self):
        exp = get_experiment(10)
        # Sphere cannot be wider than vessel
        val, msg = exp.validate_inputs(rsph=0.03, rves=0.02, g=9.8, dsph=7800.0, dliq=1260.0, vt=0.1)
        self.assertFalse(val)


if __name__ == "__main__":
    unittest.main()
