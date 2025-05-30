task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high" | "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a {priority} priority task that 
requires immediate attention today!")
        else:
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case "high" | "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a {priority} priority task that 
requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a {priority} priority task.")
    case "low":
        if time_bound == "yes":
            print(f"Note: '{task}' is a low priority task, but you can 
plan it for later today.")
        else:
            print(f"Note: '{task}' is a low priority task. Consider 
completing it when you have free time.")
    case _:
        print(f"Reminder: '{task}' has an unknown priority level.")

