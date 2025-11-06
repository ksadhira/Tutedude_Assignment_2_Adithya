#Print the number (int) is even or odd
'''1. 	Takes an integer input from the user.
2. 	Checks whether the number is even or odd using an if-else statement.
3. 	Displays the result accordingly.'''

num_input = int(input("Enter a Number to check if it is EVEN or ODD: "))

'''if num_input % 2 == 0:
    print(f"The Entered number {num_input} is EVEN!!!")
else:
    print(f"The Entered number {num_input} is ODD!!!")'''


#Ternary Operation

print(f"The Entered number {num_input} is EVEN!!!") if num_input % 2 == 0 else print(f"The Entered number {num_input} is ODD!!!")