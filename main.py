from termcolor import colored

def main():
    """Find age category."""
    age = int(input("Enter your age: \n"))

    if age < 2:
        print("You are a baby.")
    elif 2 <= age <= 12:
        print("You are a child.")
    elif 13 <= age <= 19:
        print("You are a teenager.")
    else:
        print("You are an adult.")

if __name__ == "__main__":
    print(colored("Age category detector", "blue"))  # Highlight the caption in blue
    main()
