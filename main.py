#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
from benedict import benedict
import deepdiff
import pprint

pp = pprint.PrettyPrinter(indent=4)

file1 = file2 = None 


def main():
    """
    This function takes in two yaml files and prints out the differences between them using the benedict and deepdiff libraries.

    Args:
        file1 (str): The path to the first yaml file.
        file2 (str): The path to the second yaml file.

    Returns:
        None
    """

    parser = argparse.ArgumentParser()
    parser.add_argument("-file1", help="path to first yaml file", default=None)
    parser.add_argument("-file2", help="path to second yaml file", default=None)
    parser.add_argument("-o", "--outfile", default=None, help="path to output file")

    args = parser.parse_args()

    if args.file1 and args.file2:
        dict_1 = benedict.from_yaml(args.file1, keypath_separator=None)
        dict_2 = benedict.from_yaml(args.file2, keypath_separator=None)
    elif file1 and not args.file1:
        dict_1 = benedict.from_yaml(file1, keypath_separator=None)
        dict_2 = benedict.from_yaml(file2, keypath_separator=None) 
    else:
        print("Error, no files specified")
        return 0

    # find out name of first key in both dictionaries
    key1 = list(dict_1.keys())[0]
    key2 = list(dict_2.keys())[0]

    # Skip one step, becouse key1 amd key2 differ, but i should not
    next1 = dict_1[key1]
    next2 = dict_2[key2]


    diff = deepdiff.DeepDiff(next1, next2, ignore_order=True)
    pp.pprint(diff)

    # save as file
    if args.outfile is not None:
        with open(args.outfile, "w") as f:
            f.write(pp.pformat(diff))


if __name__ == '__main__':
    main()