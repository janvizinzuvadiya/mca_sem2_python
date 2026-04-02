# 13) Accept numbers from the user; display the sum of the entered numbers.

import time

def print_header(title):
    print("=" * 50)
    print(f"{title:^50}")
    print("=" * 50)

def main():
    print_header("Vowel and Consonant Counter")
    print("Let's count the vowels and consonants in your string.")
    try:
        num = int(input("👉 Please enter : "))
    except ValueError:
        print("\n❌ Error: Please enter a valid string!")
        return