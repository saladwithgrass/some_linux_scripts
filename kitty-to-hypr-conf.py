from os import path
import shutil
import sys
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('kitty_config', help='File with kittytheme config.')
    parser.add_argument('-o', '--output', help='Output file with hypr config.', default='hyprcolors.conf')
    args = parser.parse_args()
    kitty_config = args.kitty_config
    output = args.output

    if path.exists(output):
        print(f'WARNING: output file already exists. Saving to {output}.new')
        output = output + '.new'

    if not path.exists(kitty_config):
        print(f'ERROR: file {kitty_config} does not exist. Aborting.')
        exit(1)

    with open(kitty_config, 'r') as kitty:
        kitty_lines = kitty.readlines()
        with open(output, 'w') as hypr:
            for line in kitty_lines:
                # remove unneded newline
                line = line.removesuffix('\n')
                # skip comments
                if line.startswith('#') or len(line) == 0:
                    hypr.write(line + '\n')
                    continue
                line = line.expandtabs()
                split_line = line.split()
                hypr.write(f'${split_line[0]}=\"{split_line[1]}\"\n')

if __name__ == '__main__':
    main()