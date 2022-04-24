#!/usr/bin/python
import argparse
import json
import sys


def main():
    parser = argparse.ArgumentParser(prog="dotpreprocessor")
    parser.add_argument(
        "-s", "--source", type=str, action="store", required=True
    )
    parser.add_argument(
        "-t", "--target", type=str, action="store", required=True
    )
    parser.add_argument(
        "-o", "--output", type=str, action="store", default=None
    )

    args = parser.parse_args()

    lookup = get_lookup(args.source)
    new_content = preprocess(args.target, lookup)

    if args.output is None:
        sys.stdout.write(new_content)
    else:
        write(args.output, new_content)


def get_lookup(file_path):
    file = open(file_path, "r")
    lookup = json.loads(file.read())
    file.close()
    return lookup


def preprocess(file_path, lookup):
    file = open(file_path, "r")
    content = file.read()
    new_content = content
    for varname, value in lookup.items():
        new_content = new_content.replace(f"$${varname}$$", value)
    file.close()
    return new_content


def write(file_path, content):
    file = open(file_path, "w")
    file.write(content)
    file.close()


if __name__ == "__main__":
    main()
