import re
from functools import reduce

input_file = './day3/input.txt'

char_pattern = r'[^ \d.\n]'
num_pattern = r'\d+'
gear_pattern = r'[*]'


def get_symbol_adjacent_indices(symbol_index, len_line):
    ret_set = set()
    calc_list = [symbol_index, symbol_index - len_line, symbol_index + len_line]
    index_modulo = symbol_index % len_line
    ret_set.update(calc_list)
    if index_modulo != 0:
        ret_set.update([x - 1 for x in calc_list])
    if index_modulo != len_line - 2:
        ret_set.update([x + 1 for x in calc_list])

    return ret_set


def part_1(f):
    len_line = f.find('\n') + 1
    symbol_adjacent_indices = set()
    symbols = re.finditer(char_pattern, f)
    for symbol in symbols:
        list_adjacent = get_symbol_adjacent_indices(symbol.start(), len_line)
        symbol_adjacent_indices.update(list_adjacent)
    nums = re.finditer(num_pattern, f)
    parts_num = []
    for num in nums:
        for i in range(num.start(), num.end()):
            if i in symbol_adjacent_indices:
                parts_num.append(int(num.group()))
                break
    res = reduce(lambda x, y: x + y, parts_num)
    return res


def part_2(f):
    len_line = f.find('\n') + 1
    nums_iter = re.finditer(num_pattern, f)
    dict_num = {}
    id_num = 0
    for num in nums_iter:
        n = num.group()
        for i in range(num.start(), num.end()):
            dict_num[i] = {'id': id_num, 'val': int(n)}
        id_num += 1
    gears = re.finditer(gear_pattern, f)
    gear_ratio_list = []
    for gear in gears:
        gear_adjacent_num_val_list = []
        gear_adjacent_num_id_set = set()
        indices = get_symbol_adjacent_indices(gear.start(), len_line)
        for index in indices:
            if re.match(r'\d', f[index]) and dict_num[index]['id'] not in gear_adjacent_num_id_set:
                gear_adjacent_num_id_set.add(dict_num[index]['id'])
                gear_adjacent_num_val_list.append(dict_num[index]['val'])
        if len(gear_adjacent_num_val_list) == 2:
            gear_ratio = reduce(lambda x, y: x * y, gear_adjacent_num_val_list)
            gear_ratio_list.append(gear_ratio)
    gear_ratio_sum = reduce(lambda x, y: x + y, gear_ratio_list)
    return gear_ratio_sum


def main_part_1(input=input_file):
    with open(input, 'r') as file:
        f = file.read()
        ret = part_1(f)
    print(ret)


def main_part_2(input=input_file):
    with open(input, 'r') as file:
        f = file.read()
        ret = part_2(f)
    print(ret)


main_part_1()
main_part_2()
