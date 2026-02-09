#!/usr/bin/python3
"""
task_02_requests.py
Fetch and process posts from JSONPlaceholder using requests.
"""

import csv
import requests

BASE_URL = "https://jsonplaceholder.typicode.com/posts"


def fetch_and_print_posts():
    """
    Fetch all posts and print the response status code and all titles.
    """
    try:
        response = requests.get(BASE_URL, timeout=10)
    except requests.RequestException as e:
        # Network / timeout / DNS errors, etc.
        print(f"Request failed: {e}")
        return

    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()  # list of dicts
        for post in posts:
            print(post.get("title", ""))


def fetch_and_save_posts():
    """
    Fetch all posts and save them to posts.csv with columns: id, title, body
    """
    try:
        response = requests.get(BASE_URL, timeout=10)
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return

    if response.status_code == 200:
        posts = response.json()

        # Build list of dictionaries with required keys
        data = [
            {
                "id": post.get("id"),
                "title": post.get("title", ""),
                "body": post.get("body", "")
            }
            for post in posts
        ]

        # Write to CSV
        fieldnames = ["id", "title", "body"]
        with open("posts.csv", mode="w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
