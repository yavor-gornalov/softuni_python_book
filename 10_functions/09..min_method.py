# https://judge.softuni.org/Contests/Practice/Index/1063#8

a = int(input())
b = int(input())
c = int(input())


def get_min(fst, snd):
    return min(fst, snd)


minimum = get_min(get_min(a, b), c)
print(minimum)
