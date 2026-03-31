def workout_routine():
    total_jacks = 100
    jacks_per_set = 10
    completed_jacks = 0

    while completed_jacks < total_jacks:
        print(f"Perform {jacks_per_set} jumping jacks.")
        completed_jacks += jacks_per_set
        if completed_jacks > total_jacks:
            completed_jacks = total_jacks

        tired_response = input("Are you tired? (yes/y or no/n): ").strip().lower()
        if tired_response in ['yes', 'y']:
            skip_response = input("Do you want to skip the remaining sets? (yes/y or no/n): ").strip().lower()
            if skip_response in ['yes', 'y']:
                print(f"You completed a total of {completed_jacks} jumping jacks.")
                return

        remaining_jacks = total_jacks - completed_jacks
        if remaining_jacks > 0:
            print(f"{remaining_jacks} jumping jacks remaining.")
        else:
            print("Congratulations! You completed the workout.")
            return

# Run the workout routine
workout_routine()