# While concepts

count = 0
while count <= 6:
    if count == 6:
        break
    print(count)
    count += 1
# If else statement
age = 16

if age >= 18:
    print("Eligible to vote.")
else:
    print("Eligible not to vote.")

#shorthand ifelse statement
marks = 45
student = "pass" if marks >=40 else "fail"
print(f"Result: {student}")

#elif statement

year = 1997
if year <= 1980:
    print("Generation X.")
elif year <=1996:
    print("Millenial.")
elif year <= 2012:
    print("Gen Z.")
else:
    print("Gen Alpha.")

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




