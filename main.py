class PythonTasks:

    @staticmethod
    def calculate_factorial(n):
        if n == 0:
            return 1
        factorial = 1
        for i in range(1, n + 1):
            factorial *= i
        return factorial

    @staticmethod
    def sum_of_digits(n):
        return sum(int(digit) for digit in str(n))

    @staticmethod
    def is_palindrome(s):
        return s == s[::-1]

    @staticmethod
    def process_list_commands(commands):
        lst = []
        for command in commands:
            command = command.split()
            if command[0] == "insert":
                lst.insert(int(command[1]), int(command[2]))
            elif command[0] == "print":
                print(lst)
            elif command[0] == "remove":
                lst.remove(int(command[1]))
            elif command[0] == "append":
                lst.append(int(command[1]))
            elif command[0] == "sort":
                lst.sort()
            elif command[0] == "pop":
                lst.pop()
            elif command[0] == "reverse":
                lst.reverse()
        return lst

    @staticmethod
    def drop_empty_items(d):
        return {k: v for k, v in d.items() if v is not None}

    @staticmethod
    def find_common_items(list1, list2):
        return sorted(set(list1).intersection(set(list2)))

    @staticmethod
    def reverse_words(sentence):
        return ' '.join(word[::-1] for word in sentence.split())


def main():
    # Пример использования
    print("Factorial of 5:", PythonTasks.calculate_factorial(5))
    print("Sum of digits of 123:", PythonTasks.sum_of_digits(123))
    print("Is 'abcba' palindrome?", PythonTasks.is_palindrome("abcba"))

    commands = ["insert 0 5", "insert 1 10", "insert 0 6", "print", "remove 6", "append 9", "append 1", "sort", "print", "pop", "reverse", "print"]
    print("List operations:")
    PythonTasks.process_list_commands(commands)

    d = {"c1": "Red", "c2": "Green", "c3": None}
    print("Dictionary after dropping empty items:", PythonTasks.drop_empty_items(d))

    list1 = [1, 2, 3, 4, 5]
    list2 = [4, 5, 6, 7, 8]
    print("Common items in lists:", PythonTasks.find_common_items(list1, list2))

    print("Reverse words:", PythonTasks.reverse_words("Hello World"))

if __name__ == "__main__":
    main()
