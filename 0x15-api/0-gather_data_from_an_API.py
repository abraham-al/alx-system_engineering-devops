#!/usr/bin/python3
"""
using this REST API
"""
import requests
import sys


if __name__ == '__main__':

    ids = sys.argv[1]
    task = []
    complete = 0
    total_task = 0
    url = "https://jsonplaceholder.typicode.com/users/" + ids
    res = requests.get(url).json()
    name = res.get('name')
    url = "https://jsonplaceholder.typicode.com/todos/"
    res_task = requests.get(url).json()
    for i in res_task:
        if i.get('userId') == int(ids):
            if i.get('completed') is True:
                task.append(i['title'])
                complete += 1
            total_task += 1
    print("Employee {} is done with tasks({}/{}):"
          .format(name, complete, total_task))
    for x in task:
        print("\t {}".format(x))
