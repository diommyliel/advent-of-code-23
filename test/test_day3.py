import day3.python as _3

input_test = '''467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
'''


def test_part_1():
    res = _3.part_1(input_test)
    assert res == 4361


def test_part_2():
    res = _3.part_2(input_test)
    assert res == 467835
