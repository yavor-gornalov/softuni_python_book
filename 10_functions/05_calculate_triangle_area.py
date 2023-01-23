# https://judge.softuni.org/Contests/Practice/Index/1063#4

side, height = float(input()), float(input())


def triangle_area(a, ha):
    area = (a * ha) / 2
    if area % 1 == 0:
        return int(area)  # sometimes judge don't like decimal points
    return area


print(triangle_area(side, height))
