# While concepts

count = 0
while count <= 6:
    if count == 6:
        break
    print(count)
    count += 1
# If else statement
age = 25

if age >= 30:
    print("He/She is a minor.")
else:
    print("He/She is a major.")

#shorthand ifelse statement
marks = 45
student = "pass" if marks ==40 else "fail"
print(f"Result: {student}")

#elif statement

year = 2024
if year <= 1980:
    print("Generation X.")
elif year <=1996:
    print("Millenial.")
elif year <= 2012:
    print("Gen Z.")
elif year <= 2024:
    print("Gen Alpha.")
else:
    print("Gen Beta")

# nested if statement

age = 60
is_policy = True

if age >= 40 and age<=60:
    if age >= 60:
        print("he will retire.")
    else:
        print("he's retirement will take time.")
else:
    print("he will not retire.")




