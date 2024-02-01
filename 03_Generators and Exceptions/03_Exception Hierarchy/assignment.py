number1 = 0
number2 = 0
try:
    number1 = int(input("Enter a number:"))
    number2 = int(input("Enter another number:"))
except ValueError:
    print("You didn't enter a value..")
try:
    print(number1, "Divided by", number2, "=", number1/number2)
except ZeroDivisionError:
    print("I can't do that bro, NOT EVEN A QUANTUM COMPUTER CAN DO THAT.....I think....")