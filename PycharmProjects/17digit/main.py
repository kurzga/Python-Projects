from decimal import Decimal, getcontext, ROUND_FLOOR

class DecimalNumber:
    def __init__(self, value, precision):
        getcontext().prec = precision + 1  # Set precision to handle rounding
        decimal_value = Decimal(str(value))
        self.whole_part = decimal_value.to_integral_value(rounding=ROUND_FLOOR)
        self.decimal_part = (decimal_value - self.whole_part) * 10**precision
        self.decimal_places = precision

def add_decimals(result, num1, num2):
    result.whole_part = num1.whole_part + num2.whole_part
    result.decimal_part = num1.decimal_part + num2.decimal_part

    while result.decimal_part >= 10**result.decimal_places:
        result.decimal_part /= 10
        result.decimal_places -= 1

def print_decimal(num):
    print(f"{num.whole_part}.{int(num.decimal_part):0{num.decimal_places}d}")

if __name__ == "__main__":
    num1 = DecimalNumber("0.5", 17)
    num2 = DecimalNumber("0.2", 17)
    result = DecimalNumber("0", 17)

    add_decimals(result, num1, num2)

    print("Result:", end=" ")
    print_decimal(result)
