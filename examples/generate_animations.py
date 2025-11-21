"""
Generate animated GIF examples for README.
"""

import os
from workout_generator import WorkoutImageGenerator, MuscleGroup


def main():
    """Generate animated GIF examples for README."""
    
    # Create output directory
    output_dir = "examples/output"
    os.makedirs(output_dir, exist_ok=True)
    
    # Initialize generator
    generator = WorkoutImageGenerator(width=400, height=800)
    
    # Example 1: Seated Bicep Curls Animation
    print("Generating seated bicep curls animation...")
    bicep_frames = generator.generate_animation_frames(
        {
            MuscleGroup.BICEPS: 95,
            MuscleGroup.FOREARMS: 70,
            MuscleGroup.SHOULDERS: 30,
        },
        num_frames=20,
        title="Seated Bicep Curls"
    )
    
    # Save as animated GIF
    bicep_frames[0].save(
        os.path.join(output_dir, "seated_bicep_curls.gif"),
        save_all=True,
        append_images=bicep_frames[1:],
        duration=200,  # 200ms per frame
        loop=0  # Loop forever
    )
    print(f"  Saved: {os.path.join(output_dir, 'seated_bicep_curls.gif')}")
    
    # Also save individual frames
    for i, frame in enumerate(bicep_frames):
        frame.save(os.path.join(output_dir, f"seated_bicep_curls_frame_{i+1:02d}.png"))
    
    # Example 2: Sit-ups Animation
    print("Generating sit-ups animation...")
    situp_frames = generator.generate_animation_frames(
        {
            MuscleGroup.ABS: 100,
            MuscleGroup.OBLIQUES: 75,
            MuscleGroup.HIP_FLEXORS: 80,
        },
        num_frames=20,
        title="Sit-ups"
    )
    
    # Save as animated GIF
    situp_frames[0].save(
        os.path.join(output_dir, "situps.gif"),
        save_all=True,
        append_images=situp_frames[1:],
        duration=200,  # 200ms per frame
        loop=0  # Loop forever
    )
    print(f"  Saved: {os.path.join(output_dir, 'situps.gif')}")
    
    # Also save individual frames
    for i, frame in enumerate(situp_frames):
        frame.save(os.path.join(output_dir, f"situps_frame_{i+1:02d}.png"))
    
    print(f"\nAnimations generated successfully!")
    print(f"Output directory: {output_dir}/")
    print("\nGenerated files:")
    print("  - seated_bicep_curls.gif (animated)")
    print("  - situps.gif (animated)")
    print("  - Individual frames for both exercises")


if __name__ == "__main__":
    main()
