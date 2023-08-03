import re
import sys


def vowels_counter(word: str) -> int:
    vowels = re.findall(r'[aeiouAEIOUáéíóúÁÉÍÓÚâêîôûÂÊÎÔÛãẽĩõũÃẼĨÕŨ]', word)
    return len(vowels)


def main():
    if len(sys.argv) < 2:
        print("Usage: python vowels_counter.py [argument1]")
        return

    number_of_vowels = vowels_counter(sys.argv[1])
    print(f"The number of vowels in this word is: {number_of_vowels}")


if __name__ == "__main__":
    main()
