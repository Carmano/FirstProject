from itertools import *


def main():
    with open('text/input.txt', 'r', encoding='utf-8') as file:
        n = int(file.readline().rstrip('\n'))
        arr = []
        for i in range(n):
            arr.extend(file.readline().rstrip('\n').split(', '))
        arr.sort()
        for index, value in enumerate(arr):
            print(str(index + 1) + ". " + value)


if __name__ == '__main__':
    main()
