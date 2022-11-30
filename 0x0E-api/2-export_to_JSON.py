#!/usr/bin/python3
"""documentation"""
import requests
from sys import argv
from json import dumps


if __name__ == '__main__':
    try:
        emp_id = int(argv[1])
    except ValueError:
        exit()

    url = 'https://jsonplaceholder.typicode.com'
    user_uri = '{api}/users/{id}'.format(api=url, id=emp_id)
    todo_uri = '{user_uri}/todos'.format(user_uri=user_uri)
    filename = '{emp_id}.json'.format(emp_id=emp_id)

    u_res = requests.get(user_uri).json()
    t_res = requests.get(todo_uri).json()
    user_tasks = list()

    for elem in t_res:
        data = {
            'task': elem.get('title'),
            'completed': elem.get('completed'),
            'username': u_res.get('username')
        }
        user_tasks.append(data)

    with open(filename, 'w', encoding='utf-8') as jsonfile:
        jsonfile.write(dumps({emp_id: user_tasks}))
