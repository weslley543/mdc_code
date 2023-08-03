def factorial(number: int)-> int:
    if number == 0:
        return 1
    return number * factorial(number - 1)

def main():
    number = int(input("Enter a number: "))
    print(f"The factorial of {number} is {factorial(number)}")

if __name__ == "__main__":
    main()
