"""
SVG-based workout image generator for scalable vector graphics output.
"""

from typing import Dict, Optional, Tuple, List
import svgwrite
from svgwrite import Drawing
from svgwrite.shapes import Polygon, Ellipse, Line, Polyline
from svgwrite.path import Path
from svgwrite.container import Group
import os

from .muscles import (
    MuscleGroup,
    MUSCLE_DEFINITIONS,
    get_activation_color,
)


class SVGWireframeFigure:
    """Creates SVG-based lifelike wireframe human figure."""
    
    def __init__(self, dwg: Drawing, width: int = 1200, height: int = 2400):
        """
        Initialize SVG wireframe figure.
        
        Args:
            dwg: SVG Drawing object
            width: Image width in pixels
            height: Image height in pixels
        """
        self.dwg = dwg
        self.width = width
        self.height = height
        self.line_color = 'rgb(80,80,80)'
        self.detail_color = 'rgb(140,140,140)'
        self.skin_tone = 'rgb(220,190,170)'
        
        # Scale line widths
        scale_factor = width / 400
        self.line_width = max(2, int(3 * scale_factor))
        self.detail_width = max(1, int(2 * scale_factor))
    
    def _scale_point(self, point: Tuple[float, float]) -> Tuple[float, float]:
        """Convert normalized coordinates (0-1) to pixel coordinates."""
        x, y = point
        return (x * self.width, y * self.height)
    
    def _scale_points(self, points: List[Tuple[float, float]]) -> List[Tuple[float, float]]:
        """Scale multiple points."""
        return [self._scale_point(p) for p in points]
    
    def draw_figure(self, group: Group) -> None:
        """
        Draw a lifelike SVG wireframe human figure.
        
        Args:
            group: SVG group to add elements to
        """
        # Body mass shapes with subtle fill
        # Head volume
        head_center = self._scale_point((0.5, 0.08))
        head_rx = 0.06 * self.width
        head_ry = 0.04 * self.height
        group.add(self.dwg.ellipse(
            center=head_center,
            r=(head_rx, head_ry),
            fill=self.skin_tone,
            fill_opacity=0.12,
            stroke='none'
        ))
        
        # Torso volume
        torso_points = self._scale_points([
            (0.36, 0.19), (0.64, 0.19), (0.62, 0.28), (0.38, 0.28),
            (0.39, 0.40), (0.61, 0.40), (0.60, 0.49), (0.40, 0.49)
        ])
        group.add(self.dwg.polygon(
            points=torso_points,
            fill=self.skin_tone,
            fill_opacity=0.08,
            stroke='none'
        ))
        
        # Enhanced legs with realistic bulges
        # Left thigh
        left_thigh_points = self._scale_points([
            (0.41, 0.55), (0.46, 0.55), (0.465, 0.60), (0.46, 0.68),
            (0.455, 0.73), (0.41, 0.73), (0.405, 0.68), (0.40, 0.60)
        ])
        group.add(self.dwg.polygon(
            points=left_thigh_points,
            fill=self.skin_tone,
            fill_opacity=0.10,
            stroke='none'
        ))
        
        # Right thigh
        right_thigh_points = self._scale_points([
            (0.59, 0.55), (0.54, 0.55), (0.535, 0.60), (0.54, 0.68),
            (0.545, 0.73), (0.59, 0.73), (0.595, 0.68), (0.60, 0.60)
        ])
        group.add(self.dwg.polygon(
            points=right_thigh_points,
            fill=self.skin_tone,
            fill_opacity=0.10,
            stroke='none'
        ))
        
        # Left calf with realistic bulge
        left_calf_points = self._scale_points([
            (0.415, 0.74), (0.445, 0.74), (0.45, 0.78), (0.445, 0.85),
            (0.43, 0.90), (0.41, 0.90), (0.405, 0.85), (0.40, 0.78)
        ])
        group.add(self.dwg.polygon(
            points=left_calf_points,
            fill=self.skin_tone,
            fill_opacity=0.10,
            stroke='none'
        ))
        
        # Right calf
        right_calf_points = self._scale_points([
            (0.585, 0.74), (0.555, 0.74), (0.55, 0.78), (0.555, 0.85),
            (0.57, 0.90), (0.59, 0.90), (0.595, 0.85), (0.60, 0.78)
        ])
        group.add(self.dwg.polygon(
            points=right_calf_points,
            fill=self.skin_tone,
            fill_opacity=0.10,
            stroke='none'
        ))
        
        # Wireframe details
        # Head outline
        group.add(self.dwg.ellipse(
            center=head_center,
            r=(head_rx, head_ry),
            fill='none',
            stroke=self.line_color,
            stroke_width=self.line_width
        ))
        
        # Neck
        neck_left = self._scale_points([(0.48, 0.12), (0.47, 0.16), (0.46, 0.18)])
        neck_right = self._scale_points([(0.52, 0.12), (0.53, 0.16), (0.54, 0.18)])
        group.add(self.dwg.polyline(
            points=neck_left,
            fill='none',
            stroke=self.line_color,
            stroke_width=self.line_width,
            stroke_linecap='round',
            stroke_linejoin='round'
        ))
        group.add(self.dwg.polyline(
            points=neck_right,
            fill='none',
            stroke=self.line_color,
            stroke_width=self.line_width,
            stroke_linecap='round',
            stroke_linejoin='round'
        ))
        
        # Torso contours
        self._draw_torso(group)
        
        # Arms
        self._draw_arms(group)
        
        # Enhanced legs with detail
        self._draw_legs(group)
    
    def _draw_torso(self, group: Group):
        """Draw detailed torso."""
        # Shoulders
        left_shoulder = self._scale_points([(0.33, 0.18), (0.31, 0.20), (0.30, 0.23), (0.31, 0.25)])
        right_shoulder = self._scale_points([(0.67, 0.18), (0.69, 0.20), (0.70, 0.23), (0.69, 0.25)])
        
        for points in [left_shoulder, right_shoulder]:
            group.add(self.dwg.polyline(
                points=points,
                fill='none',
                stroke=self.line_color,
                stroke_width=self.line_width,
                stroke_linecap='round',
                stroke_linejoin='round'
            ))
        
        # Torso sides
        left_torso = self._scale_points([(0.37, 0.28), (0.38, 0.33), (0.39, 0.40), (0.40, 0.47)])
        right_torso = self._scale_points([(0.63, 0.28), (0.62, 0.33), (0.61, 0.40), (0.60, 0.47)])
        
        for points in [left_torso, right_torso]:
            group.add(self.dwg.polyline(
                points=points,
                fill='none',
                stroke=self.line_color,
                stroke_width=self.line_width,
                stroke_linecap='round',
                stroke_linejoin='round'
            ))
    
    def _draw_arms(self, group: Group):
        """Draw arms with detail."""
        # Left arm
        left_arm_outer = self._scale_points([(0.31, 0.25), (0.29, 0.30), (0.28, 0.35), (0.28, 0.38)])
        left_forearm_outer = self._scale_points([(0.28, 0.38), (0.27, 0.43), (0.26, 0.48), (0.26, 0.52)])
        
        # Right arm
        right_arm_outer = self._scale_points([(0.69, 0.25), (0.71, 0.30), (0.72, 0.35), (0.72, 0.38)])
        right_forearm_outer = self._scale_points([(0.72, 0.38), (0.73, 0.43), (0.74, 0.48), (0.74, 0.52)])
        
        for points in [left_arm_outer, left_forearm_outer, right_arm_outer, right_forearm_outer]:
            group.add(self.dwg.polyline(
                points=points,
                fill='none',
                stroke=self.line_color,
                stroke_width=self.line_width,
                stroke_linecap='round',
                stroke_linejoin='round'
            ))
    
    def _draw_legs(self, group: Group):
        """Draw enhanced legs with realistic detail."""
        # Left leg - detailed quads
        left_quad_outer = self._scale_points([(0.40, 0.59), (0.395, 0.64), (0.395, 0.69), (0.40, 0.73)])
        left_quad_inner = self._scale_points([(0.45, 0.56), (0.455, 0.64), (0.455, 0.69), (0.45, 0.73)])
        
        # Left calf - detailed with gastrocnemius
        left_calf_outer = self._scale_points([(0.40, 0.745), (0.395, 0.77), (0.395, 0.82), (0.40, 0.87), (0.41, 0.90)])
        left_calf_inner = self._scale_points([(0.45, 0.745), (0.455, 0.76), (0.46, 0.80), (0.455, 0.86), (0.445, 0.90)])
        
        # Right leg - mirror
        right_quad_outer = self._scale_points([(0.60, 0.59), (0.605, 0.64), (0.605, 0.69), (0.60, 0.73)])
        right_quad_inner = self._scale_points([(0.55, 0.56), (0.545, 0.64), (0.545, 0.69), (0.55, 0.73)])
        
        right_calf_outer = self._scale_points([(0.60, 0.745), (0.605, 0.77), (0.605, 0.82), (0.60, 0.87), (0.59, 0.90)])
        right_calf_inner = self._scale_points([(0.55, 0.745), (0.545, 0.76), (0.54, 0.80), (0.545, 0.86), (0.555, 0.90)])
        
        all_leg_lines = [
            left_quad_outer, left_quad_inner, left_calf_outer, left_calf_inner,
            right_quad_outer, right_quad_inner, right_calf_outer, right_calf_inner
        ]
        
        for points in all_leg_lines:
            group.add(self.dwg.polyline(
                points=points,
                fill='none',
                stroke=self.line_color,
                stroke_width=self.line_width,
                stroke_linecap='round',
                stroke_linejoin='round'
            ))
        
        # Knee caps
        for knee_x in [0.425, 0.575]:
            knee_center = self._scale_point((knee_x, 0.735))
            group.add(self.dwg.ellipse(
                center=knee_center,
                r=(8, 10),
                fill=self.skin_tone,
                fill_opacity=0.14,
                stroke=self.detail_color,
                stroke_width=1
            ))
        
        # Ankle bones
        for ankle_x in [0.405, 0.595]:
            ankle_pt = self._scale_point((ankle_x, 0.905))
            group.add(self.dwg.circle(
                center=ankle_pt,
                r=4,
                fill=self.skin_tone,
                fill_opacity=0.20,
                stroke=self.detail_color,
                stroke_width=1
            ))
        
        # Feet
        left_foot = self._scale_points([
            (0.425, 0.91), (0.415, 0.93), (0.405, 0.945),
            (0.405, 0.955), (0.415, 0.965), (0.430, 0.970)
        ])
        right_foot = self._scale_points([
            (0.575, 0.91), (0.585, 0.93), (0.595, 0.945),
            (0.595, 0.955), (0.585, 0.965), (0.570, 0.970)
        ])
        
        for foot_points in [left_foot, right_foot]:
            group.add(self.dwg.polyline(
                points=foot_points,
                fill='none',
                stroke=self.line_color,
                stroke_width=self.line_width,
                stroke_linecap='round',
                stroke_linejoin='round'
            ))


class SVGWorkoutImageGenerator:
    """
    Generates workout images as SVG (Scalable Vector Graphics).
    
    SVG format provides infinite scalability and smaller file sizes.
    """
    
    def __init__(
        self,
        width: int = 1200,
        height: int = 2400,
        background_color: Tuple[int, int, int] = (245, 245, 245),
    ):
        """
        Initialize the SVG workout image generator.
        
        Args:
            width: Image width in pixels
            height: Image height in pixels
            background_color: RGB tuple for background color
        """
        self.width = width
        self.height = height
        self.background_color = background_color
    
    def generate(
        self,
        muscle_activations: Dict[MuscleGroup, float],
        title: Optional[str] = None,
        output_path: Optional[str] = None,
    ) -> Drawing:
        """
        Generate an SVG workout image.
        
        Args:
            muscle_activations: Dictionary mapping muscle groups to activation levels (0-100)
            title: Optional title to display on the image
            output_path: Optional path to save the SVG file
            
        Returns:
            SVG Drawing object
        """
        # Create SVG drawing
        dwg = svgwrite.Drawing(
            filename=output_path if output_path else 'workout.svg',
            size=(f'{self.width}px', f'{self.height}px'),
            viewBox=f'0 0 {self.width} {self.height}'
        )
        
        # Add background with subtle vignette
        bg_color = f'rgb({self.background_color[0]},{self.background_color[1]},{self.background_color[2]})'
        dwg.add(dwg.rect(
            insert=(0, 0),
            size=('100%', '100%'),
            fill=bg_color
        ))
        
        # Add vignette effect with radial gradient
        vignette = dwg.defs.add(dwg.radialGradient(id='vignette'))
        vignette.add_stop_color(offset='0%', color=bg_color, opacity=1)
        vignette.add_stop_color(offset='100%', color='rgb(200,200,200)', opacity=0.3)
        dwg.add(dwg.rect(
            insert=(0, 0),
            size=('100%', '100%'),
            fill='url(#vignette)'
        ))
        
        # Create main group for muscles and figure
        main_group = dwg.add(dwg.g(id='workout_figure'))
        
        # Draw muscles with gradient shading
        muscle_group = dwg.add(dwg.g(id='muscles'))
        
        for muscle_type, activation in muscle_activations.items():
            if muscle_type in MUSCLE_DEFINITIONS:
                color = get_activation_color(activation)
                color_str = f'rgb({color[0]},{color[1]},{color[2]})'
                
                for muscle_def in MUSCLE_DEFINITIONS[muscle_type]:
                    # Scale polygon points
                    scaled_points = [
                        (x * self.width, y * self.height)
                        for x, y in muscle_def.polygon_points
                    ]
                    
                    # Create gradient for 3D effect
                    grad_id = f'grad_{muscle_type.value}_{muscle_def.side}'
                    gradient = dwg.defs.add(dwg.linearGradient(id=grad_id))
                    
                    # Darker at edges, lighter in center
                    darker = tuple(max(0, c - 40) for c in color)
                    lighter = tuple(min(255, c + 30) for c in color)
                    
                    gradient.add_stop_color(offset='0%', color=f'rgb({darker[0]},{darker[1]},{darker[2]})', opacity=0.55)
                    gradient.add_stop_color(offset='50%', color=f'rgb({lighter[0]},{lighter[1]},{lighter[2]})', opacity=0.65)
                    gradient.add_stop_color(offset='100%', color=f'rgb({darker[0]},{darker[1]},{darker[2]})', opacity=0.55)
                    
                    muscle_group.add(dwg.polygon(
                        points=scaled_points,
                        fill=f'url(#{grad_id})',
                        stroke='none'
                    ))
        
        # Draw wireframe figure
        wireframe = SVGWireframeFigure(dwg, self.width, self.height)
        figure_group = dwg.add(dwg.g(id='wireframe'))
        wireframe.draw_figure(figure_group)
        
        # Add title
        if title:
            font_size = max(28, int(28 * (self.width / 400)))
            dwg.add(dwg.text(
                title,
                insert=(self.width // 2, font_size + 15),
                text_anchor='middle',
                font_size=f'{font_size}px',
                font_family='Arial, sans-serif',
                font_weight='bold',
                fill='rgb(20,20,20)',
                style='text-shadow: 2px 2px 4px rgba(100,100,100,0.5);'
            ))
        
        # Save if path provided
        if output_path:
            dwg.save()
        
        return dwg
    
    def generate_animation_frames(
        self,
        muscle_activations: Dict[MuscleGroup, float],
        num_frames: int = 10,
        title: Optional[str] = None,
        output_dir: Optional[str] = None,
    ) -> List[Drawing]:
        """
        Generate SVG animation frames showing gradual muscle activation.
        
        Args:
            muscle_activations: Dictionary mapping muscle groups to final activation levels
            num_frames: Number of animation frames to generate
            title: Optional title to display on the images
            output_dir: Optional directory to save SVG frames
            
        Returns:
            List of SVG Drawing objects representing animation frames
        """
        frames = []
        
        if output_dir:
            os.makedirs(output_dir, exist_ok=True)
        
        for frame_idx in range(num_frames):
            # Calculate activation level for this frame
            progress = (frame_idx + 1) / num_frames
            frame_activations = {
                muscle: activation * progress
                for muscle, activation in muscle_activations.items()
            }
            
            # Generate frame
            output_path = None
            if output_dir:
                output_path = os.path.join(output_dir, f'frame_{frame_idx:03d}.svg')
            
            frame = self.generate(frame_activations, title, output_path)
            frames.append(frame)
        
        return frames


def generate_workout_svg(
    exercise_name: str,
    muscle_activations: Optional[Dict[MuscleGroup, float]] = None,
    width: int = 1200,
    height: int = 2400,
    save_path: Optional[str] = None,
) -> Drawing:
    """
    Convenience function to generate a workout SVG image.
    
    Args:
        exercise_name: Name of the exercise (or Exercise object from exercises module)
        muscle_activations: Dictionary mapping muscle groups to activation levels (0-100).
                          If None, will attempt to use predefined exercise data.
        width: Image width in pixels (default: 1200)
        height: Image height in pixels (default: 2400)
        save_path: Optional path to save the SVG file
        
    Returns:
        SVG Drawing object
        
    Example:
        >>> from workout_generator import generate_workout_svg, MuscleGroup
        >>> # Using predefined exercise
        >>> svg = generate_workout_svg("Push-up", save_path="pushup.svg")
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
    
    generator = SVGWorkoutImageGenerator(width, height)
    return generator.generate(activations, title, save_path)
