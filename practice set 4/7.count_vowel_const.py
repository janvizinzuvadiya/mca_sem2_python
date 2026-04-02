# 7) Accept the string from the user; display the count of vowels and consonants.

import time

def print_header(title):
    print("=" * 50)
    print(f"{title:^50}")
    print("=" * 50)

def main():
    print_header("Vowel and Consonant Counter")
    print("Let's count the vowels and consonants in your string.")
    try:
        string = input("👉 Please enter a string: ")
    except ValueError:
        print("\n❌ Error: Please enter a valid string!")
        return

    print("\n⏳ Analyzing...\n")
    time.sleep(0.5)

    print("-" * 50)
    vowels = 0
    consonants = 0
    for char in string:
        if(char.lower() in "aeiou"):
            vowels += 1
        elif(char.isalpha()):
            consonants += 1
    print(f"The number of vowels is {vowels}")
    print(f"The number of consonants is {consonants}")
    print("-" * 50)
    print("\nThank you for using the program! 👋\n")

if __name__ == "__main__":
    main()