num = 5
star = '*'
space = ' '
p = 0

for x in range(1, num + 1):
    p = num + 1 - x
    print(space * p + star * x*2)
    if x == num:
        for n in range(num + 1, 0, -1):
            p = num + 1 - n
            print(space * p + star * n*2)
