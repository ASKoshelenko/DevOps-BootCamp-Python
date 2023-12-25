def reverse_words(sentence):
    return ' '.join(word[::-1] for word in sentence.split())

def main():
    sentence = input()
    print(reverse_words(sentence))

if __name__ == "__main__":
    main()
