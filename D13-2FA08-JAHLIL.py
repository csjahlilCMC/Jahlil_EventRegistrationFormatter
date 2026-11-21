# --- STUDENT EVENT REGISTRATION SUMMARY ---
# General Information
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
section = input("Enter your section: ")

event_title = input("Enter your event title: ")
year = int(input("Enter the year: "))
month = int(input("Enter the month: "))
day = int(input("Enter the day: "))

# Version 1.0
print()
print("=== Student Event Registration Summary ===\n")
print("Name: ", first_name + " " + last_name)
print("Section: ", section)
print("Event: ", event_title)
print("Date: ", month, day, year)
print("Language Used: Python\n")
print("Registration record created successfully.")
print()