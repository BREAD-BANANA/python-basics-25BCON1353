x = input("Please enter a number: ")
fact = int (1)  

for i in range(1, int(x) + 1):

    fact *= i 
print(f"The factorial of {x} is {fact}")
