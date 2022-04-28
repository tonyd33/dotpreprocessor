#!/usr/bin/python
import argparse
import json
import sys
import os


def main():
    parser = argparse.ArgumentParser(prog="dotpp")
    parser.add_argument(
        "-s",
        "--source",
        type=str,
        action="store",
        required=True,
        help="the .py or .json file to source variables from",
    )
    parser.add_argument(
        "-t",
        "--target",
        type=str,
        action="store",
        help="the target replace variables on",
    )
    parser.add_argument(
        "-j",
        "--json",
        action="store_true",
        help="if provided, will generate the source to a portable JSON file",
    )
    parser.add_argument(
        "-o", "--output", type=str, action="store", default=None
    )

    args = parser.parse_args()

    lookup = get_lookup(args.source)
    out = None
    if args.json:
        out = json.dumps(lookup, indent=2)
    else:
        out = preprocess(args.target, lookup)

    if args.output is None:
        sys.stdout.write(out)
    else:
        write(args.output, out)


def get_lookup(file_path):
    file_name, file_extension = os.path.splitext(file_path)
    if file_extension == "json":
        return json.load(file_path)
    module = __import__(file_name)
    return module.lookup


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
