
initial_total = 0
print("--- Running Total Calculator ---")
print("Enter numbers to add them up. Type 'done' to see the total.")
while True:
    user_input = input("Enter a number or 'done': ")
    if user_input == "done":
        print("--- Final Calculation ---")
        print(f"The final sum of all numbers is: {initial_total}")
        break
    else:
        initial_total = float(user_input) + initial_total
        print(f"Current total: {initial_total:.1f}")