def min(a, b):
    if(a < b):
        return a
    else:
        return b

def average(a, b):
    return (a + b) / 2

number1 = float(input("Enter a decimal number: "))
number2 = float(input("Enter another decimal number: "))
print(average(number1, number2))
