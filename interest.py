def calculate_interest(principal: float, interest_rate: float, month: int) -> float:
    return principal * (1 + interest_rate / 100) ** month

def main():
    principal = float(input("Enter the principal: "))
    interest_rate = float(input("Enter the interest rate: "))
    month = int(input("Enter the number of month(s): "))
    result = round(calculate_interest(principal, interest_rate, month), 2)
    print(f"The final amount is: {result}")

if __name__ == "__main__":
    main()
