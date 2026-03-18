Student Grading System
Project Overview

This project is a Python-based Student Grading System that takes student marks as input and returns a grade (A, B, C, D, F) along with encouraging messages.

Objectives:

Implement grading logic using if-elif-else
Validate user input (marks between 0–100)
Use functions for modular coding
Handle invalid input using while loop
Provide motivational feedback to students

 Setup Instructions
 Requirements:
Python 3.x installed

How to Run:

Copy the code into a file:
grading_system.py
Open terminal / command prompt
Run the program:
python grading_system.py
Enter:

Student name

Marks (0–100)

Code Structure
project-folder/

 grading_system.py   # Main program file
 README.md      # Project documentation
 test_cases.txt  # To test the program
 screenshots.png  # Working project SS 

🔹 Key Components:

Function: grade_cal(num) → calculates grade & message

Input System → takes user input

Validation Loop → ensures marks are valid

Output Section → displays result

Visual Documentation
Sample Input:
Enter student name: Anubhav
Enter marks (0-100): 85

 Sample Output:
RESULT FOR Anubhav:
Marks: 85/100
Grade: B
Message: Very Good! Keep it up!
 Invalid Input Example:
Enter marks (0-100): 120
Invalid marks! Please enter between 0-100.
 Technical Details
 Algorithm:

Take student name input

Use while True loop for marks input

Validate marks range (0–100)

Call function grade_cal()

Return grade and message

Display result

Data Structures:

Basic variables (int, string)

Function returning tuple (grade, message)

Architecture:

Modular design

Input Layer

Validation Layer

Processing Layer (Function)

Output Layer

🧪 Testing Evidence
✔ Test Cases:
Input Marks	Expected Grade	Result
45	F	Pass ✅
65	D	Pass ✅
75	C	Pass ✅
85	B	Pass ✅
95	A	Pass ✅
-10	Invalid	Pass ✅
150	Invalid	Pass ✅
🔍 Edge Cases Tested:

Negative numbers 

Marks above 100 

Boundary values (0, 59, 60, 100) ✅

🚀 Features

✔ Simple and beginner-friendly

✔ Input validation using loop

✔ Clean function-based design

✔ Encouraging messages for students

📈 Future Improvements

Add multiple student records

Store results in file (CSV/Database)

Add percentage calculation


👨‍💻 Author

Anubhav Kumar