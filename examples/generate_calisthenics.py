"""
Generate images for all predefined calisthenics exercises.
"""

import os
from workout_generator import generate_workout_image, list_exercises


def main():
    """Generate images for all calisthenics exercises."""
    
    # Create output directory
    output_dir = "examples/output/calisthenics"
    os.makedirs(output_dir, exist_ok=True)
    
    print("Generating images for all calisthenics exercises...\n")
    
    # Get all exercises grouped by difficulty
    for difficulty in ["beginner", "intermediate", "advanced"]:
        exercises = list_exercises(difficulty=difficulty)
        print(f"\n{difficulty.upper()} EXERCISES ({len(exercises)} exercises)")
        print("=" * 60)
        
        for exercise in exercises:
            print(f"  Generating: {exercise.name}...")
            filename = exercise.name.lower().replace(" ", "_").replace("-", "_") + ".png"
            filepath = os.path.join(output_dir, filename)
            
            try:
                generate_workout_image(
                    exercise,
                    save_path=filepath
                )
                print(f"    ✓ Saved: {filename}")
            except Exception as e:
                print(f"    ✗ Error: {e}")
    
    # Also create a summary showing all exercises
    print(f"\n{'=' * 60}")
    print(f"All exercise images saved to: {output_dir}/")
    print(f"{'=' * 60}\n")
    
    # List all generated files
    files = sorted([f for f in os.listdir(output_dir) if f.endswith('.png')])
    print(f"Generated {len(files)} images:")
    for i, f in enumerate(files, 1):
        print(f"  {i:2d}. {f}")


if __name__ == "__main__":
    main()
