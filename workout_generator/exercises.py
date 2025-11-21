"""
Predefined muscle activation patterns for common bodyweight calisthenics exercises.

This module contains activation data for popular bodyweight exercises, making it easy
to generate workout visualizations without manually specifying muscle activations.
"""

from typing import Dict, List
from .muscles import MuscleGroup


class Exercise:
    """Represents a bodyweight calisthenics exercise with muscle activation data."""
    
    def __init__(
        self,
        name: str,
        muscle_activations: Dict[MuscleGroup, float],
        description: str = "",
        difficulty: str = "intermediate"
    ):
        """
        Initialize an exercise.
        
        Args:
            name: Exercise name
            muscle_activations: Dictionary mapping muscle groups to activation levels (0-100)
            description: Optional description of the exercise
            difficulty: Difficulty level ("beginner", "intermediate", "advanced")
        """
        self.name = name
        self.muscle_activations = muscle_activations
        self.description = description
        self.difficulty = difficulty


# Upper Body Push Exercises
PUSH_UP = Exercise(
    "Push-up",
    {
        MuscleGroup.CHEST: 85,
        MuscleGroup.TRICEPS: 75,
        MuscleGroup.SHOULDERS: 65,
        MuscleGroup.ABS: 55,
    },
    "Classic push-up targeting chest, triceps, and shoulders",
    "beginner"
)

WIDE_PUSH_UP = Exercise(
    "Wide Push-up",
    {
        MuscleGroup.CHEST: 95,
        MuscleGroup.TRICEPS: 60,
        MuscleGroup.SHOULDERS: 70,
        MuscleGroup.ABS: 50,
    },
    "Push-up with wider hand placement, emphasizing chest",
    "beginner"
)

DIAMOND_PUSH_UP = Exercise(
    "Diamond Push-up",
    {
        MuscleGroup.TRICEPS: 95,
        MuscleGroup.CHEST: 70,
        MuscleGroup.SHOULDERS: 60,
        MuscleGroup.ABS: 55,
    },
    "Push-up with hands close together, emphasizing triceps",
    "intermediate"
)

PIKE_PUSH_UP = Exercise(
    "Pike Push-up",
    {
        MuscleGroup.SHOULDERS: 90,
        MuscleGroup.TRICEPS: 65,
        MuscleGroup.CHEST: 45,
        MuscleGroup.ABS: 60,
    },
    "Push-up in pike position, targeting shoulders",
    "intermediate"
)

HANDSTAND_PUSH_UP = Exercise(
    "Handstand Push-up",
    {
        MuscleGroup.SHOULDERS: 100,
        MuscleGroup.TRICEPS: 85,
        MuscleGroup.ABS: 70,
        MuscleGroup.UPPER_BACK: 60,
    },
    "Advanced push-up in handstand position",
    "advanced"
)

DIPS = Exercise(
    "Dips",
    {
        MuscleGroup.TRICEPS: 90,
        MuscleGroup.CHEST: 75,
        MuscleGroup.SHOULDERS: 70,
    },
    "Tricep dips on parallel bars or bench",
    "intermediate"
)

# Upper Body Pull Exercises
PULL_UP = Exercise(
    "Pull-up",
    {
        MuscleGroup.LATS: 95,
        MuscleGroup.BICEPS: 85,
        MuscleGroup.FOREARMS: 75,
        MuscleGroup.UPPER_BACK: 80,
        MuscleGroup.ABS: 50,
    },
    "Classic pull-up with overhand grip",
    "intermediate"
)

CHIN_UP = Exercise(
    "Chin-up",
    {
        MuscleGroup.BICEPS: 95,
        MuscleGroup.LATS: 85,
        MuscleGroup.FOREARMS: 70,
        MuscleGroup.UPPER_BACK: 75,
    },
    "Pull-up with underhand grip, emphasizing biceps",
    "intermediate"
)

AUSTRALIAN_PULL_UP = Exercise(
    "Australian Pull-up",
    {
        MuscleGroup.UPPER_BACK: 85,
        MuscleGroup.LATS: 75,
        MuscleGroup.BICEPS: 70,
        MuscleGroup.FOREARMS: 60,
        MuscleGroup.ABS: 45,
    },
    "Horizontal pull-up (inverted row)",
    "beginner"
)

# Core Exercises
PLANK = Exercise(
    "Plank",
    {
        MuscleGroup.ABS: 90,
        MuscleGroup.OBLIQUES: 70,
        MuscleGroup.SHOULDERS: 60,
        MuscleGroup.QUADS: 50,
    },
    "Isometric core hold in push-up position",
    "beginner"
)

SIDE_PLANK = Exercise(
    "Side Plank",
    {
        MuscleGroup.OBLIQUES: 95,
        MuscleGroup.ABS: 75,
        MuscleGroup.SHOULDERS: 65,
    },
    "Isometric core hold on side",
    "beginner"
)

SIT_UP = Exercise(
    "Sit-up",
    {
        MuscleGroup.ABS: 100,
        MuscleGroup.OBLIQUES: 75,
        MuscleGroup.HIP_FLEXORS: 80,
    },
    "Classic abdominal exercise",
    "beginner"
)

CRUNCH = Exercise(
    "Crunch",
    {
        MuscleGroup.ABS: 95,
        MuscleGroup.OBLIQUES: 60,
    },
    "Partial sit-up targeting upper abs",
    "beginner"
)

BICYCLE_CRUNCH = Exercise(
    "Bicycle Crunch",
    {
        MuscleGroup.ABS: 95,
        MuscleGroup.OBLIQUES: 90,
        MuscleGroup.HIP_FLEXORS: 70,
    },
    "Dynamic crunch with rotation",
    "intermediate"
)

LEG_RAISE = Exercise(
    "Leg Raise",
    {
        MuscleGroup.ABS: 95,
        MuscleGroup.HIP_FLEXORS: 90,
        MuscleGroup.OBLIQUES: 60,
    },
    "Lower ab exercise",
    "intermediate"
)

HANGING_LEG_RAISE = Exercise(
    "Hanging Leg Raise",
    {
        MuscleGroup.ABS: 100,
        MuscleGroup.HIP_FLEXORS: 95,
        MuscleGroup.OBLIQUES: 75,
        MuscleGroup.FOREARMS: 70,
        MuscleGroup.LATS: 50,
    },
    "Advanced lower ab exercise hanging from bar",
    "advanced"
)

V_UP = Exercise(
    "V-up",
    {
        MuscleGroup.ABS: 100,
        MuscleGroup.HIP_FLEXORS: 90,
        MuscleGroup.OBLIQUES: 70,
    },
    "Advanced full-body crunch",
    "advanced"
)

MOUNTAIN_CLIMBER = Exercise(
    "Mountain Climber",
    {
        MuscleGroup.ABS: 85,
        MuscleGroup.HIP_FLEXORS: 80,
        MuscleGroup.SHOULDERS: 70,
        MuscleGroup.QUADS: 65,
    },
    "Dynamic core and cardio exercise",
    "intermediate"
)

# Lower Body Exercises
SQUAT = Exercise(
    "Squat",
    {
        MuscleGroup.QUADS: 95,
        MuscleGroup.GLUTES: 90,
        MuscleGroup.HAMSTRINGS: 70,
        MuscleGroup.CALVES: 40,
        MuscleGroup.ABS: 50,
    },
    "Classic bodyweight squat",
    "beginner"
)

JUMP_SQUAT = Exercise(
    "Jump Squat",
    {
        MuscleGroup.QUADS: 100,
        MuscleGroup.GLUTES: 95,
        MuscleGroup.HAMSTRINGS: 75,
        MuscleGroup.CALVES: 80,
        MuscleGroup.ABS: 60,
    },
    "Explosive squat variation",
    "intermediate"
)

PISTOL_SQUAT = Exercise(
    "Pistol Squat",
    {
        MuscleGroup.QUADS: 100,
        MuscleGroup.GLUTES: 95,
        MuscleGroup.HAMSTRINGS: 80,
        MuscleGroup.CALVES: 70,
        MuscleGroup.ABS: 75,
        MuscleGroup.HIP_FLEXORS: 60,
    },
    "Single-leg squat",
    "advanced"
)

LUNGE = Exercise(
    "Lunge",
    {
        MuscleGroup.QUADS: 90,
        MuscleGroup.GLUTES: 85,
        MuscleGroup.HAMSTRINGS: 65,
        MuscleGroup.CALVES: 45,
    },
    "Alternating leg lunge",
    "beginner"
)

BULGARIAN_SPLIT_SQUAT = Exercise(
    "Bulgarian Split Squat",
    {
        MuscleGroup.QUADS: 95,
        MuscleGroup.GLUTES: 90,
        MuscleGroup.HAMSTRINGS: 70,
        MuscleGroup.CALVES: 50,
    },
    "Single-leg squat with rear foot elevated",
    "intermediate"
)

CALF_RAISE = Exercise(
    "Calf Raise",
    {
        MuscleGroup.CALVES: 100,
    },
    "Standing calf raise",
    "beginner"
)

GLUTE_BRIDGE = Exercise(
    "Glute Bridge",
    {
        MuscleGroup.GLUTES: 95,
        MuscleGroup.HAMSTRINGS: 80,
        MuscleGroup.ABS: 55,
    },
    "Hip thrust exercise targeting glutes",
    "beginner"
)

SINGLE_LEG_GLUTE_BRIDGE = Exercise(
    "Single Leg Glute Bridge",
    {
        MuscleGroup.GLUTES: 100,
        MuscleGroup.HAMSTRINGS: 85,
        MuscleGroup.ABS: 65,
    },
    "Single-leg hip thrust",
    "intermediate"
)

# Full Body / Compound Exercises
BURPEE = Exercise(
    "Burpee",
    {
        MuscleGroup.CHEST: 75,
        MuscleGroup.TRICEPS: 70,
        MuscleGroup.SHOULDERS: 65,
        MuscleGroup.ABS: 80,
        MuscleGroup.QUADS: 85,
        MuscleGroup.GLUTES: 80,
        MuscleGroup.HAMSTRINGS: 60,
        MuscleGroup.CALVES: 55,
    },
    "Full-body explosive exercise",
    "intermediate"
)

JUMPING_JACK = Exercise(
    "Jumping Jack",
    {
        MuscleGroup.SHOULDERS: 60,
        MuscleGroup.CALVES: 70,
        MuscleGroup.QUADS: 55,
        MuscleGroup.ABS: 45,
    },
    "Classic cardio and warm-up exercise",
    "beginner"
)

BEAR_CRAWL = Exercise(
    "Bear Crawl",
    {
        MuscleGroup.SHOULDERS: 80,
        MuscleGroup.ABS: 85,
        MuscleGroup.QUADS: 75,
        MuscleGroup.TRICEPS: 60,
    },
    "Quadrupedal movement exercise",
    "intermediate"
)

# All exercises dictionary for easy lookup
EXERCISES = {
    # Push
    "push_up": PUSH_UP,
    "pushup": PUSH_UP,
    "wide_push_up": WIDE_PUSH_UP,
    "diamond_push_up": DIAMOND_PUSH_UP,
    "pike_push_up": PIKE_PUSH_UP,
    "handstand_push_up": HANDSTAND_PUSH_UP,
    "dips": DIPS,
    
    # Pull
    "pull_up": PULL_UP,
    "pullup": PULL_UP,
    "chin_up": CHIN_UP,
    "chinup": CHIN_UP,
    "australian_pull_up": AUSTRALIAN_PULL_UP,
    
    # Core
    "plank": PLANK,
    "side_plank": SIDE_PLANK,
    "sit_up": SIT_UP,
    "situp": SIT_UP,
    "crunch": CRUNCH,
    "bicycle_crunch": BICYCLE_CRUNCH,
    "leg_raise": LEG_RAISE,
    "hanging_leg_raise": HANGING_LEG_RAISE,
    "v_up": V_UP,
    "mountain_climber": MOUNTAIN_CLIMBER,
    
    # Lower Body
    "squat": SQUAT,
    "jump_squat": JUMP_SQUAT,
    "pistol_squat": PISTOL_SQUAT,
    "lunge": LUNGE,
    "bulgarian_split_squat": BULGARIAN_SPLIT_SQUAT,
    "calf_raise": CALF_RAISE,
    "glute_bridge": GLUTE_BRIDGE,
    "single_leg_glute_bridge": SINGLE_LEG_GLUTE_BRIDGE,
    
    # Full Body
    "burpee": BURPEE,
    "jumping_jack": JUMPING_JACK,
    "bear_crawl": BEAR_CRAWL,
}


def get_exercise(name: str) -> Exercise:
    """
    Get a predefined exercise by name.
    
    Args:
        name: Exercise name (case-insensitive, underscores optional)
        
    Returns:
        Exercise object with muscle activation data
        
    Raises:
        KeyError: If exercise name is not found
        
    Example:
        >>> from workout_generator.exercises import get_exercise
        >>> exercise = get_exercise("push_up")
        >>> print(exercise.muscle_activations)
    """
    key = name.lower().replace(" ", "_").replace("-", "_")
    if key not in EXERCISES:
        available = ", ".join(sorted(set(EXERCISES.keys())))
        raise KeyError(
            f"Exercise '{name}' not found. Available exercises: {available}"
        )
    return EXERCISES[key]


def list_exercises(difficulty: str = None, category: str = None) -> List[Exercise]:
    """
    List available exercises, optionally filtered by difficulty or category.
    
    Args:
        difficulty: Filter by difficulty level ("beginner", "intermediate", "advanced")
        category: Filter by category ("push", "pull", "core", "lower_body", "full_body")
        
    Returns:
        List of Exercise objects
        
    Example:
        >>> from workout_generator.exercises import list_exercises
        >>> beginner_exercises = list_exercises(difficulty="beginner")
        >>> for ex in beginner_exercises:
        ...     print(ex.name)
    """
    # Get unique exercises (since EXERCISES dict has multiple keys for same exercise)
    unique_exercises = list({ex.name: ex for ex in EXERCISES.values()}.values())
    
    # Filter by difficulty
    if difficulty:
        unique_exercises = [ex for ex in unique_exercises if ex.difficulty == difficulty.lower()]
    
    # Filter by category (basic categorization based on primary muscle groups)
    if category:
        category = category.lower()
        filtered = []
        for ex in unique_exercises:
            primary_muscles = ex.muscle_activations.keys()
            if category == "push" and (MuscleGroup.CHEST in primary_muscles or MuscleGroup.TRICEPS in primary_muscles):
                filtered.append(ex)
            elif category == "pull" and (MuscleGroup.LATS in primary_muscles or MuscleGroup.BICEPS in primary_muscles):
                filtered.append(ex)
            elif category == "core" and MuscleGroup.ABS in primary_muscles:
                filtered.append(ex)
            elif category == "lower_body" and (MuscleGroup.QUADS in primary_muscles or MuscleGroup.GLUTES in primary_muscles):
                filtered.append(ex)
            elif category == "full_body" and len(primary_muscles) >= 5:
                filtered.append(ex)
        unique_exercises = filtered
    
    return sorted(unique_exercises, key=lambda x: x.name)
