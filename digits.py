def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

def main():
    n = int(input())
    print(sum_of_digits(n))

if __name__ == "__main__":
    main()
