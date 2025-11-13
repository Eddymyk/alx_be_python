task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:

    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Note: '{task}' is a high priority task. Plan to complete.")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a medium priority task that should be done today if possible.")
        else:
            print(f"Note: '{task}' is a medium priority task. Try to do it this week.")
    case "low":
        if time_bound == "yes":
            print(f"Tip: '{task}' is a low priority but time-bound task. Schedule it when convenient.")
        else:
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
    case _:
        print("Invalid priority level entered. Please choose high, medium, or low.")