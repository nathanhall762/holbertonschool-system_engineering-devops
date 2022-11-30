#!/usr/bin/python3
"""documentation"""
import requests
from sys import argv

if __name__ == '__main__':
    try:
        emp_id = int(argv[1])
    except ValueError:
        exit()

    url = 'https://jsonplaceholder.typicode.com'
    user_uri = '{api}/users/{id}'.format(api=url, id=emp_id)
    todo_uri = '{user_uri}/todos'.format(user_uri=user_uri)

    res = requests.get(user_uri).json()
    name = res.get('name')
    res = requests.get(todo_uri).json()
    total = len(res)
    incomplete = sum([elem['completed'] is False for elem in res])
    completed = total - incomplete
    str = "Employee {emp_name} is done with tasks({completed}/{total}):"
    print(str.format(emp_name=name, completed=completed, total=total))

    for elem in res:
        if elem.get('completed') is True:
            print('\t', elem.get('title'))
