"""
Main workout image generator module.
"""

from typing import Dict, Optional, Tuple
from PIL import Image, ImageDraw, ImageFont
import os

from .muscles import (
    MuscleGroup,
    ActivationLevel,
    MUSCLE_DEFINITIONS,
    get_activation_color,
)
from .wireframe import WireframeFigure


class WorkoutImageGenerator:
    """
    Generates workout images with wireframe figures and muscle activation visualization.
    
    Creates safe-for-work images showing which muscles are activated during exercises,
    with color gradients from blue (inactive) to red (fully activated).
    """
    
    def __init__(
        self,
        width: int = 400,
        height: int = 800,
        background_color: Tuple[int, int, int] = (255, 255, 255),
    ):
        """
        Initialize the workout image generator.
        
        Args:
            width: Image width in pixels
            height: Image height in pixels
            background_color: RGB tuple for background color
        """
        self.width = width
        self.height = height
        self.background_color = background_color
        self.wireframe = WireframeFigure(width, height)
        
    def _scale_polygon(
        self, points: list[Tuple[float, float]]
    ) -> list[Tuple[int, int]]:
        """Convert normalized polygon coordinates to pixel coordinates."""
        return [(int(x * self.width), int(y * self.height)) for x, y in points]
    
    def generate(
        self,
        muscle_activations: Dict[MuscleGroup, float],
        title: Optional[str] = None,
    ) -> Image.Image:
        """
        Generate a workout image with muscle activation visualization.
        
        Args:
            muscle_activations: Dictionary mapping muscle groups to activation levels (0-100)
            title: Optional title to display on the image
            
        Returns:
            PIL Image object containing the generated workout visualization
        """
        # Create base image
        image = Image.new("RGB", (self.width, self.height), self.background_color)
        draw = ImageDraw.Draw(image, "RGBA")
        
        # Draw muscle overlays first (underneath the wireframe)
        for muscle_group, activation in muscle_activations.items():
            if muscle_group in MUSCLE_DEFINITIONS:
                color = get_activation_color(activation)
                # Add transparency to the color
                color_with_alpha = color + (100,)  # 100/255 opacity
                
                for muscle_def in MUSCLE_DEFINITIONS[muscle_group]:
                    scaled_points = self._scale_polygon(muscle_def.polygon_points)
                    draw.polygon(scaled_points, fill=color_with_alpha, outline=None)
        
        # Draw the wireframe figure on top
        self.wireframe.draw_figure(draw)
        
        # Add title if provided
        if title:
            try:
                # Try to use a nicer font if available
                font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 24)
            except:
                # Fallback to default font
                font = ImageFont.load_default()
            
            # Draw title at the top
            title_bbox = draw.textbbox((0, 0), title, font=font)
            title_width = title_bbox[2] - title_bbox[0]
            title_x = (self.width - title_width) // 2
            draw.text((title_x, 10), title, fill=(0, 0, 0), font=font)
        
        return image
    
    def generate_animation_frames(
        self,
        muscle_activations: Dict[MuscleGroup, float],
        num_frames: int = 10,
        title: Optional[str] = None,
    ) -> list[Image.Image]:
        """
        Generate animation frames showing gradual muscle activation.
        
        Args:
            muscle_activations: Dictionary mapping muscle groups to final activation levels (0-100)
            num_frames: Number of animation frames to generate
            title: Optional title to display on the images
            
        Returns:
            List of PIL Image objects representing animation frames
        """
        frames = []
        
        for frame_idx in range(num_frames):
            # Calculate activation level for this frame
            progress = (frame_idx + 1) / num_frames
            frame_activations = {
                muscle: activation * progress
                for muscle, activation in muscle_activations.items()
            }
            
            # Generate frame
            frame = self.generate(frame_activations, title)
            frames.append(frame)
        
        return frames


def generate_workout_image(
    exercise_name: str,
    muscle_activations: Dict[MuscleGroup, float],
    width: int = 400,
    height: int = 800,
    save_path: Optional[str] = None,
) -> Image.Image:
    """
    Convenience function to generate a workout image.
    
    Args:
        exercise_name: Name of the exercise
        muscle_activations: Dictionary mapping muscle groups to activation levels (0-100)
        width: Image width in pixels
        height: Image height in pixels
        save_path: Optional path to save the image
        
    Returns:
        PIL Image object containing the generated workout visualization
        
    Example:
        >>> from workout_generator import generate_workout_image, MuscleGroup
        >>> image = generate_workout_image(
        ...     "Bicep Curls",
        ...     {
        ...         MuscleGroup.BICEPS: 90,
        ...         MuscleGroup.FOREARMS: 60,
        ...     }
        ... )
    """
    generator = WorkoutImageGenerator(width, height)
    image = generator.generate(muscle_activations, title=exercise_name)
    
    if save_path:
        image.save(save_path)
    
    return image
