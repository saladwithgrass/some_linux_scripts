#!/usr/bin/python

import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('color', help='Hex color code. May be with or without the # in the beginning.')
    parser.add_argument('-s', '--separator', help='Separator between components', default=', ')
    args = parser.parse_args()
    sep = args.separator
    color:str = args.color
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
        print(int(color[pos:pos+2], 16), end=f'{sep}')

if __name__ == '__main__':
    main()

