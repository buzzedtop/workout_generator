"""
Wireframe figure generation for safe-for-work human body visualization.
"""

from typing import List, Tuple
from PIL import Image, ImageDraw


class WireframeFigure:
    """Creates a safe-for-work wireframe human figure."""
    
    def __init__(self, width: int = 400, height: int = 800):
        """
        Initialize wireframe figure.
        
        Args:
            width: Image width in pixels
            height: Image height in pixels
        """
        self.width = width
        self.height = height
        self.line_color = (200, 200, 200)  # Light gray for wireframe
        self.line_width = 2
        
    def _scale_point(self, point: Tuple[float, float]) -> Tuple[int, int]:
        """Convert normalized coordinates (0-1) to pixel coordinates."""
        x, y = point
        return (int(x * self.width), int(y * self.height))
    
    def draw_figure(self, draw: ImageDraw.ImageDraw) -> None:
        """
        Draw a safe-for-work wireframe human figure.
        
        The figure is a simplified stick figure with basic body proportions,
        censored to be appropriate for all audiences.
        
        Args:
            draw: PIL ImageDraw object to draw on
        """
        # Head (circle, SFW - simple circle)
        head_center = self._scale_point((0.5, 0.10))
        head_radius = int(0.08 * self.height)
        draw.ellipse(
            [
                head_center[0] - head_radius,
                head_center[1] - head_radius,
                head_center[0] + head_radius,
                head_center[1] + head_radius,
            ],
            outline=self.line_color,
            width=self.line_width,
        )
        
        # Neck
        neck_top = self._scale_point((0.5, 0.18))
        neck_bottom = self._scale_point((0.5, 0.20))
        draw.line([neck_top, neck_bottom], fill=self.line_color, width=self.line_width)
        
        # Torso outline (simplified, censored shape)
        # Upper torso
        torso_points = [
            self._scale_point((0.38, 0.20)),  # Left shoulder
            self._scale_point((0.62, 0.20)),  # Right shoulder
            self._scale_point((0.60, 0.35)),  # Right mid-torso
            self._scale_point((0.58, 0.50)),  # Right waist
            self._scale_point((0.56, 0.52)),  # Right hip
            self._scale_point((0.44, 0.52)),  # Left hip
            self._scale_point((0.42, 0.50)),  # Left waist
            self._scale_point((0.40, 0.35)),  # Left mid-torso
            self._scale_point((0.38, 0.20)),  # Back to left shoulder
        ]
        draw.line(torso_points, fill=self.line_color, width=self.line_width)
        
        # Add a censorship box/simplified area for lower torso
        censor_box = [
            self._scale_point((0.42, 0.48)),
            self._scale_point((0.58, 0.48)),
            self._scale_point((0.58, 0.54)),
            self._scale_point((0.42, 0.54)),
            self._scale_point((0.42, 0.48)),
        ]
        draw.line(censor_box, fill=self.line_color, width=self.line_width)
        
        # Arms
        # Left arm
        left_shoulder = self._scale_point((0.38, 0.20))
        left_elbow = self._scale_point((0.32, 0.35))
        left_wrist = self._scale_point((0.30, 0.50))
        draw.line([left_shoulder, left_elbow], fill=self.line_color, width=self.line_width)
        draw.line([left_elbow, left_wrist], fill=self.line_color, width=self.line_width)
        
        # Right arm
        right_shoulder = self._scale_point((0.62, 0.20))
        right_elbow = self._scale_point((0.68, 0.35))
        right_wrist = self._scale_point((0.70, 0.50))
        draw.line([right_shoulder, right_elbow], fill=self.line_color, width=self.line_width)
        draw.line([right_elbow, right_wrist], fill=self.line_color, width=self.line_width)
        
        # Simple hand representations (circles)
        hand_radius = int(0.015 * self.height)
        draw.ellipse(
            [
                left_wrist[0] - hand_radius,
                left_wrist[1] - hand_radius,
                left_wrist[0] + hand_radius,
                left_wrist[1] + hand_radius,
            ],
            outline=self.line_color,
            width=self.line_width,
        )
        draw.ellipse(
            [
                right_wrist[0] - hand_radius,
                right_wrist[1] - hand_radius,
                right_wrist[0] + hand_radius,
                right_wrist[1] + hand_radius,
            ],
            outline=self.line_color,
            width=self.line_width,
        )
        
        # Legs
        # Left leg
        left_hip = self._scale_point((0.44, 0.52))
        left_knee = self._scale_point((0.43, 0.73))
        left_ankle = self._scale_point((0.43, 0.92))
        draw.line([left_hip, left_knee], fill=self.line_color, width=self.line_width)
        draw.line([left_knee, left_ankle], fill=self.line_color, width=self.line_width)
        
        # Right leg
        right_hip = self._scale_point((0.56, 0.52))
        right_knee = self._scale_point((0.57, 0.73))
        right_ankle = self._scale_point((0.57, 0.92))
        draw.line([right_hip, right_knee], fill=self.line_color, width=self.line_width)
        draw.line([right_knee, right_ankle], fill=self.line_color, width=self.line_width)
        
        # Simple foot representations (small lines)
        left_foot_end = self._scale_point((0.41, 0.92))
        right_foot_end = self._scale_point((0.59, 0.92))
        draw.line([left_ankle, left_foot_end], fill=self.line_color, width=self.line_width)
        draw.line([right_ankle, right_foot_end], fill=self.line_color, width=self.line_width)
        
        # Add shoulder structure
        draw.ellipse(
            [
                left_shoulder[0] - 5,
                left_shoulder[1] - 5,
                left_shoulder[0] + 5,
                left_shoulder[1] + 5,
            ],
            outline=self.line_color,
            width=self.line_width,
        )
        draw.ellipse(
            [
                right_shoulder[0] - 5,
                right_shoulder[1] - 5,
                right_shoulder[0] + 5,
                right_shoulder[1] + 5,
            ],
            outline=self.line_color,
            width=self.line_width,
        )
        
        # Add knee joints
        knee_radius = 5
        draw.ellipse(
            [
                left_knee[0] - knee_radius,
                left_knee[1] - knee_radius,
                left_knee[0] + knee_radius,
                left_knee[1] + knee_radius,
            ],
            outline=self.line_color,
            width=self.line_width,
        )
        draw.ellipse(
            [
                right_knee[0] - knee_radius,
                right_knee[1] - knee_radius,
                right_knee[0] + knee_radius,
                right_knee[1] + knee_radius,
            ],
            outline=self.line_color,
            width=self.line_width,
        )
