#IterationAndRecursion Made by Alon Rehin for CIS 261

def recursive(num2):

    if num2 <= 0:
       return 1

    else:
        return num2*recursive(num2 - 1)
    

 

def interative(num1):

    if num1 == 0:
        return 1

    for Number in range(1, num1):
        num1 = num1*Number

    return num1

print("The recursive factorial of 0 is", (recursive(0)))
print("The recursive factorial of 5 is", (recursive(5)))
print("The recursive factorial of 10 is", (recursive(10)))
print("The recursive factorial of 25 is", (recursive(25)))
print("The recursive factorial of 50 is", (recursive(50)))
print("The recursive factorial of 100 is", (recursive(100)))
print()
print("The interative factorial of 0 is", (interative(0)))
print("The interative factorial of 5 is", (interative(5)))
print("The interative factorial of 10 is", (interative(10)))
print("The interative factorial of 25 is", (interative(25)))
print("The interative factorial of 50 is", (interative(50)))
print("The interative factorial of 100 is", (interative(100)))

