def is_palindrome(word: str) -> bool :
    word = word.lower().replace(" ", "")

    return word == word[::-1]

def main():
    word = input("Enter a word: ")
    print("Is palindrome" if is_palindrome(word) else "Is not palindrome")

if __name__ == "__main__":
    main()
