# --- STUDENT EVENT REGISTRATION SUMMARY ---
# General Information
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
section = input("Enter your section: ")

event_title = input("Enter your event title: ")
year = int(input("Enter the year: "))
month = int(input("Enter the month: "))
day = int(input("Enter the day: "))

# Version 3.0
clean_name = first_name.strip().title() + " " + last_name.strip().title()
clean_section = section.strip().upper()

from datetime import datetime
event_date = datetime(year, month, day)

print("=== Student Event Registration Summary ===\n")
print("Name: ", clean_name)
print("Name Code: ", clean_name.upper())
print("Section: ", clean_section)
print("Event: ", event_title.upper())
print("Event Date: ", event_date.strftime("%B %d, %Y"))
print("Language Used: Python")
print("String Feature used: strip(), title(), upper()")
print("Date/Time Feature Used: datetime\n")
print("Registration record created successfully.")
print()
