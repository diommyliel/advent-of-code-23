# Part 2
# see problem with line 2, 6 appearing multiple times
input_file = './1/input.txt'

sub = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9
}

with open(input_file, 'r') as f:
    s = 0
    for i in f:

        li = len(i) + 1
        ri = -1

        for k in sub.keys():
            pos = i.find(k)
            posr = i.rfind(k)
            if pos == -1:
                continue
            if pos < li:
                left = sub[k]
                li = pos
            if posr > ri:
                r = sub[k]
                ri = posr

        ret = (left * 10) + r
        s += ret
        print(ret)

    print(s)


# proto
it = []

it.append('two1nine')
it.append('eightwothree')
it.append('abcone2threexyz')
it.append('xtwone3four')
it.append('4nineeightseven2')
it.append('zoneight234')
it.append('7pqrstsixteen')

s = 0
for i in it:
    left = 0
    r = 0

    li = len(i) + 1
    ri = -1

    for k in sub.keys():
        pos = i.find(k)
        if pos == -1:
            continue
        if pos < li:
            left = sub[k]
            li = pos
        if pos > ri:
            r = sub[k]
            ri = pos

    ret = (left * 10) + r
    s += ret

print(s)
