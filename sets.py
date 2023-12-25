def find_common_items(list1, list2):
    return sorted(set(list1).intersection(set(list2)))

def main():
    list1 = list(map(int, input().split()))
    list2 = list(map(int, input().split()))
    print(find_common_items(list1, list2))

if __name__ == "__main__":
    main()
