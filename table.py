# Program to generate a multiplication table

# Taking input from the user
num = int(input("Enter the number to generate its multiplication table: "))

# Printing the multiplication table from 1 to 10
print(f"\nMultiplication Table for {num}:\n")

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
