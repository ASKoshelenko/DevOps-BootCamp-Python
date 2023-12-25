def drop_empty_items(d):
    return {k: v for k, v in d.items() if v is not None}

def main():
    import json
    data = json.loads(input())
    print(drop_empty_items(data))

if __name__ == "__main__":
    main()
