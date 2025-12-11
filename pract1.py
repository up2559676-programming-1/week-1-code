from typing import Mapping, Sequence


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


def say_name() -> None:
    print("Oliver")


def say_hello_2() -> None:
    print("hello")
    print("world")


def float_input(prompt: str) -> float:
    return float(input(prompt))


def dollars_to_pounds() -> None:
    exchange_rate = 1.35

    dollars = float_input("Enter the amount of dollars to convert $")
    print(f"Pounds: {round(dollars / exchange_rate, 2)}")


def sum_and_difference() -> None:
    num1 = float_input("Enter first number: ")
    num2 = float_input("Enter second number: ")
    print(f"Sum: {num1 + num2} | Diff: {num1 - num2}")


def int_input(prompt: str) -> int:
    return int(input(prompt))


def change_counter() -> None:
    coins = [1, 2, 5]

    total = 0
    for coin in coins:
        total += int_input(f"Enter the quantity of {coin}p coins: ") * coin

    print(f"Total: {total}p")


def ten_hellos():
    for _ in range(10):
        print("Hello World")


def zoom():
    num = int_input("Enter number of zooms to print: ")
    for i in range(num):
        print(f"zoom {i + 1}")


def count_to():
    target = int_input("Enter target number: ")
    for i in range(1, target + 1):
        print(i)


def count_from_to():
    start = int_input("Enter start number: ")
    end = int_input("Enter final number (inclusive): ")

    for i in range(start, end + 1):
        print(i)


def pretty_table(data: Sequence[Mapping[str, object]]) -> str:
    if not data:
        return ""

    headers = list(data[0].keys())

    rows = [headers] + [[str(row.get(h, "")) for h in headers] for row in data]
    col_widths = [max(len(str(cell)) for cell in col) for col in zip(*rows)]

    def format_row(row: list[str]) -> str:
        return " | ".join(cell.ljust(width) for cell, width in zip(row, col_widths))

    output_lines: list[str] = []
    output_lines.append(format_row(rows[0]))  # Header row
    output_lines.append("-+-".join("-" * width for width in col_widths))  # Separator
    for row in rows[1:]:
        output_lines.append(format_row(row))

    return "\n".join(output_lines)


def weights_table():
    start = 10
    end = 100
    step = 10
    kg_to_oz = 35.274

    data: list[dict[str, object]] = []
    for weight in range(start, end + step, step):
        data.append({"Kg": weight, "Oz": round(weight * kg_to_oz, 2)})

    print(pretty_table(data))


def future_value():
    interest_rate = 3.5
    interest_mult = 1.0 + interest_rate / 100.0

    amount = int_input("Enter the initial amount: ")
    years = int_input("Enter the number of years to invest: ")

    total = amount
    for _ in range(years):
        total *= interest_mult

    print(f"Amount after {years} years: {round(total, 2)}")


say_name()
say_hello_2()
dollars_to_pounds()
sum_and_difference()
change_counter()
ten_hellos()
zoom()
count_to()
count_from_to()
weights_table()
future_value()
