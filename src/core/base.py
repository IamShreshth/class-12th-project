"""
Base Experiment Definitions and Result Containers
CBSE Class XII Computer Science (Subject Code 083) Project
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Tuple


@dataclass
class CalculationResult:
    """Standardized result envelope for experiment calculations."""
    success: bool
    data: Dict[str, Any] = field(default_factory=dict)
    error_message: Optional[str] = None
    warnings: List[str] = field(default_factory=list)

    def get(self, key: str, default: Any = None) -> Any:
        return self.data.get(key, default)


class Experiment(ABC):
    """Abstract Base Class for all Physics Experiments."""

    def __init__(self, exp_id: int, name: str, description: str, file_name: str, headers: List[str]):
        self.exp_id = exp_id
        self.name = name
        self.description = description
        self.file_name = file_name
        self.headers = headers

    @abstractmethod
    def calculate(self, **kwargs) -> CalculationResult:
        """Execute the mathematical & physics formula calculations."""
        pass

    @abstractmethod
    def validate_inputs(self, **kwargs) -> Tuple[bool, Optional[str]]:
        """Validate whether inputs adhere to physical laws and ranges."""
        pass

    @abstractmethod
    def format_csv_row(self, inputs: Dict[str, Any], result: CalculationResult) -> List[Any]:
        """Convert input and output values to a list matching self.headers."""
        pass

    def __repr__(self) -> str:
        return f"<Experiment {self.exp_id}: {self.name}>"
