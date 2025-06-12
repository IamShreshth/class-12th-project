"""
Experiment Factory and Registry
Provides instantiation and lookup for all 10 Physics Experiments.
CBSE Class XII Computer Science (Subject Code 083) Project
"""

from typing import Dict, List, Optional, Type
from src.core.base import Experiment
from src.core.pendulum import PendulumExperiment
from src.core.potentiometer import PotentiometerExperiment
from src.core.galvanometer import GalvanometerConversionExperiment
from src.core.optics import ConvexLensDisplacementExperiment
from src.core.sound import ResonanceTubeExperiment
from src.core.calorimetry import CalorimetryExperiment
from src.core.mechanics import FrictionExperiment, YoungsModulusExperiment
from src.core.electricity import MetreBridgeExperiment
from src.core.fluids import ViscosityExperiment


EXPERIMENT_CLASSES: Dict[int, Type[Experiment]] = {
    1: PendulumExperiment,
    2: PotentiometerExperiment,
    3: GalvanometerConversionExperiment,
    4: ConvexLensDisplacementExperiment,
    5: ResonanceTubeExperiment,
    6: CalorimetryExperiment,
    7: FrictionExperiment,
    8: YoungsModulusExperiment,
    9: MetreBridgeExperiment,
    10: ViscosityExperiment
}


def get_experiment(exp_id: int) -> Optional[Experiment]:
    """Return an instantiated Experiment object for the given ID (1-10)."""
    cls = EXPERIMENT_CLASSES.get(exp_id)
    if cls:
        return cls()
    return None


def get_all_experiments() -> List[Experiment]:
    """Return instances of all 10 experiments."""
    return [cls() for cls in EXPERIMENT_CLASSES.values()]
