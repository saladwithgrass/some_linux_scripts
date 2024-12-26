#!/usr/bin/python

import argparse

def parse_hex(color:str, use_percent, sep, max_value):
    match len(color):
        case 6:
            print('default rgb detected.')
        case 8:
            print('rgba detected.')
        case _:
            print('wrong length of color.')
            exit(1)
    for pos in range(0, len(color), 2):
        if pos == len(color) - 2:
            sep = '\n'
        color_value = int(color[pos:pos+2], 16)
        if use_percent:
            color_value = int(color_value / max_value * 100)
        print(color_value, end=f'{sep}')


def parse_rgb(rgb:str):
    with_alpha = 'rgba(' in rgb
    rgb = rgb.replace('rgb', '').replace('rgba', '').replace('(', '').replace(')', '').replace(' ', '')
    val_list = rgb.split(',')
    if with_alpha and len(val_list) != 4:
        print(f'WARNING: rgba must have 4 components, but {len(val_list)} found.')
    elif not with_alpha and len(val_list) != 3:
        print(f'WARNING: rgb must have 3 components, but {len(val_list)} found')
    print('#', end='')
    for val in val_list:
        hex_val = hex(int(val)).removeprefix('0x')
        if len(hex_val) == 1:
            hex_val = '0' + hex_val
        print(hex_val, end='')
    print()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('color', help='Hex color code. May be with or without the # in the beginning.')
    parser.add_argument('-s', '--separator', help='Separator between components', default=', ')
    parser.add_argument('-p', '--percent', help='Will print precentages instead of 8-bit values', action='store_true')
    args = parser.parse_args()
    sep = args.separator
    use_percent = args.percent
    color:str = args.color
    max_value = 2**8
    
    if color.startswith('rgb'):
        parse_rgb(color)
    else:
        color = color.removeprefix('#')
        parse_hex(
            color, 
            use_percent=use_percent,
            sep=sep,
            max_value=max_value
            )

if __name__ == '__main__':
    main()

