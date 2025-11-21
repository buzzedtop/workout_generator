"""
Muscle group definitions and activation levels for workout visualization.
"""

from enum import Enum
from typing import Tuple, List


class ActivationLevel(Enum):
    """Muscle activation levels from 0 (none) to 100 (maximum)."""
    NONE = 0
    LOW = 25
    MEDIUM = 50
    HIGH = 75
    MAXIMUM = 100


class MuscleGroup(Enum):
    """Major muscle groups that can be visualized."""
    # Upper body
    CHEST = "chest"
    SHOULDERS = "shoulders"
    BICEPS = "biceps"
    TRICEPS = "triceps"
    FOREARMS = "forearms"
    UPPER_BACK = "upper_back"
    LATS = "lats"
    ABS = "abs"
    OBLIQUES = "obliques"
    
    # Lower body
    QUADS = "quads"
    HAMSTRINGS = "hamstrings"
    GLUTES = "glutes"
    CALVES = "calves"
    HIP_FLEXORS = "hip_flexors"


class MuscleDefinition:
    """Defines the anatomical position and shape of a muscle group."""
    
    def __init__(
        self,
        name: str,
        muscle_group: MuscleGroup,
        polygon_points: List[Tuple[float, float]],
        side: str = "both"  # "left", "right", or "both"
    ):
        """
        Initialize a muscle definition.
        
        Args:
            name: Display name of the muscle
            muscle_group: The muscle group this belongs to
            polygon_points: List of (x, y) coordinates defining the muscle shape (0-1 normalized)
            side: Which side of the body ("left", "right", or "both")
        """
        self.name = name
        self.muscle_group = muscle_group
        self.polygon_points = polygon_points
        self.side = side


# Define muscle shapes as normalized coordinates (0-1 scale)
# These will be scaled to the actual figure size
MUSCLE_DEFINITIONS = {
    # Front view muscles
    MuscleGroup.CHEST: [
        MuscleDefinition(
            "Left Pectoral",
            MuscleGroup.CHEST,
            [(0.4, 0.22), (0.45, 0.22), (0.48, 0.28), (0.42, 0.32), (0.38, 0.28)],
            "left"
        ),
        MuscleDefinition(
            "Right Pectoral",
            MuscleGroup.CHEST,
            [(0.6, 0.22), (0.55, 0.22), (0.52, 0.28), (0.58, 0.32), (0.62, 0.28)],
            "right"
        ),
    ],
    MuscleGroup.BICEPS: [
        MuscleDefinition(
            "Left Bicep",
            MuscleGroup.BICEPS,
            [(0.32, 0.28), (0.35, 0.28), (0.36, 0.38), (0.32, 0.38)],
            "left"
        ),
        MuscleDefinition(
            "Right Bicep",
            MuscleGroup.BICEPS,
            [(0.68, 0.28), (0.65, 0.28), (0.64, 0.38), (0.68, 0.38)],
            "right"
        ),
    ],
    MuscleGroup.FOREARMS: [
        MuscleDefinition(
            "Left Forearm",
            MuscleGroup.FOREARMS,
            [(0.30, 0.40), (0.33, 0.40), (0.33, 0.52), (0.30, 0.52)],
            "left"
        ),
        MuscleDefinition(
            "Right Forearm",
            MuscleGroup.FOREARMS,
            [(0.70, 0.40), (0.67, 0.40), (0.67, 0.52), (0.70, 0.52)],
            "right"
        ),
    ],
    MuscleGroup.SHOULDERS: [
        MuscleDefinition(
            "Left Deltoid",
            MuscleGroup.SHOULDERS,
            [(0.35, 0.20), (0.38, 0.22), (0.36, 0.28), (0.32, 0.26)],
            "left"
        ),
        MuscleDefinition(
            "Right Deltoid",
            MuscleGroup.SHOULDERS,
            [(0.65, 0.20), (0.62, 0.22), (0.64, 0.28), (0.68, 0.26)],
            "right"
        ),
    ],
    MuscleGroup.ABS: [
        MuscleDefinition(
            "Rectus Abdominis",
            MuscleGroup.ABS,
            [(0.45, 0.35), (0.55, 0.35), (0.54, 0.50), (0.46, 0.50)],
            "both"
        ),
    ],
    MuscleGroup.OBLIQUES: [
        MuscleDefinition(
            "Left Oblique",
            MuscleGroup.OBLIQUES,
            [(0.42, 0.38), (0.45, 0.38), (0.44, 0.48), (0.40, 0.48)],
            "left"
        ),
        MuscleDefinition(
            "Right Oblique",
            MuscleGroup.OBLIQUES,
            [(0.58, 0.38), (0.55, 0.38), (0.56, 0.48), (0.60, 0.48)],
            "right"
        ),
    ],
    MuscleGroup.QUADS: [
        MuscleDefinition(
            "Left Quadriceps",
            MuscleGroup.QUADS,
            [(0.42, 0.54), (0.47, 0.54), (0.47, 0.75), (0.42, 0.75)],
            "left"
        ),
        MuscleDefinition(
            "Right Quadriceps",
            MuscleGroup.QUADS,
            [(0.58, 0.54), (0.53, 0.54), (0.53, 0.75), (0.58, 0.75)],
            "right"
        ),
    ],
    MuscleGroup.CALVES: [
        MuscleDefinition(
            "Left Calf",
            MuscleGroup.CALVES,
            [(0.43, 0.77), (0.46, 0.77), (0.45, 0.90), (0.43, 0.90)],
            "left"
        ),
        MuscleDefinition(
            "Right Calf",
            MuscleGroup.CALVES,
            [(0.57, 0.77), (0.54, 0.77), (0.55, 0.90), (0.57, 0.90)],
            "right"
        ),
    ],
    MuscleGroup.HIP_FLEXORS: [
        MuscleDefinition(
            "Left Hip Flexor",
            MuscleGroup.HIP_FLEXORS,
            [(0.44, 0.50), (0.47, 0.50), (0.47, 0.54), (0.44, 0.54)],
            "left"
        ),
        MuscleDefinition(
            "Right Hip Flexor",
            MuscleGroup.HIP_FLEXORS,
            [(0.56, 0.50), (0.53, 0.50), (0.53, 0.54), (0.56, 0.54)],
            "right"
        ),
    ],
}


def get_activation_color(activation: float) -> Tuple[int, int, int]:
    """
    Get RGB color based on activation level (0-100).
    
    Blue (0,0,255) at 0% activation -> Red (255,0,0) at 100% activation
    
    Args:
        activation: Activation level from 0 to 100
        
    Returns:
        RGB tuple (r, g, b) with values 0-255
    """
    activation = max(0, min(100, activation))  # Clamp to 0-100
    
    # Interpolate between blue and red
    red = int(255 * (activation / 100))
    blue = int(255 * (1 - activation / 100))
    green = 0
    
    return (red, green, blue)
