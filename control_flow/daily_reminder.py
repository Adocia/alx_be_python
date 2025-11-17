task = input("Enter the task: ")
Finish project report
priority = input("Enter the priority (high, medium, low): ")
high
time_bound = input("Is the task time-bound? (yes or no): ")
yes
match priority.lower():
    case "high":
        reminder = f"Your task '{task}' is a HIGH priority task."
    case "medium":
        reminder = f"Your task '{task}' is a MEDIUM priority task."
    case "low":
        reminder = f"Your task '{task}' is a LOW priority task."
    case _:
        reminder = f"Your task '{task}' has an UNKNOWN priority."
if time_bound.lower() == "yes":
    reminder += " Finish project report' is a high priority task that requires immediate attention today!"
    print(reminder)
  reminder =  Finish project report' is a high priority task that requires immediate attention today!
