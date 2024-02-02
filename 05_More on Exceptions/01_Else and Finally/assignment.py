number1 = 0
number2 = 0
try:
    number1 = int(input("Enter a number:"))
    number2 = int(input("Enter another number:"))
except ValueError:
    print("You didn't enter a value..")

    print("An input was not correct")

else:
    print("You're good here dude, you entered a value.")
finally:
    print("The value is taken care of.")
try:
    print(number1, "Divided by", number2, "=", number1/number2)
except ZeroDivisionError:
    print("I can't do that bro, NOT EVEN A QUANTUM COMPUTER CAN DO THAT.....I think....")
else:
    print("There was no zero, you're good.")
finally:
    print("I'm gonna do something bad....something reaaal bad......something.........devious....")
