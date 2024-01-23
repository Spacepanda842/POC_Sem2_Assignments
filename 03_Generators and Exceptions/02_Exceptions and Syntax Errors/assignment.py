number_1 = int(input("Enter a number:"))
number_2 = int(input("Enter another number:"))
try:
    print(number_1, "Divided by", number_2, "=", int(number_1/number_2))
except ZeroDivisionError:
    print("Sorry, you divided by zero, that's literally impossible goofy. For example, if you have  and divide it by 10, YOU CAN'T DIVIDE ABSOLUTELY NOTHING, which means the answer is.......Hold up...it's zero💀")