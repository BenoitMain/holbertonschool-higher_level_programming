#!/usr/bin/python3
"""
Add command-line arguments to a JSON list stored in a file.

This script loads a list from `add_item.json` (creating an empty list if it
does not exist), appends any arguments passed via the command line to that list,
and then saves the updated list back to `add_item.json` using JSON format.

Usage:
    ./7-add_item.py [item1] [item2] [...]

If `add_item.json` does not exist,  is created with an empty list before adding
any items. Subsequent runs will preserve existing items and append new ones.

Args:
    sys.argv[1:] (list of str): Items to add to the JSON list. Each element is
        appended in the order provided.


"""
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    my_list = load_from_json_file("add_item.json")
except FileNotFoundError:
    my_list = []
args_to_add = sys.argv[1:]
for item in args_to_add:
    my_list.append(item)

save_to_json_file(my_list, "add_item.json")
