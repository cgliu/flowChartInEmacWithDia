#!/usr/bin/env python
"""
Post-process Tex files to fix export issue in Dia via LaTex PGF macro
"""

from glob import glob
from pathlib import Path

import argparse


def process_single_tex(filename, output):
    """ Process a single Tex file

    :param filename: The file name to be processed.
    :param output: The output file name.
    """

    result = []
    with open(filename) as fh:
        line = fh.read()
        while line != '':
            line = line.replace('\\$', '$')
            line = line.replace('\\ensuremath{\\backslash}', '\\')
            line = line.replace('\\_', '_')
            line = line.replace('\\{', '{')
            line = line.replace('\\}', '}')
            line = line.replace('\\^{}', '^')
            result.append(line)
            line = fh.read()

    with open(output, 'w') as fh:
        fh.writelines(result)
    print(f"Done! {filename} -> {output}")


def process_tex_files_in_folder(folder):
    files = glob(f"{folder}/*.tex")
    dest = Path(folder).joinpath("fixed")
    dest.mkdir(parents=True, exist_ok=True)
    for file in files:
        output = dest.joinpath(Path(file).name)
        process_single_tex(file, output)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Fix Latex export')
    parser.add_argument('folder', help='source folder')
    args = parser.parse_args()

    process_tex_files_in_folder(args.folder)
