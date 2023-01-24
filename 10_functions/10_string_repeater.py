# https://judge.softuni.org/Contests/Practice/Index/1063#9


user_string = input()
repeat_times = int(input())


def repeat_string(string, count):
    res = ''
    for _ in range(count):
        res += string
    return res


result_to_print = repeat_string(user_string, repeat_times)
print(result_to_print)
