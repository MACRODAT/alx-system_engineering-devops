#!/usr/bin/python3

"""
Script to fetch data from API
"""

import requests
from sys import argv

REST_API = "https://jsonplaceholder.typicode.com"


if __name__ == "__main__":
    employer = argv[1]
    j = requests.get(f'{REST_API}/users/{argv[1]}').json()
    tasks = requests.get(f'{REST_API}/todos').json()
    name = j.get('name')
    alltasks = list(filter(lambda x: x.get('userId' == argv[1]), tasks))
    completed_tasks = list(filter(lambda x: x.get('completed'), alltasks))
    print(
        'Employee {} is done with tasks({}/{}):'.format(
            name,
            len(completed_tasks),
            len(alltasks)
        )
    )
    if len(completed_tasks) > 0:
        for task in completed_tasks:
            print('\t {}'.format(task.get('title')))
