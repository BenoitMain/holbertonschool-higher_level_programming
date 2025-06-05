#!/usr/bin/python3
"""
Module task_02_csv

Converts a CSV file to a JSON file by serializing the content.
The output is saved to 'data.json'.

Example:
    Input CSV:
        name,age,city
        John,28,New York

    Output JSON:
        [
            {"name": "John", "age": "28", "city": "New York"}
        ]
"""


import csv
import json


def convert_csv_to_json(filename):
    """
    Convert the contents of a CSV file to a JSON file.

    Reads the CSV using DictReader to preserve column headers as keys.
    Outputs the JSON data to 'data.json'.

    Args:
        csv_file (str): The path to the CSV file.

    Returns:
        bool: True if conversion was successful,
        False if there was an error (e.g. file not found or invalid CSV).
    """
    try:

        with open(filename, 'r') as f:
            csv_dict = []
            data = csv.DictReader(f)
            with open('data.json', 'w') as json_file:
                json.dump(list(data), json_file, indent=4)
        return True
    except Exception:
        return False
