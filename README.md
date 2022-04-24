# dotpreprocessor

## Motivation
When creating settings, we often have to redefine variables that should really be centralized and shared. For example, in a terminal emulator configuration file, we might be using fonts and colors that is also used in a browser configuration file, window manager configuration file, etc. If we ever decided to change that font, we'd have to change all instances of where those variables were used.

## Quickstart
```sh
chmod +x dotpp.py
./dotpp.py --source <python file with lookup dictionary> --target <file to be preprocessed>
```

## Usage
Suppose we have a file `colors.conf` with the following contents:
```
foreground_color #ffffff
background_color #000000
```
We want to replace `foreground_color` and `background_color` with variables, say `white` and `black`, respectively. To do this, create a new file `colors.conf.dot` with the following contents:
```
foreground_color $$white$$
background_color $$black$$
```
and a Python file `lookup.py`:
```py
lookup = {
  "white": "#ffffff",
  "black": #000000"
}
```
Now run `./dotppy.py --source lookup.py --target colors.conf.dot --output colors.conf`.

## Workflow
A simple script to build all `.dot` files I use in [my dotfiles](https://github.com/tonyd33/dotfiles)
```sh
function build() {
  directory=`dirname $1`
  filename=`basename $1`
  [ ${filename##*.} != dot ] && exit # ignore non .dot files
  built="$directory/${filename::-4}"
  dotpp -s lookup.py -t $1 -o $built
  echo "built $1->$built"
}

export -f build # we have to export this for the find subshell to pick it up

find . type f -exec bash -c 'build "{}"' \;
```
