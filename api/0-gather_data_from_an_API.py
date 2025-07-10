#!/usr/bin/python3
"""
This module uses the REST API (https://jsonplaceholder.typicode.com/)
to get data for a given employee ID and returns information about
his/her TODO list progress.
"""

import requests
import sys

if __name__ == "__main__":
    empl_ID = sys.argv[1]

    # TODO and User endpoints
    todo_url = f"https://jsonplaceholder.typicode.com/todos?userId={empl_ID}"
    user_url = f"https://jsonplaceholder.typicode.com/users/{empl_ID}"

    # Fetch employee data
    user_response = requests.get(user_url)
    userjson = user_response.json()
    empl_name = userjson.get("name")

    # Fetch employee TODO list
    todo_response = requests.get(todo_url)
    tdjson = todo_response.json()

    # Count completed and total tasks
    completed_tasks = [i for i in tdjson if i.get("completed")]
    total_tasks = len(tdjson)

    print("Employee {} is done with tasks({}/{}):".format(
        empl_name, len(completed_tasks), total_tasks))

    for i in completed_tasks:
        print("\t {}".format(i.get('title')))
