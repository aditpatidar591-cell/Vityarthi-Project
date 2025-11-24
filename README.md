# Vityarthi-Project
Simple Password Stregth Checker
A Python Program designed to assess the strength of a user-provided password based on its length and character variety, providing an instant rating, estimated crack time, and security advice.

Features
Strength Scoring: Uses a basic, cumulative scoring system based on length and character types (digits, uppercase letters, special characters).

Intuitive Rating: Maps the score to clear ratings: Weak , Medium , and Strong .

Security Feedback: Provides hypothetical estimates for crack time and hacker cost to illustrate the importance of strong passwords.

Interactive Interface: Runs in an infinite loop, allowing users to test multiple passwords until they type 'exit'.

 How It Works
The script assigns points (up to a maximum of 5) for the following criteria:

Criterion	Points
Password length ≥8 characters	+1
Password length ≥12 characters	+1
Contains at least one Digit	+1
Contains at least one Uppercase letter	+1
Contains at least one Special Character (Punctuation)	+1

Export to Sheets

Rating Logic
Score	Rating	Advice
≤2	Weak 	Too easy to guess. Try something better.
3 - 4	Medium 	Okay for small stuff, not for anything serious.
5	Strong 	Your password is Super strong. You’re safe.

Export to Sheets

Getting Started
Prerequisites
Python 3.x must be installed on your system.

Installation and Running
Save the Code: Save the provided code into a file named password_scanner.py.

Run from Terminal: Open your terminal or command prompt, navigate to the directory where you saved the file, and execute the script:

Bash

python password_scanner.py
Example Usage
---  SIMPLE PASSWORD SCANNER WHICH WILL HELP YOU CREATE A STRONG PASSWORD ---

Enter password (or 'exit'): password
Analyzing password... done!
------------------------------
1. RATING:       Weak 
2. CRACK TIME:   Instant
3. HACKER COST:   free of cost (Anyone can try)
4. MY_OPINION:       Too easy to guess. Try something better.
------------------------------

Enter password (or 'exit'): P@$$w0rd1234
Analyzing password... done!
------------------------------
1. RATING:       Strong 
2. CRACK TIME:   Thousands of years
3. HACKER COST:   TOO MUCH COST (IN BILLIONS)
4. MY_OPINION:       your password is Super strong. You’re safe.
------------------------------
 Dependencies
This script uses only standard Python libraries and has no external dependencies:

THANK YOU.




