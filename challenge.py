# The basic functionality of this code is complete, BUT it is not very DRY
# Your task to refactor this code so that it is DRY


student_name = input("Student name? ")
student_name = student_name.strip()  # This will remove any leading or trailing spaces in a string.
student_name = student_name.title()  # This will capitalize the first letter of each word.
if not student_name:  # An empty string counts as being false. So this is making sure they typed something.
    student_name = input("Student name? ")
    student_name = student_name.strip()
    student_name = student_name.title()
print(f"You have entered the student name as {student_name}.")

parent_or_guardian_name = input("Parent or Guardian name? ")
parent_or_guardian_name = parent_or_guardian_name.strip()
parent_or_guardian_name = parent_or_guardian_name.title()
if not parent_or_guardian_name:
    parent_or_guardian_name = input("Parent or Guardian name? ")
    parent_or_guardian_name = parent_or_guardian_name.strip()
    parent_or_guardian_name = parent_or_guardian_name.title()
print(f"You have entered the parent or guardian name as {parent_or_guardian_name}.")

city_name = input("City? ")
city_name = city_name.strip()
city_name = city_name.title()
if not city_name:
    city_name = input("City? ")
    city_name = city_name.strip()
    city_name = city_name.title()
print(f"You have entered the city as {city_name}.")

state_name = input("State? ")
state_name = state_name.strip()
state_name = state_name.title()
if not state_name:
    state_name = input("State? ")
    state_name = state_name.strip()
    state_name = state_name.title()
print(f"You have entered the city as {state_name}.")

country_name = input("Country? ")
country_name = country_name.strip()
country_name = country_name.title()
if not state_name:
    country_name = input("Country? ")
    country_name = country_name.strip()
    country_name = country_name.title()
print(f"You have entered the country as {country_name}.")

print(f"Thank you for completing the form. Good bye.")
