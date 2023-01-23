# https://judge.softuni.org/Contests/Practice/Index/1063#3

num = int(input())


def print_square_side(n):
    for i in range(2 * n):
        print('-', end='')
    print()


def print_square_middle(n):
    for i in range(n - 2):
        middle = ""
        for j in range(2 * n - 2):
            if j % 2 == 0:
                middle += "\\"
            else:
                middle += "/"
        print(f"-{middle}-")


def print_square(n):
    print_square_side(n)
    print_square_middle(n)
    print_square_side(n)


print_square(num)
