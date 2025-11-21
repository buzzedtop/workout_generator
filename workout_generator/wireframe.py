"""
High-fidelity wireframe figure generation for anatomically accurate visualization.
"""

from typing import List, Tuple, Optional
from PIL import Image, ImageDraw
import math


class WireframeFigure:
    """Creates a high-fidelity wireframe human figure with anatomical detail."""
    
    def __init__(self, width: int = 400, height: int = 800):
        """
        Initialize high-fidelity wireframe figure.
        
        Args:
            width: Image width in pixels
            height: Image height in pixels
        """
        self.width = width
        self.height = height
        self.line_color = (120, 120, 120)  # Dark gray for primary wireframe
        self.detail_color = (160, 160, 160)  # Lighter gray for detail lines
        self.line_width = 2
        self.detail_width = 1
        
    def _scale_point(self, point: Tuple[float, float]) -> Tuple[int, int]:
        """Convert normalized coordinates (0-1) to pixel coordinates."""
        x, y = point
        return (int(x * self.width), int(y * self.height))
    
    def _draw_contour(self, draw: ImageDraw.ImageDraw, points: List[Tuple[float, float]], 
                      width: int = None, color: Tuple[int, int, int] = None):
        """Draw a smooth contour through multiple points."""
        if width is None:
            width = self.line_width
        if color is None:
            color = self.line_color
        
        scaled_points = [self._scale_point(p) for p in points]
        if len(scaled_points) >= 2:
            draw.line(scaled_points, fill=color, width=width, joint="curve")
    
    def _draw_ellipse_outline(self, draw: ImageDraw.ImageDraw, center: Tuple[float, float],
                             width: float, height: float, color: Tuple[int, int, int] = None):
        """Draw an ellipse outline."""
        if color is None:
            color = self.line_color
        
        cx, cy = self._scale_point(center)
        w = int(width * self.width)
        h = int(height * self.height)
        
        bbox = [cx - w//2, cy - h//2, cx + w//2, cy + h//2]
        draw.ellipse(bbox, outline=color, width=self.line_width)
    
    def draw_figure(self, draw: ImageDraw.ImageDraw) -> None:
        """
        Draw a high-fidelity wireframe human figure with anatomical accuracy.
        
        This creates a detailed wireframe showing body contours, muscle groups,
        and anatomical landmarks while remaining safe for all audiences.
        
        Args:
            draw: PIL ImageDraw object to draw on
        """
        # === HEAD AND NECK ===
        # Head (more detailed with facial features indication)
        head_center = (0.5, 0.08)
        self._draw_ellipse_outline(draw, head_center, 0.12, 0.08, self.line_color)
        
        # Face guideline
        face_center_x = 0.5
        self._draw_contour(draw, [
            (face_center_x, 0.04),
            (face_center_x, 0.12)
        ], self.detail_width, self.detail_color)
        
        # Neck with sternocleidomastoid indication
        neck_points_left = [(0.48, 0.12), (0.47, 0.16), (0.46, 0.18)]
        neck_points_right = [(0.52, 0.12), (0.53, 0.16), (0.54, 0.18)]
        self._draw_contour(draw, neck_points_left, self.line_width, self.line_color)
        self._draw_contour(draw, neck_points_right, self.line_width, self.line_color)
        
        # Trapezius line
        trap_line = [(0.46, 0.18), (0.5, 0.19), (0.54, 0.18)]
        self._draw_contour(draw, trap_line, self.detail_width, self.detail_color)
        
        # === TORSO - FRONT VIEW ===
        # Shoulders (deltoid contours)
        left_shoulder_outer = [
            (0.33, 0.18),
            (0.31, 0.20),
            (0.30, 0.23),
            (0.31, 0.25)
        ]
        right_shoulder_outer = [
            (0.67, 0.18),
            (0.69, 0.20),
            (0.70, 0.23),
            (0.69, 0.25)
        ]
        self._draw_contour(draw, left_shoulder_outer, self.line_width, self.line_color)
        self._draw_contour(draw, right_shoulder_outer, self.line_width, self.line_color)
        
        # Shoulder tops (clavicle area)
        clavicle_left = [(0.46, 0.18), (0.40, 0.19), (0.35, 0.19)]
        clavicle_right = [(0.54, 0.18), (0.60, 0.19), (0.65, 0.19)]
        self._draw_contour(draw, clavicle_left, self.detail_width, self.detail_color)
        self._draw_contour(draw, clavicle_right, self.detail_width, self.detail_color)
        
        # Chest/Pectoral contours
        left_pec_outer = [(0.38, 0.20), (0.36, 0.24), (0.37, 0.28)]
        left_pec_inner = [(0.46, 0.20), (0.44, 0.24), (0.43, 0.28)]
        right_pec_outer = [(0.62, 0.20), (0.64, 0.24), (0.63, 0.28)]
        right_pec_inner = [(0.54, 0.20), (0.56, 0.24), (0.57, 0.28)]
        
        self._draw_contour(draw, left_pec_outer, self.line_width, self.line_color)
        self._draw_contour(draw, left_pec_inner, self.detail_width, self.detail_color)
        self._draw_contour(draw, right_pec_outer, self.line_width, self.line_color)
        self._draw_contour(draw, right_pec_inner, self.detail_width, self.detail_color)
        
        # Ribcage/torso sides
        left_torso = [
            (0.37, 0.28),
            (0.38, 0.33),
            (0.39, 0.40),
            (0.40, 0.47)
        ]
        right_torso = [
            (0.63, 0.28),
            (0.62, 0.33),
            (0.61, 0.40),
            (0.60, 0.47)
        ]
        self._draw_contour(draw, left_torso, self.line_width, self.line_color)
        self._draw_contour(draw, right_torso, self.line_width, self.line_color)
        
        # Abdominal sections (rectus abdominis)
        ab_sections = [
            [(0.43, 0.30), (0.57, 0.30)],  # Upper abs
            [(0.43, 0.35), (0.57, 0.35)],  # Mid abs
            [(0.43, 0.40), (0.57, 0.40)],  # Lower mid abs
            [(0.43, 0.45), (0.57, 0.45)],  # Lower abs
        ]
        for section in ab_sections:
            self._draw_contour(draw, section, self.detail_width, self.detail_color)
        
        # Centerline (linea alba)
        self._draw_contour(draw, [(0.5, 0.20), (0.5, 0.49)], self.detail_width, self.detail_color)
        
        # Obliques
        oblique_lines_left = [
            [(0.40, 0.35), (0.42, 0.40)],
            [(0.40, 0.40), (0.42, 0.45)],
        ]
        oblique_lines_right = [
            [(0.60, 0.35), (0.58, 0.40)],
            [(0.60, 0.40), (0.58, 0.45)],
        ]
        for line in oblique_lines_left:
            self._draw_contour(draw, line, self.detail_width, self.detail_color)
        for line in oblique_lines_right:
            self._draw_contour(draw, line, self.detail_width, self.detail_color)
        
        # Waist/hip area
        waist_left = [(0.40, 0.47), (0.41, 0.50), (0.42, 0.53)]
        waist_right = [(0.60, 0.47), (0.59, 0.50), (0.58, 0.53)]
        self._draw_contour(draw, waist_left, self.line_width, self.line_color)
        self._draw_contour(draw, waist_right, self.line_width, self.line_color)
        
        # Pelvis (SFW - simplified geometric shape)
        pelvis_outline = [
            (0.42, 0.53),
            (0.43, 0.55),
            (0.57, 0.55),
            (0.58, 0.53)
        ]
        self._draw_contour(draw, pelvis_outline, self.line_width, self.line_color)
        self._draw_contour(draw, [(0.42, 0.53), (0.58, 0.53)], self.line_width, self.line_color)
        
        # === ARMS ===
        # Left arm
        # Upper arm (bicep/tricep contours)
        left_upper_arm_outer = [(0.31, 0.25), (0.29, 0.30), (0.28, 0.35), (0.28, 0.38)]
        left_upper_arm_inner = [(0.35, 0.25), (0.34, 0.30), (0.33, 0.35), (0.32, 0.38)]
        self._draw_contour(draw, left_upper_arm_outer, self.line_width, self.line_color)
        self._draw_contour(draw, left_upper_arm_inner, self.line_width, self.line_color)
        
        # Elbow
        left_elbow = [(0.28, 0.38), (0.30, 0.39), (0.32, 0.38)]
        self._draw_contour(draw, left_elbow, self.detail_width, self.detail_color)
        
        # Forearm
        left_forearm_outer = [(0.28, 0.38), (0.27, 0.43), (0.26, 0.48), (0.26, 0.52)]
        left_forearm_inner = [(0.32, 0.38), (0.31, 0.43), (0.30, 0.48), (0.29, 0.52)]
        self._draw_contour(draw, left_forearm_outer, self.line_width, self.line_color)
        self._draw_contour(draw, left_forearm_inner, self.line_width, self.line_color)
        
        # Wrist and hand
        left_wrist = [(0.26, 0.52), (0.27, 0.53), (0.29, 0.52)]
        self._draw_contour(draw, left_wrist, self.detail_width, self.detail_color)
        left_hand = [(0.27, 0.53), (0.26, 0.55), (0.25, 0.57)]
        self._draw_contour(draw, left_hand, self.line_width, self.line_color)
        
        # Right arm (mirror of left)
        right_upper_arm_outer = [(0.69, 0.25), (0.71, 0.30), (0.72, 0.35), (0.72, 0.38)]
        right_upper_arm_inner = [(0.65, 0.25), (0.66, 0.30), (0.67, 0.35), (0.68, 0.38)]
        self._draw_contour(draw, right_upper_arm_outer, self.line_width, self.line_color)
        self._draw_contour(draw, right_upper_arm_inner, self.line_width, self.line_color)
        
        right_elbow = [(0.72, 0.38), (0.70, 0.39), (0.68, 0.38)]
        self._draw_contour(draw, right_elbow, self.detail_width, self.detail_color)
        
        right_forearm_outer = [(0.72, 0.38), (0.73, 0.43), (0.74, 0.48), (0.74, 0.52)]
        right_forearm_inner = [(0.68, 0.38), (0.69, 0.43), (0.70, 0.48), (0.71, 0.52)]
        self._draw_contour(draw, right_forearm_outer, self.line_width, self.line_color)
        self._draw_contour(draw, right_forearm_inner, self.line_width, self.line_color)
        
        right_wrist = [(0.74, 0.52), (0.73, 0.53), (0.71, 0.52)]
        self._draw_contour(draw, right_wrist, self.detail_width, self.detail_color)
        right_hand = [(0.73, 0.53), (0.74, 0.55), (0.75, 0.57)]
        self._draw_contour(draw, right_hand, self.line_width, self.line_color)
        
        # === LEGS ===
        # Left leg
        # Hip/glute area
        left_hip_outer = [(0.42, 0.53), (0.41, 0.56), (0.41, 0.59)]
        self._draw_contour(draw, left_hip_outer, self.line_width, self.line_color)
        
        # Quadriceps contours
        left_quad_outer = [(0.41, 0.59), (0.40, 0.64), (0.40, 0.69), (0.41, 0.73)]
        left_quad_inner = [(0.45, 0.56), (0.45, 0.64), (0.45, 0.69), (0.45, 0.73)]
        self._draw_contour(draw, left_quad_outer, self.line_width, self.line_color)
        self._draw_contour(draw, left_quad_inner, self.line_width, self.line_color)
        
        # Quad muscle divisions
        quad_divisions_left = [
            [(0.42, 0.60), (0.44, 0.62)],
            [(0.42, 0.66), (0.44, 0.68)],
        ]
        for div in quad_divisions_left:
            self._draw_contour(draw, div, self.detail_width, self.detail_color)
        
        # Knee
        left_knee = [(0.41, 0.73), (0.43, 0.74), (0.45, 0.73)]
        self._draw_contour(draw, left_knee, self.detail_width, self.detail_color)
        
        # Calf (gastrocnemius)
        left_calf_outer = [(0.41, 0.73), (0.40, 0.77), (0.40, 0.84), (0.41, 0.90)]
        left_calf_inner = [(0.45, 0.73), (0.45, 0.77), (0.45, 0.84), (0.45, 0.90)]
        self._draw_contour(draw, left_calf_outer, self.line_width, self.line_color)
        self._draw_contour(draw, left_calf_inner, self.line_width, self.line_color)
        
        # Calf muscle shape
        left_calf_bulge = [(0.42, 0.78), (0.44, 0.78)]
        self._draw_contour(draw, left_calf_bulge, self.detail_width, self.detail_color)
        
        # Ankle
        left_ankle = [(0.41, 0.90), (0.42, 0.91), (0.44, 0.91), (0.45, 0.90)]
        self._draw_contour(draw, left_ankle, self.detail_width, self.detail_color)
        
        # Foot
        left_foot = [(0.43, 0.91), (0.42, 0.94), (0.40, 0.96)]
        self._draw_contour(draw, left_foot, self.line_width, self.line_color)
        
        # Right leg (mirror of left)
        right_hip_outer = [(0.58, 0.53), (0.59, 0.56), (0.59, 0.59)]
        self._draw_contour(draw, right_hip_outer, self.line_width, self.line_color)
        
        right_quad_outer = [(0.59, 0.59), (0.60, 0.64), (0.60, 0.69), (0.59, 0.73)]
        right_quad_inner = [(0.55, 0.56), (0.55, 0.64), (0.55, 0.69), (0.55, 0.73)]
        self._draw_contour(draw, right_quad_outer, self.line_width, self.line_color)
        self._draw_contour(draw, right_quad_inner, self.line_width, self.line_color)
        
        quad_divisions_right = [
            [(0.58, 0.60), (0.56, 0.62)],
            [(0.58, 0.66), (0.56, 0.68)],
        ]
        for div in quad_divisions_right:
            self._draw_contour(draw, div, self.detail_width, self.detail_color)
        
        right_knee = [(0.59, 0.73), (0.57, 0.74), (0.55, 0.73)]
        self._draw_contour(draw, right_knee, self.detail_width, self.detail_color)
        
        right_calf_outer = [(0.59, 0.73), (0.60, 0.77), (0.60, 0.84), (0.59, 0.90)]
        right_calf_inner = [(0.55, 0.73), (0.55, 0.77), (0.55, 0.84), (0.55, 0.90)]
        self._draw_contour(draw, right_calf_outer, self.line_width, self.line_color)
        self._draw_contour(draw, right_calf_inner, self.line_width, self.line_color)
        
        right_calf_bulge = [(0.58, 0.78), (0.56, 0.78)]
        self._draw_contour(draw, right_calf_bulge, self.detail_width, self.detail_color)
        
        right_ankle = [(0.59, 0.90), (0.58, 0.91), (0.56, 0.91), (0.55, 0.90)]
        self._draw_contour(draw, right_ankle, self.detail_width, self.detail_color)
        
        right_foot = [(0.57, 0.91), (0.58, 0.94), (0.60, 0.96)]
        self._draw_contour(draw, right_foot, self.line_width, self.line_color)
