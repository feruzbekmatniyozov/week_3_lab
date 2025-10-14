print("--- Triangle Pattern Printer ---")

input_height = int(input("Enter the desired height of the triangle: "))

for height in range(input_height):
    for horizontal_line in range(height+1):
        print("* ", end="")
    print()