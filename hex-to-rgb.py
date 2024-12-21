#!/usr/bin/python

import argparse

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
    color = color.removeprefix('#')
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

if __name__ == '__main__':
    main()

