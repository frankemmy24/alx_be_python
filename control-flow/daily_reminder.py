task = input("Enter your task: ").lower()
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high":
        reminder = f"'{task}' is a high priority task"
        if time_bound == "yes":
            reminder += "that requires immediate attention today!"
        else:
            reminder += "."
    case "medium":
        reminder = f"'{task}' is a medium priority task"
        if time_bound == "yes":
            reminder += "consider addressing it soon.!"
        else:
            reminder += " you can schedule it for later."
    case "low":
        reminder = f"'{task}' is a low priority task"
        if time_bound == "yes":
            reminder += "but it's important to complete it soon.!"
        else:
            reminder += " Consider completing it when you have free time."
    case _:
        reminder = "Invalid priority level, please enter 'high' , 'medium' , or 'low'. "
print(f"Reminder: {reminder}")

    
 