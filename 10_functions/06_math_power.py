# https://judge.softuni.org/Contests/Practice/Index/1063#5

num = float(input())
power = float(input())


def calculate_power(a, n):
    pwr = a ** n
    if pwr % 1 == 0:
        return int(a ** n)
    return pwr


power_result = calculate_power(num, power)
print(power_result)
