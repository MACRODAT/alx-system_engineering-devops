#!/usr/bin/python3
"""Exports to-do list information for emp
in json format"""

import json
import requests
import sys

url = "https://jsonplaceholder.typicode.com/"


if __name__ == "__main__":
    user_id = sys.argv[1]
    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    with open("{}.json".format(user_id), "w") as jsonfile:
        json.dump({user_id: [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": username
            } for t in todos]}, jsonfile)
