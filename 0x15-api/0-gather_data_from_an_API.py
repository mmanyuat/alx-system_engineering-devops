#!/usr/bin/python3
"""importing module to request and take arguments"""

import requests
from sys import argv


def get_employee_to_info(employee_Id):
    """Takes an employee id and renders the todo progress"""
    try:
        url = "https://jsonplaceholder.typicode.com/"
        user_data = requests.get(url + f"users/{employee_Id}")
        user = user_data.json()
        employee_name = user['name']

        todo_list = requests.get(url + f"todo?userId={employee_Id}")
        todos = todo_list.json()
        total_task = len(todos)
        task_done = [task for task in todos if task['completed']]
        no_task_done = len(task_done)

        print(f"Employee {employee_name} is done with tasks ("
              f"{no_task_done}/{total_task}):")
        for task in task_done:
            print(f"/t {task[title]}")

    except exception as e:
        print(f"an error occured: {e}")


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: script <employee_Id>")
    else:
        get_employee_to_info(argv[1])
