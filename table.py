def table(number: int)-> None:

    for i in range(1, 11):
        print(f"{number} * {i} = {_calculate_multiply(number, i)}")


def _calculate_multiply(number: int, multiplier: int) -> int:
    return number * multiplier


def main():
    number = int(input("Write a number: "))
    table(number)


if __name__ == "__main__":
    main()
