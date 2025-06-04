#!/usr/bin/python3

import json

def serialize_and_save_to_file(data, filename):
    if not isinstance(data, dict):
        raise TypeError(f"serialize_and_save_to_file not dict {type(data)}")

    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(data, f)

def load_and_deserialize(filename):
    with open(filename, 'r', encoding="utf-8") as fp:
        data = json.load(fp)
        
    if not isinstance(data, dict):
        raise ValueError(f"serialize_and_save_to_file Not a dict{type(data)}")
    return data
