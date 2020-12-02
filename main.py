# Create a program  tells us how many days, weeks, months we have left if we live until 90 years old.

age = input("What is your current age? ")
# converting str to int.

new_age = int(age)

days = (90 - new_age) * 356
weeks = (90 - new_age) * 52
months = (90 - new_age) * 12

print(f"You have {days} days, {weeks} weeks, and {months} months left")
