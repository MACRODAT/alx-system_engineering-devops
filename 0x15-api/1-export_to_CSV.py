#!/usr/bin/python3
"""Exports to-do list infos
for a given employee
to CSV format."""

import csv
import requests
import sys

path_url = "https://jsonplaceholder.typicode.com/"


if __name__ == "__main__":
    usr_id = sys.argv[1]
    user = requests.get(path_url + "users/{}".format(usr_id)).json()
    username = user.get("username")
    todos = requests.get(path_url + "todos", params={"userId": usr_id}).json()

    with open("{}.csv".format(usr_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [usr_id, username, t.get("completed"), t.get("title")]
         ) for t in todos]
