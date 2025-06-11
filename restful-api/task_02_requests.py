#!/usr/bin/python3

import requests
import csv


def fetch_and_print_posts():
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    print(f"Status Code: {r.status_code}")
    if r.status_code == 200:
        for post in r.json():
            print(post["title"])

def fetch_and_save_posts():
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    if r.status_code == 200:
        post = r.json()
        with open("posts.csv", "w", newline='', encoding="utf-8") as f:
            data = csv.DictWriter(f, ["id", "title", "body"])
            data.writeheader()
            for dict in post:
                data.writerow({
                    "id": dict["id"],
                    "title": dict["title"],
                    "body": dict["body"]
                })

