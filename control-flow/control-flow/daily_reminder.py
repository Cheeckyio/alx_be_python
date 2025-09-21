# daily_reminder.py
# A script to provide customized reminders for a single task based on priority and time sensitivity

# Prompt for a single task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

print()  # Add a blank line for better formatting

# Process the task based on priority using Match Case
match priority.lower():
    case "high":
        if time_bound.lower() == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Note: '{task}' is a high priority task. Consider completing it when you have free time.")
    
    case "medium":
        if time_bound.lower() == "yes":
            print(f"Reminder: '{task}' is a medium priority task that requires immediate attention today!")
        else:
            print(f"Note: '{task}' is a medium priority task. Consider completing it when you have free time.")
    
    case "low":
        if time_bound.lower() == "yes":
            print(f"Reminder: '{task}' is a low priority task that requires immediate attention today!")
        else:
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
    
    case _:
        print(f"Invalid priority level. Please restart and enter high, medium, or low.")