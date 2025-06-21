"""
Unit Tests for All 10 Physics Experiments
CBSE Class XII Computer Science (Subject Code 083) Project
"""

import unittest
import math
from src.core.factory import get_experiment, get_all_experiments
from src.core.pendulum import PendulumExperiment
from src.core.potentiometer import PotentiometerExperiment
from src.core.galvanometer import GalvanometerConversionExperiment
from src.core.optics import ConvexLensDisplacementExperiment
from src.core.sound import ResonanceTubeExperiment
from src.core.calorimetry import CalorimetryExperiment
from src.core.mechanics import FrictionExperiment, YoungsModulusExperiment
from src.core.electricity import MetreBridgeExperiment
from src.core.fluids import ViscosityExperiment


class TestPhysicsExperiments(unittest.TestCase):
    """Verifies calculation accuracy, physical boundaries, and error handling."""

    def test_factory_lookup(self):
        """Verify that all 10 experiments are indexed and loadable."""
        for i in range(1, 11):
            exp = get_experiment(i)
            self.assertIsNotNone(exp, f"Experiment {i} should be loadable.")
            self.assertEqual(exp.exp_id, i)
        self.assertIsNone(get_experiment(11))
        self.assertEqual(len(get_all_experiments()), 10)

    # 1. Pendulum
    def test_pendulum_calculation(self):
        exp = PendulumExperiment()
        # L = 1.0m, 20 oscillations in 40.1s -> T = 2.005s -> g ~ 9.8087
        res = exp.calculate(length=1.0, length_error=0.001, num_oscillations=20, time=40.1, time_error=0.2)
        self.assertTrue(res.success)
        self.assertAlmostEqual(res.get("g"), 9.8204, places=2)
        self.assertGreater(res.get("error_percentage"), 0)

        # Invalid: negative length
        bad_res = exp.calculate(length=-1.0, length_error=0.001, num_oscillations=20, time=40.0, time_error=0.2)
        self.assertFalse(bad_res.success)

    # 2. Potentiometer
    def test_potentiometer_calculation(self):
        exp = PotentiometerExperiment()
        # EMF = 4.0V, wire = 2.0m, balance = 1.2m -> V = 2.4V
        res = exp.calculate(emf=4.0, wire_length=2.0, error_wire_length=0.01,
                            balance_length=1.2, error_balance_length=0.01)
        self.assertTrue(res.success)
        self.assertAlmostEqual(res.get("voltage"), 2.4, places=2)
        self.assertAlmostEqual(res.get("potential_gradient"), 2.0, places=2)

        # Invalid: balance length > wire length
        bad = exp.calculate(emf=4.0, wire_length=2.0, error_wire_length=0.01,
                            balance_length=2.5, error_balance_length=0.01)
        self.assertFalse(bad.success)

    # 3. Galvanometer
    def test_galvanometer_conversion(self):
        exp = GalvanometerConversionExperiment()
        # G = 50 ohm, Ig = 0.002 A, Ammeter I = 3.0 A -> S = (0.002 * 50) / (3 - 0.002) = 0.1 / 2.998 ~ 0.033356
        # Voltmeter V = 10 V -> R = (10 / 0.002) - 50 = 5000 - 50 = 4950
        res = exp.calculate(G=50.0, ig=0.002, mode=3, i_target=3.0, v_target=10.0)
        self.assertTrue(res.success)
        self.assertAlmostEqual(res.get("r_shunt"), 0.033356, places=4)
        self.assertAlmostEqual(res.get("r_series"), 4950.0, places=1)

        # Invalid: target current <= ig
        bad = exp.calculate(G=50.0, ig=0.002, mode=1, i_target=0.001)
        self.assertFalse(bad.success)

    # 4. Optics (Lens Displacement)
    def test_optics_displacement(self):
        exp = ConvexLensDisplacementExperiment()
        # D = 100 cm, x = 20 cm -> f = (10000 - 400) / 400 = 9600 / 400 = 24.0 cm
        res = exp.calculate(D=100.0, x=20.0)
        self.assertTrue(res.success)
        self.assertEqual(res.get("focal_length"), 24.0)

        # Invalid: x >= D
        bad = exp.calculate(D=50.0, x=60.0)
        self.assertFalse(bad.success)

    # 5. Sound (Resonance Tube)
    def test_resonance_sound(self):
        exp = ResonanceTubeExperiment()
        # f = 512 Hz, l1 = 16.0 cm, l2 = 49.0 cm -> v = 2 * 512 * 33 = 33792 cm/s = 337.92 m/s
        # e = (49 - 48) / 2 = 0.5 cm
        res = exp.calculate(frequency=512.0, l1=16.0, l2=49.0)
        self.assertTrue(res.success)
        self.assertEqual(res.get("velocity_cm_s"), 33792.0)
        self.assertEqual(res.get("velocity_m_s"), 337.92)
        self.assertEqual(res.get("end_correction"), 0.5)

        # Invalid: l2 <= l1
        bad = exp.calculate(frequency=512.0, l1=30.0, l2=20.0)
        self.assertFalse(bad.success)

    # 6. Calorimetry
    def test_calorimetry(self):
        exp = CalorimetryExperiment()
        # Mode 1: specific heat
        # m1=3, s1=5, dt1=10 -> 150
        # m2=2, s2=8, dt2=15 -> 240
        # sum = 390
        # mf=4, dtf=20 -> denominator = 80
        # sf = 390 / 80 = 4.875
        res = exp.calculate(mode=1, m1=3.0, s1=5.0, dt1=10.0, m2=2.0, s2=8.0, dt2=15.0, mf=4.0, dtf=20.0)
        self.assertTrue(res.success)
        self.assertAlmostEqual(res.get("calculated_value"), 4.875, places=3)

    # 7. Friction
    def test_friction(self):
        exp = FrictionExperiment()
        # mass = 0.5 kg, max_f = 1.47 N, g = 9.8 -> mu = 1.47 / 4.9 = 0.30
        res = exp.calculate(mass=0.5, max_f=1.47, g=9.8, e_mass=0.005, e_max_f=0.02)
        self.assertTrue(res.success)
        self.assertAlmostEqual(res.get("coeff_friction"), 0.30, places=2)

    # 8. Young's Modulus
    def test_youngs_modulus(self):
        exp = YoungsModulusExperiment()
        # M = 2.0 kg, g = 9.8, L = 2.5 m, rw = 0.00025 m, dl = 0.0012 m
        # A = pi * (2.5e-4)^2 ~ 1.9635e-7
        # Y = (2 * 9.8 * 2.5) / (A * 0.0012) ~ 49 / (2.356e-10) ~ 2.079e11
        res = exp.calculate(M=2.0, g=9.8, L=2.5, rw=0.00025, dl=0.0012)
        self.assertTrue(res.success)
        self.assertAlmostEqual(res.get("youngs_modulus") / 1e11, 2.08, places=1)

    # 9. Metre Bridge
    def test_metre_bridge(self):
        exp = MetreBridgeExperiment()
        # R = 10 ohm, l1 = 48.5, l2 = 51.5 -> X = (48.5 / 51.5) * 10 ~ 9.4175
        res = exp.calculate(R=10.0, l1=48.5, l2=51.5, error_in_R=0.05, lc=0.1)
        self.assertTrue(res.success)
        self.assertAlmostEqual(res.get("unknown_resistance"), 9.4175, places=2)
        self.assertGreater(res.get("absolute_error"), 0)

    # 10. Viscosity
    def test_viscosity(self):
        exp = ViscosityExperiment()
        # rsph = 0.003, rves = 0.025, g = 9.8, dsph = 7800, dliq = 1260, vt = 0.15
        res = exp.calculate(rsph=0.003, rves=0.025, g=9.8, dsph=7800.0, dliq=1260.0, vt=0.15)
        self.assertTrue(res.success)
        self.assertGreater(res.get("coeff_viscosity"), 0)
        self.assertAlmostEqual(res.get("wall_correction_factor"), 1.0 + 2.4 * (0.003 / 0.025), places=3)


if __name__ == "__main__":
    unittest.main()
