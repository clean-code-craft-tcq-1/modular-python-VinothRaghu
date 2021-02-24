from color_tables import *


def color_pair_to_string(major_color, minor_color):

    major_color_length = len(major_color)
    tab_decor = ''
    tab_decor_len = 12 - major_color_length
    for i in range(tab_decor_len):
        tab_decor = tab_decor + ' '
    return f'{major_color}{tab_decor}| {minor_color}'


def print_manual():
    print('-----------------------------------')
    print('Pair No | Major Color | Minor Color')
    print('-----------------------------------')
    pair_num = 0
    for major_color in MAJOR_COLORS:
        for minor_color in MINOR_COLORS:
            pair_num = pair_num + 1
            color_pair = color_pair_to_string(major_color,minor_color)
            if pair_num >=10:
                print(f'{pair_num}      | {color_pair}')
            else:
                print(f'{pair_num}       | {color_pair}')
    print('-----------------------------------')