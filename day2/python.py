# part 1
import re
import enum
import typing as t

split_pattern = '; |, '

input_file = './day2/input.txt'


class MaxColor(enum.Enum):
    blue = 14
    red = 12
    green = 13


def get_line_index(elem: str) -> int:
    return int(elem.split(' ')[1])


def get_max_color_line(li: t.List, color: str) -> t.Dict:
    list_color = [elem['val'] for elem in li if elem['key'] == color]
    return max(list_color)


def get_dict_color_value(elem: str) -> t.Dict:
    splited = elem.split(' ')
    return {'key': splited[1], 'val': int(splited[0])}


def get_tuple_color_value(elem: str) -> t.Tuple:
    splited = elem.split(' ')
    return (splited[1], int(splited[0]))


def parse_line(line: str):
    splited = re.split(split_pattern, line)
    list_of_dict = [get_dict_color_value(elem) for elem in splited]
    dict_of_max = {elem.name: get_max_color_line(list_of_dict, elem.name) for elem in MaxColor}
    return dict_of_max


def part_1(f):
    s = 0

    for line in f:
        add_id = True
        line_split = line.replace('\n', '').split(': ')
        dict_of_max = parse_line(line_split[1])
        for k, v in dict_of_max.items():
            if v > MaxColor[k].value:
                add_id = False
                break
        if add_id:
            s += get_line_index(line_split[0])

    return s


def part_2(f):
    s = 0

    for line in f:
        line_split = line.replace('\n', '').split(': ')
        dict_of_max = parse_line(line_split[1])
        p = 1
        for _, v in dict_of_max.items():
            p *= v
        s += p

    return s


def main(file_name=input_file):

    with open(file_name) as f:
        s = part_2(f)

    print(s)


main()
