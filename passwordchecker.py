import string
import time

print("---  SIMPLE PASSWORD SCANNER WHICH WILL HELP YOU CREATE A STRONG PASSWORD ---")

while True:
    password = input("\nEnter password (or 'exit'): ")

    if password.lower() == "exit":
        break

    # --- BASIC SCORING SYSTEM ---
    score = 0

    # Length checks
    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1

    # Character variety checks
    if any(ch.isdigit() for ch in password):
        score += 1
    if any(ch.isupper() for ch in password):
        score += 1
    if any(ch in string.punctuation for ch in password):
        score += 1

    # --- RESULT MAPPING ---
    if score <= 2:
        rating = "Weak 🔴"
        crack_time = "Instant"
        hacker_cost = " free of cost (Anyone can try)"
        MY_OPINION = "Too easy to guess. Try something better."

    elif score <= 4:
        rating = "Medium 🟠"
        crack_time = "Around 2–3 days"
        hacker_cost = " (40 - 50) k rupees (Electricity + patience)"
        MY_OPINION = "Okay for small stuff, not for anything serious."

    else:
        rating = "Strong 🟢"
        crack_time = "Thousands of years"
        hacker_cost = "TOO MUCH COST (IN BILLIONS)"
        MY_OPINION = " your password is Super strong. You’re safe."

    # --- FAKE LOADING EFFECT ---
    print("Analyzing password", end="")
    for _ in range(3):
        time.sleep(0.4)
        print(".", end="")
    print(" done!")

    # --- OUTPUT ---
    print("-" * 30)
    print("1. RATING:      ", rating)
    print("2. CRACK TIME:  ", crack_time)
    print("3. HACKER COST: ", hacker_cost)
    print("4. MY_OPINION:     ",MY_OPINION)
    print("-" * 30)