
def main():
    t = input()
    num = input()
    correct = 0;

    for n in num:
        if n == t:
            correct += 1

    print(correct)


if __name__ == '__main__':
    main()