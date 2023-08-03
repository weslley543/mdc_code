from math import sqrt

def is_prime(number: int) -> bool:
    if number < 2:
        return False

    for k in range(2, int(sqrt(number)) + 1):
        if number % k == 0:
            return False

    return True


def print_first_10_prime_numbers():
    count = 0
    number = 2
    while count < 10:
        if is_prime(number):
            print(number)
            count += 1
        number += 1


def main():
    print_first_10_prime_numbers()

if __name__ == "__main__":
    main()
