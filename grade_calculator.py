def grade_cal(num):
    if 0 <= num <= 59:
        return "F", "You are Fail! Need to Work Hard!"

    elif 60 <= num <= 69:
        return "D", "You are about to fail! Need to concentrate on study!"

    elif 70 <= num <= 79:
        return "C", "You are Average! Keep improving!"

    elif 80 <= num <= 89:
        return "B", "Very Good! Keep it up!"

    elif 90 <= num <= 100:
        return "A", "Excellent! You are awesome!"


# Day 2: Input
name = input("Enter student name: ")

# Day 4: Validation using while loop
while True:
    marks = int(input("Enter marks (0-100): "))
    
    if 0 <= marks <= 100:
        break
    else:
        print("Invalid marks! Please enter between 0-100.")

# Day 5: Final Output
grade, message = grade_cal(marks)

print(f"\nRESULT FOR {name}:")
print(f"Marks: {marks}/100")
print(f"Grade: {grade}")
print(f"Message: {message}")