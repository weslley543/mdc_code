from statistics import mean

import sys


def average(student_grades: list[float]) -> float:
    return round(mean(student_grades), 2)


def parse_args(args: list[str]) -> list[float]:
    grades = []
    for arg in args:
        try:
            parsed_arg = float(arg)
            grades.append(parsed_arg)
        except ValueError:
            raise ValueError(f"Invalid value! Arg must be a number, given argument: {arg}")
    return grades


def main():
    if len(sys.argv) < 4:
        print("Usage: python average.py [argument1] [argument2] [argument3]")
        return
    grades = parse_args(sys.argv[1:])
    print(f"The average is: {average(grades)}")


if __name__ == "__main__":
    main()
