# https://judge.softuni.org/Contests/Practice/Index/1063#6

input_type = input()
first_input = input()
second_input = input()


def greater_value(tp, fst, snd):
    res= None
    if tp == 'int':
        if int(fst) >= int(snd):
            res = fst
        else:
            res = snd
    elif tp in ['char', 'string']:
        if fst >= snd:
            res = fst
        else:
            res = snd

    return res


result = greater_value(input_type, first_input, second_input)
print(result)
