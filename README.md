# some_linux_scripts
A collection of some handy scripts i wrote for everyday use

# hex_to_rgb.py
`$ hex_to_rgb.py "#XXXXXX"`
Outputs RGB numbers in decimal for that color.
Will be added soon.

# replace.sh
Is just a shorthand for `sed -i "s/$1/$2/g" $3`.
Usage: `$ bash replace text_to_replace replace_with file`

# kitty-to-hypr-conf.py
A small script that converts a file formatted like this:
```
color1 #XXXXXX
color2 #XXXXXX
...
```
to:
```
$color1="#XXXXXX"
$color2="#XXXXXX"
```

