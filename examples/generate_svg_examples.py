"""
Example script demonstrating SVG generation for workout images.

SVG files are scalable vector graphics that can be displayed at any resolution
without loss of quality.
"""

import os
from workout_generator import generate_workout_svg, SVGWorkoutImageGenerator, get_exercise


def main():
    """Generate example SVG workout images."""
    
    # Create output directory
    output_dir = "examples/output/svg"
    os.makedirs(output_dir, exist_ok=True)
    
    print("Generating SVG workout images...\n")
    
    # Example 1: Push-up
    print("Generating Push-up SVG...")
    generate_workout_svg(
        "Push-up",
        save_path=os.path.join(output_dir, "push_up.svg")
    )
    print(f"  ✓ Saved: push_up.svg")
    
    # Example 2: Squat
    print("Generating Squat SVG...")
    generate_workout_svg(
        "Squat",
        save_path=os.path.join(output_dir, "squat.svg")
    )
    print(f"  ✓ Saved: squat.svg")
    
    # Example 3: Pull-up
    print("Generating Pull-up SVG...")
    generate_workout_svg(
        "Pull-up",
        save_path=os.path.join(output_dir, "pull_up.svg")
    )
    print(f"  ✓ Saved: pull_up.svg")
    
    # Example 4: Plank
    print("Generating Plank SVG...")
    generate_workout_svg(
        "Plank",
        save_path=os.path.join(output_dir, "plank.svg")
    )
    print(f"  ✓ Saved: plank.svg")
    
    # Example 5: Generate animation frames as SVG
    print("\nGenerating Bicep Curl animation frames as SVG...")
    generator = SVGWorkoutImageGenerator()
    exercise = get_exercise("chin_up")  # Use an available exercise
    
    generator.generate_animation_frames(
        exercise.muscle_activations,
        num_frames=10,
        title=exercise.name,
        output_dir=os.path.join(output_dir, "chin_up_animation")
    )
    print(f"  ✓ Saved 10 animation frames to chin_up_animation/")
    
    print(f"\n{'=' * 60}")
    print(f"All SVG images saved to: {output_dir}/")
    print(f"{'=' * 60}\n")
    print("SVG files can be:")
    print("  - Opened in any modern web browser")
    print("  - Edited in vector graphics software (Inkscape, Adobe Illustrator)")
    print("  - Scaled to any size without quality loss")
    print("  - Converted to PNG with: cairosvg input.svg -o output.png")


if __name__ == "__main__":
    main()
