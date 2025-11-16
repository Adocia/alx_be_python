task = input("Enter the task description: ")
Finish project report
priority = input("Enter the task priority (high, medium, low): ")
high
time_bound = input("Is the task time-bound? (yes or no): ")
yes
match priority.lower():
    case "high":
        reminder = "High priority task: " + task
    case "medium":
        reminder = "Medium priority task: " + task
    case "low":
        reminder = "Low priority task: " + task
    case _:
        reminder = "Task: " + task

if time_bound.lower() == "yes":
    reminder = reminder + " - This task is time-bound!"

print(reminder)
Reminder: 'Finish project report' is a priority task that requires immediate attention today!