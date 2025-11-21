"""
Example usage of the workout_generator package.

This script demonstrates how to generate workout images for various exercises.
"""

import os
from workout_generator import generate_workout_image, WorkoutImageGenerator, MuscleGroup


def main():
    """Generate example workout images."""
    
    # Create output directory
    output_dir = "examples/output"
    os.makedirs(output_dir, exist_ok=True)
    
    # Example 1: Bicep Curls
    print("Generating bicep curls image...")
    bicep_curls = generate_workout_image(
        "Bicep Curls",
        {
            MuscleGroup.BICEPS: 90,
            MuscleGroup.FOREARMS: 60,
        },
        save_path=os.path.join(output_dir, "bicep_curls.png")
    )
    
    # Example 2: Squats
    print("Generating squats image...")
    squats = generate_workout_image(
        "Squats",
        {
            MuscleGroup.QUADS: 95,
            MuscleGroup.GLUTES: 90,
            MuscleGroup.HAMSTRINGS: 70,
            MuscleGroup.CALVES: 40,
            MuscleGroup.ABS: 50,
        },
        save_path=os.path.join(output_dir, "squats.png")
    )
    
    # Example 3: Push-ups
    print("Generating push-ups image...")
    pushups = generate_workout_image(
        "Push-ups",
        {
            MuscleGroup.CHEST: 85,
            MuscleGroup.TRICEPS: 75,
            MuscleGroup.SHOULDERS: 65,
            MuscleGroup.ABS: 55,
        },
        save_path=os.path.join(output_dir, "pushups.png")
    )
    
    # Example 4: Plank
    print("Generating plank image...")
    plank = generate_workout_image(
        "Plank",
        {
            MuscleGroup.ABS: 90,
            MuscleGroup.OBLIQUES: 70,
            MuscleGroup.SHOULDERS: 60,
            MuscleGroup.QUADS: 50,
        },
        save_path=os.path.join(output_dir, "plank.png")
    )
    
    # Example 5: Deadlift
    print("Generating deadlift image...")
    deadlift = generate_workout_image(
        "Deadlift",
        {
            MuscleGroup.HAMSTRINGS: 95,
            MuscleGroup.GLUTES: 90,
            MuscleGroup.UPPER_BACK: 85,
            MuscleGroup.LATS: 80,
            MuscleGroup.FOREARMS: 75,
            MuscleGroup.ABS: 70,
        },
        save_path=os.path.join(output_dir, "deadlift.png")
    )
    
    # Example 6: Animation frames for shoulder press
    print("Generating shoulder press animation frames...")
    generator = WorkoutImageGenerator()
    shoulder_press_frames = generator.generate_animation_frames(
        {
            MuscleGroup.SHOULDERS: 95,
            MuscleGroup.TRICEPS: 70,
            MuscleGroup.ABS: 45,
        },
        num_frames=5,
        title="Shoulder Press"
    )
    
    for i, frame in enumerate(shoulder_press_frames):
        frame.save(os.path.join(output_dir, f"shoulder_press_frame_{i+1}.png"))
    
    print(f"\nAll example images have been saved to {output_dir}/")
    print("\nExample images generated:")
    print("  - bicep_curls.png")
    print("  - squats.png")
    print("  - pushups.png")
    print("  - plank.png")
    print("  - deadlift.png")
    print("  - shoulder_press_frame_1.png through shoulder_press_frame_5.png")


if __name__ == "__main__":
    main()
