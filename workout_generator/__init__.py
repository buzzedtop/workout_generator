"""
Workout Generator - A package for generating workout images with muscle activation visualization.

This package creates wireframe human figures with color-coded muscle activation,
showing which muscles are engaged during different exercises.

Supports both raster (PNG) and vector (SVG) output formats.
"""

from .generator import WorkoutImageGenerator, generate_workout_image
from .svg_generator import SVGWorkoutImageGenerator, generate_workout_svg
from .muscles import MuscleGroup, ActivationLevel
from .exercises import Exercise, get_exercise, list_exercises, EXERCISES

__version__ = "0.1.0"
__all__ = [
    "WorkoutImageGenerator",
    "generate_workout_image",
    "SVGWorkoutImageGenerator",
    "generate_workout_svg",
    "MuscleGroup",
    "ActivationLevel",
    "Exercise",
    "get_exercise",
    "list_exercises",
    "EXERCISES",
]
