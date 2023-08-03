import sys
import re
from operator import add, sub, mul, truediv

operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": truediv
}

def simple_calculator(a:str, b: str, operator: str) -> None:
    operation = operations.get(operator)
    if not operation:
        raise ValueError(f"Invalid operator! Operator must be one of {list(operations.keys())}")

    try:
        result = operation(float(a), float(b))
        print(f"{a} {operator} {b} = {round(result, 2)}")
    except ZeroDivisionError:
        print("You can't divide by zero!")


def is_number(s: str) -> bool:
    pattern = r'^[-+]?\d*\.?\d+$'
    return bool(re.match(pattern, s))

def validate_args(args: list[str]) :
    for arg in args:
        if not is_number(arg):
            raise ValueError(f"Invalid value! Arg must be a number, given argument: {arg}")

def main():
    if len(sys.argv) < 4:
        print("Usage: python calculator.py [argument1] [argument2] [operator]")
        return

    validate_args(sys.argv[1:3])
    simple_calculator(sys.argv[1], sys.argv[2], sys.argv[3])


"""To run this script, type in the terminal: python calculator.py 1 2 +
    For another operations is in the same way.
    For the multiplication operator you need to pass as follows 1 2 \*
    this is because the "*" character can be treated as a special character
    by the command line, and the shell is expanding it to filenames
    in the current directory
"""
if __name__ == "__main__":
    main()

