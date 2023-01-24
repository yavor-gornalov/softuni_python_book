# https://judge.softuni.org/Contests/Practice/Index/1063#10

num = input()
ind = int(input())


def find_nth_digit(number, index):
    res = num[-index]
    return res


result = find_nth_digit(num, ind)
print(result)
