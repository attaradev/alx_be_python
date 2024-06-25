task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
        if time_bound == "yes":
            reminder += " that requires immediate attention today!"
        else:
            reminder += "."
    case "medium":
        reminder = f"'{task}' is a medium priority task"
        if time_bound == "yes":
            reminder += " that requires attention today."
        else:
            reminder += "."
    case "low":
        if time_bound == "yes":
            reminder = f"'{task}' is a low priority task that requires attention today."
        else:
            reminder = f"'{task}' is a low priority task. Consider completing it when you have free time."
    case _:
        reminder = "Invalid priority level entered."

print("Reminder:", reminder)
