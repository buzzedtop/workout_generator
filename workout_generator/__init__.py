"""
Workout Generator - A package for generating workout images with muscle activation visualization.

This package creates wireframe human figures with color-coded muscle activation,
showing which muscles are engaged during different exercises.
"""

from .generator import WorkoutImageGenerator, generate_workout_image
from .muscles import MuscleGroup, ActivationLevel
from .exercises import Exercise, get_exercise, list_exercises, EXERCISES

__version__ = "0.1.0"
__all__ = [
    "WorkoutImageGenerator",
    "generate_workout_image",
    "MuscleGroup",
    "ActivationLevel",
    "Exercise",
    "get_exercise",
    "list_exercises",
    "EXERCISES",
]
