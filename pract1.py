def say_hello():
    print("Hello World")


def say_bye():
    print("Goodbye Mars")


# A simple kilograms to ounces conversion program
# It asks for a weight in kilograms (for example 10)
# and converts it to ounces (352.74)
def kilos_to_ounces():
    kilos = float(input("Enter a weight in kilograms: "))
    ounces = kilos * 35.274
    print("The weight in ounces is", ounces)


def count():
    for number in range(10):
        print("Number is now:", number)


# A simple euros to pounds conversion program
# It asks for a value in euros (for example 10)
# and converts it to pounds (8.7)
def euros_to_pounds():
    euros = float(input("Enter a value in euros: "))
    pounds = euros * 0.87
    print("The value in pounds is", pounds)


# Write your code here
