# Type Error, Type Checking and Type Conversion

#len(1343) # TypeError

num_char = len(input("What is your name?\n"))
# print("Your name has " + num_char + " characters.") # TypeError: can only concatenate str
print(type(num_char)) # type check

# Type Conversion

new_num_char = str(num_char)
print("Your name has " + new_num_char + " characters.")

a = 123
print(type(a))

a = str(123)
print(type(a))

print(70 + float("100.5"))
print(str(70) + str(100))