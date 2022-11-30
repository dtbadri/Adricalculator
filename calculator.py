# ADRI BASIC CALCULATOR
# IM VERY BORED LOL

import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

print(f"{Fore.CYAN}Select an operation to perform:")
print(Fore.RED + "1. ADD")
print(Fore.YELLOW + "2. MULTIPLY")
print(Fore.MAGENTA + "3. DIVIDE")
print(Fore.GREEN + "4. SUBTRACT")

operation = input("Select :")

if operation == "1":
    num1 = input("Enter firts number: ")
    num2 = input("Enter second number: ") 
    print("The sum is " + str(int(num1) + int(num2)))
elif operation == "2":
    num1 = input("Enter firts number: ")
    num2 = input("Enter second number: ") 
    print("The sum is " + str(int(num1) * int(num2)))
elif operation == "3":
    num1 = input("Enter firts number: ")
    num2 = input("Enter second number: ") 
    print("The sum is " + str(int(num1) / int(num2)))
elif operation == "4":
    num1 = input("Enter firts number: ")
    num2 = input("Enter second number: ") 
    print("The sum is " + str(int(num1) - int(num2)))
else:
    print("ERR")