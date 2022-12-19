'''
Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

It will take your current age as the input and output a message with our time left in this format:

    You have x days, y weeks, and z months left.

Where x, y and z are replaced with the actual calculated numbers.
1 year = 365 days , 12 months and 52 weeks
'''

# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#print(type(age))
days = int(age) * 365
months = int(age) * 12
weeks = int(age) * 52

years_total = 90
days_total = years_total * 365
months_total = years_total * 12
weeks_total = years_total * 52

days_left = days_total - days 
months_left = months_total - months 
weeks_left = weeks_total - weeks

print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")
