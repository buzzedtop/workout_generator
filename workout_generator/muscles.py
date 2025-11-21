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
# These are designed to align with the high-fidelity wireframe
MUSCLE_DEFINITIONS = {
    # Front view muscles
    MuscleGroup.CHEST: [
        MuscleDefinition(
            "Left Pectoral",
            MuscleGroup.CHEST,
            [(0.38, 0.20), (0.46, 0.20), (0.44, 0.26), (0.43, 0.28), (0.37, 0.28), (0.36, 0.24)],
            "left"
        ),
        MuscleDefinition(
            "Right Pectoral",
            MuscleGroup.CHEST,
            [(0.62, 0.20), (0.54, 0.20), (0.56, 0.26), (0.57, 0.28), (0.63, 0.28), (0.64, 0.24)],
            "right"
        ),
    ],
    MuscleGroup.BICEPS: [
        MuscleDefinition(
            "Left Bicep",
            MuscleGroup.BICEPS,
            [(0.31, 0.26), (0.34, 0.26), (0.33, 0.35), (0.32, 0.37), (0.29, 0.37), (0.29, 0.30)],
            "left"
        ),
        MuscleDefinition(
            "Right Bicep",
            MuscleGroup.BICEPS,
            [(0.69, 0.26), (0.66, 0.26), (0.67, 0.35), (0.68, 0.37), (0.71, 0.37), (0.71, 0.30)],
            "right"
        ),
    ],
    MuscleGroup.TRICEPS: [
        MuscleDefinition(
            "Left Tricep",
            MuscleGroup.TRICEPS,
            [(0.32, 0.25), (0.35, 0.25), (0.34, 0.32), (0.33, 0.37), (0.30, 0.37), (0.30, 0.30)],
            "left"
        ),
        MuscleDefinition(
            "Right Tricep",
            MuscleGroup.TRICEPS,
            [(0.68, 0.25), (0.65, 0.25), (0.66, 0.32), (0.67, 0.37), (0.70, 0.37), (0.70, 0.30)],
            "right"
        ),
    ],
    MuscleGroup.FOREARMS: [
        MuscleDefinition(
            "Left Forearm",
            MuscleGroup.FOREARMS,
            [(0.28, 0.39), (0.31, 0.39), (0.30, 0.48), (0.29, 0.52), (0.27, 0.52), (0.27, 0.45)],
            "left"
        ),
        MuscleDefinition(
            "Right Forearm",
            MuscleGroup.FOREARMS,
            [(0.72, 0.39), (0.69, 0.39), (0.70, 0.48), (0.71, 0.52), (0.73, 0.52), (0.73, 0.45)],
            "right"
        ),
    ],
    MuscleGroup.SHOULDERS: [
        MuscleDefinition(
            "Left Deltoid",
            MuscleGroup.SHOULDERS,
            [(0.33, 0.18), (0.31, 0.20), (0.30, 0.24), (0.31, 0.26), (0.34, 0.25), (0.35, 0.22)],
            "left"
        ),
        MuscleDefinition(
            "Right Deltoid",
            MuscleGroup.SHOULDERS,
            [(0.67, 0.18), (0.69, 0.20), (0.70, 0.24), (0.69, 0.26), (0.66, 0.25), (0.65, 0.22)],
            "right"
        ),
    ],
    MuscleGroup.ABS: [
        MuscleDefinition(
            "Rectus Abdominis",
            MuscleGroup.ABS,
            [(0.43, 0.29), (0.57, 0.29), (0.57, 0.46), (0.43, 0.46)],
            "both"
        ),
    ],
    MuscleGroup.OBLIQUES: [
        MuscleDefinition(
            "Left Oblique",
            MuscleGroup.OBLIQUES,
            [(0.39, 0.33), (0.42, 0.33), (0.42, 0.46), (0.40, 0.48), (0.38, 0.42)],
            "left"
        ),
        MuscleDefinition(
            "Right Oblique",
            MuscleGroup.OBLIQUES,
            [(0.61, 0.33), (0.58, 0.33), (0.58, 0.46), (0.60, 0.48), (0.62, 0.42)],
            "right"
        ),
    ],
    MuscleGroup.QUADS: [
        MuscleDefinition(
            "Left Quadriceps",
            MuscleGroup.QUADS,
            [(0.41, 0.56), (0.45, 0.56), (0.45, 0.73), (0.41, 0.73)],
            "left"
        ),
        MuscleDefinition(
            "Right Quadriceps",
            MuscleGroup.QUADS,
            [(0.59, 0.56), (0.55, 0.56), (0.55, 0.73), (0.59, 0.73)],
            "right"
        ),
    ],
    MuscleGroup.HAMSTRINGS: [
        MuscleDefinition(
            "Left Hamstring",
            MuscleGroup.HAMSTRINGS,
            [(0.42, 0.56), (0.45, 0.56), (0.45, 0.72), (0.42, 0.72)],
            "left"
        ),
        MuscleDefinition(
            "Right Hamstring",
            MuscleGroup.HAMSTRINGS,
            [(0.58, 0.56), (0.55, 0.56), (0.55, 0.72), (0.58, 0.72)],
            "right"
        ),
    ],
    MuscleGroup.GLUTES: [
        MuscleDefinition(
            "Left Glute",
            MuscleGroup.GLUTES,
            [(0.42, 0.53), (0.45, 0.54), (0.44, 0.58), (0.41, 0.57)],
            "left"
        ),
        MuscleDefinition(
            "Right Glute",
            MuscleGroup.GLUTES,
            [(0.58, 0.53), (0.55, 0.54), (0.56, 0.58), (0.59, 0.57)],
            "right"
        ),
    ],
    MuscleGroup.CALVES: [
        MuscleDefinition(
            "Left Calf",
            MuscleGroup.CALVES,
            [(0.41, 0.74), (0.45, 0.74), (0.45, 0.88), (0.42, 0.90), (0.41, 0.88)],
            "left"
        ),
        MuscleDefinition(
            "Right Calf",
            MuscleGroup.CALVES,
            [(0.59, 0.74), (0.55, 0.74), (0.55, 0.88), (0.58, 0.90), (0.59, 0.88)],
            "right"
        ),
    ],
    MuscleGroup.HIP_FLEXORS: [
        MuscleDefinition(
            "Left Hip Flexor",
            MuscleGroup.HIP_FLEXORS,
            [(0.43, 0.50), (0.45, 0.51), (0.45, 0.55), (0.43, 0.54)],
            "left"
        ),
        MuscleDefinition(
            "Right Hip Flexor",
            MuscleGroup.HIP_FLEXORS,
            [(0.57, 0.50), (0.55, 0.51), (0.55, 0.55), (0.57, 0.54)],
            "right"
        ),
    ],
    MuscleGroup.UPPER_BACK: [
        MuscleDefinition(
            "Upper Back",
            MuscleGroup.UPPER_BACK,
            [(0.40, 0.22), (0.60, 0.22), (0.60, 0.35), (0.40, 0.35)],
            "both"
        ),
    ],
    MuscleGroup.LATS: [
        MuscleDefinition(
            "Left Lat",
            MuscleGroup.LATS,
            [(0.37, 0.28), (0.40, 0.28), (0.41, 0.42), (0.38, 0.44), (0.36, 0.38)],
            "left"
        ),
        MuscleDefinition(
            "Right Lat",
            MuscleGroup.LATS,
            [(0.63, 0.28), (0.60, 0.28), (0.59, 0.42), (0.62, 0.44), (0.64, 0.38)],
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
