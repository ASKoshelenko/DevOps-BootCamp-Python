def is_palindrome(s):
    return s == s[::-1]

def main():
    input_string = input()
    print("yes" if is_palindrome(input_string) else "no")

if __name__ == "__main__":
    main()
