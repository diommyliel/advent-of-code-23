# Part 1
input_file = '/home/diommy/Documents/dev/advent-of-code-23/1/input.txt'

with open(input_file, 'r') as f:
    s = 0
    for i in f:
        li = 0
        ri = -1

        while li <= len(i):
            try:
                l = int(i[li])
                break
            except:
                li += 1

        while ri >= - len(i):
            try:
                r = int(i[ri])
                break
            except:
                ri -= 1

        s += (l * 10) + r

    print(s)

# proto

j = '1abc2'
k = 'pqr3stu8vwx'
n = 'a1b2c3d4e5f'
m = 'treb7uchet'

it = [j, k, n, m]

s = 0
for i in it:
    li = 0
    ri = -1

    while li <= len(i):
        try:
            l = int(i[li])
            break
        except:
            li += 1

    while ri >= - len(i):
        try:
            r = int(i[ri])
            break
        except:
            ri -= 1

    s += (l * 10) + r

# print(s)
