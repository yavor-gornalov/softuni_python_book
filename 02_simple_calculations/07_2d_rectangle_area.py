# https://judge.softuni.org/Contests/Practice/Index/1047#6

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

width = max(x1, x2) - min(x1, x2)
height = max(y1, y2) - min(y1, y2)

area = width * height
perimeter = 2 * (width + height)

print('Area = ', area)
print('Perimeter = ', perimeter)
