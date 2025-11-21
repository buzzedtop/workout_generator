"""
Main workout image generator module with lifelike rendering.
"""

from typing import Dict, Optional, Tuple, Union, List
from PIL import Image, ImageDraw, ImageFont, ImageFilter
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
    Generates workout images with lifelike figures and muscle activation visualization.
    
    Creates realistic images showing which muscles are activated during exercises,
    with 3D shading and color gradients from blue (inactive) to red (fully activated).
    """
    
    def __init__(
        self,
        width: int = 1200,
        height: int = 2400,
        background_color: Tuple[int, int, int] = (245, 245, 245),
    ):
        """
        Initialize the workout image generator.
        
        Args:
            width: Image width in pixels (default: 1200)
            height: Image height in pixels (default: 2400)
            background_color: RGB tuple for background color
        """
        self.width = width
        self.height = height
        self.background_color = background_color
        self.wireframe = WireframeFigure(width, height)
        
    def _scale_polygon(
        self, points: List[Tuple[float, float]]
    ) -> List[Tuple[int, int]]:
        """Convert normalized polygon coordinates to pixel coordinates."""
        return [(int(x * self.width), int(y * self.height)) for x, y in points]
    
    def _add_gradient_to_muscle(
        self, 
        draw: ImageDraw.ImageDraw,
        points: List[Tuple[int, int]], 
        base_color: Tuple[int, int, int],
        activation: float
    ):
        """
        Draw a muscle with 3D gradient shading for lifelike appearance.
        
        Args:
            draw: PIL ImageDraw object
            points: Polygon points defining the muscle
            base_color: Base RGB color (from activation level)
            activation: Activation level 0-100
        """
        # Create gradient effect by drawing multiple overlapping polygons
        # with varying opacity to simulate 3D rounded muscle
        
        # Calculate center point of muscle
        if len(points) < 3:
            return
            
        center_x = sum(p[0] for p in points) / len(points)
        center_y = sum(p[1] for p in points) / len(points)
        
        # Draw base muscle with slight shadow
        shadow_color = tuple(max(0, c - 40) for c in base_color)
        draw.polygon(points, fill=shadow_color + (180,), outline=None)
        
        # Draw highlight gradient layers from center outward for 3D effect
        num_layers = 5
        for i in range(num_layers, 0, -1):
            scale = 0.3 + (i / num_layers) * 0.5  # Scale from center
            
            # Scale points toward center
            scaled_points = []
            for px, py in points:
                new_x = center_x + (px - center_x) * scale
                new_y = center_y + (py - center_y) * scale
                scaled_points.append((int(new_x), int(new_y)))
            
            # Lighter color toward center (highlight)
            brightness_boost = int(30 * (1 - i / num_layers))
            layer_color = tuple(min(255, c + brightness_boost) for c in base_color)
            opacity = int(160 - (i * 15))  # Fade out toward edges
            
            if len(scaled_points) >= 3:
                draw.polygon(scaled_points, fill=layer_color + (opacity,), outline=None)
    
    def generate(
        self,
        muscle_activations: Dict[MuscleGroup, float],
        title: Optional[str] = None,
    ) -> Image.Image:
        """
        Generate a lifelike workout image with muscle activation visualization.
        
        Args:
            muscle_activations: Dictionary mapping muscle groups to activation levels (0-100)
            title: Optional title to display on the image
            
        Returns:
            PIL Image object containing the generated workout visualization
        """
        # Create base image with subtle gradient background for depth
        image = Image.new("RGBA", (self.width, self.height), self.background_color + (255,))
        
        # Add subtle vignette background for more professional look
        bg_draw = ImageDraw.Draw(image, "RGBA")
        for i in range(20):
            darkness = int(i * 2)
            color = tuple(max(0, c - darkness) for c in self.background_color)
            # Draw border rectangles getting darker
            border = i * 3
            bg_draw.rectangle(
                [border, border, self.width - border, self.height - border],
                outline=color + (5,),
                width=2
            )
        
        # Create a separate layer for muscles with transparency
        muscle_layer = Image.new("RGBA", (self.width, self.height), (255, 255, 255, 0))
        muscle_draw = ImageDraw.Draw(muscle_layer, "RGBA")
        
        # Draw muscle overlays with 3D gradient shading
        for muscle_group, activation in muscle_activations.items():
            if muscle_group in MUSCLE_DEFINITIONS:
                color = get_activation_color(activation)
                
                for muscle_def in MUSCLE_DEFINITIONS[muscle_group]:
                    scaled_points = self._scale_polygon(muscle_def.polygon_points)
                    # Use gradient rendering for lifelike 3D appearance
                    self._add_gradient_to_muscle(muscle_draw, scaled_points, color, activation)
        
        # Apply slight blur to muscles for softer, more realistic appearance
        muscle_layer = muscle_layer.filter(ImageFilter.GaussianBlur(radius=1))
        
        # Composite the muscle layer onto the base image
        image = Image.alpha_composite(image, muscle_layer)
        
        # Convert back to RGB for wireframe drawing
        final_image = Image.new("RGB", (self.width, self.height), self.background_color)
        final_image.paste(image, (0, 0), image)
        
        # Draw the wireframe figure on top with anti-aliasing
        draw = ImageDraw.Draw(final_image, "RGBA")
        self.wireframe.draw_figure(draw)
        
        # Add title if provided with better typography
        if title:
            # Cross-platform font discovery
            font = None
            # Scale font size based on image width (base size is 28 for 400px width)
            font_size = max(28, int(28 * (self.width / 400)))
            font_paths = [
                "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",  # Linux
                "/System/Library/Fonts/Helvetica.ttc",  # macOS
                "C:\\Windows\\Fonts\\arialbd.ttf",  # Windows
            ]
            
            for font_path in font_paths:
                try:
                    font = ImageFont.truetype(font_path, font_size)
                    break
                except:
                    continue
            
            # Fallback to default font if no system font found
            if font is None:
                font = ImageFont.load_default()
            
            # Draw title at the top with shadow for better readability
            title_bbox = draw.textbbox((0, 0), title, font=font)
            title_width = title_bbox[2] - title_bbox[0]
            title_x = (self.width - title_width) // 2
            # Scale title position based on height
            title_y = max(15, int(15 * (self.height / 800)))
            shadow_offset = max(2, int(2 * (self.width / 400)))
            
            # Draw shadow
            draw.text((title_x + shadow_offset, title_y + shadow_offset), title, fill=(100, 100, 100), font=font)
            # Draw main text
            draw.text((title_x, title_y), title, fill=(20, 20, 20), font=font)
        
        return final_image
        
        return final_image
    
    def generate_animation_frames(
        self,
        muscle_activations: Dict[MuscleGroup, float],
        num_frames: int = 10,
        title: Optional[str] = None,
    ) -> List[Image.Image]:
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
    muscle_activations: Optional[Dict[MuscleGroup, float]] = None,
    width: int = 1200,
    height: int = 2400,
    save_path: Optional[str] = None,
) -> Image.Image:
    """
    Convenience function to generate a workout image.
    
    Args:
        exercise_name: Name of the exercise (or Exercise object from exercises module)
        muscle_activations: Dictionary mapping muscle groups to activation levels (0-100).
                          If None, will attempt to use predefined exercise data.
        width: Image width in pixels (default: 1200)
        height: Image height in pixels (default: 2400)
        save_path: Optional path to save the image
        
    Returns:
        PIL Image object containing the generated workout visualization
        
    Example:
        >>> from workout_generator import generate_workout_image, MuscleGroup
        >>> # Using predefined exercise
        >>> image = generate_workout_image("Push-up")
        >>> 
        >>> # Using custom activations
        >>> image = generate_workout_image(
        ...     "Bicep Curls",
        ...     {
        ...         MuscleGroup.BICEPS: 90,
        ...         MuscleGroup.FOREARMS: 60,
        ...     }
        ... )
    """
    # Check if it's an Exercise object
    from .exercises import Exercise
    
    if isinstance(exercise_name, Exercise):
        title = exercise_name.name
        activations = exercise_name.muscle_activations
    elif muscle_activations is None:
        # Try to get predefined exercise
        from .exercises import get_exercise
        try:
            exercise = get_exercise(exercise_name)
            title = exercise.name
            activations = exercise.muscle_activations
        except KeyError:
            raise ValueError(
                f"No muscle activations provided and '{exercise_name}' is not a predefined exercise. "
                "Either provide muscle_activations or use a predefined exercise name."
            )
    else:
        title = exercise_name
        activations = muscle_activations
    
    generator = WorkoutImageGenerator(width, height)
    image = generator.generate(activations, title=title)
    
    if save_path:
        image.save(save_path)
    
    return image
