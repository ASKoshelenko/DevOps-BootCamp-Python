def calculate_factorial(n):
    if n == 0:
        return 1
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

def main():
    n = int(input())
    print(calculate_factorial(n))

if __name__ == "__main__":
    main()
