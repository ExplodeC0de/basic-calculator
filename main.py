from colorama import Fore
import itertools
import threading
import time
import sys

done = False
#here is the animation
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rloading, please wait patiently ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
       

t = threading.Thread(target=animate)
t.start()

#long process here
time.sleep(10)
done = True
print('\r')
# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y

print(Fore.LIGHTGREEN_EX + "\nSelect operation.")
print(Fore.LIGHTGREEN_EX + "1.Add")
print(Fore.LIGHTGREEN_EX + "2.Subtract")
print(Fore.LIGHTGREEN_EX + "3.Multiply")
print(Fore.LIGHTGREEN_EX + "4.Divide")

while True:
    # take input from the user
    choice = input(Fore.LIGHTBLUE_EX + "Enter choice(1/2/3/4): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input(Fore.LIGHTYELLOW_EX + "Enter first number: "))
            num2 = float(input(Fore.LIGHTYELLOW_EX + "Enter second number: "))
        except ValueError:
            print(Fore.RED + "Invalid input. Please enter a number.")
            continue

        if choice == '1':
          print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
          print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
          print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
          print(num1, "/", num2, "=", divide(num1, num2))
         
         
             
         
       
        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input(Fore.LIGHTGREEN_EX + "Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    else:
        print(Fore.RED + "Invalid Input")
