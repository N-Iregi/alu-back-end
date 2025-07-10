#!/usr/bin/python3
"""
This module uses this REST API(https://jsonplaceholder.typicode.com/)to get
data for a given employee ID, records all
tasks that are owned by this employee in json format
to a file called USER_ID.json
"""

import json
import requests
import sys

if __name__ == "__main__":
    empl_ID = sys.argv[1]

    # TODO and User endpoints for getting data
    todo_url = f"https://jsonplaceholder.typicode.com/todos?userId={empl_ID}"
    user_url = f"https://jsonplaceholder.typicode.com/users/{empl_ID}"

    # Fetch data for employee name
    user_response = requests.get(user_url)
    userjson = user_response.json()
    empl_name = userjson.get("username")

    # Fetch employee TODO list
    todo_response = requests.get(todo_url)
    tdjson = todo_response.json()

    # save data from json file
    task_list = []

    for i in tdjson:
        task_list.append({
                    "task": i.get("title"),
                    "completed": i.get("completed"),
                    "username": empl_name
                    })

    # Final data structure
    tasks = {empl_ID: task_list}

    # Open CSV file for writing
    filename = f"{empl_ID}.json"

    with open(filename, "w") as jsonfile:
        json.dump(tasks, jsonfile)
        jsonfile.write("\n")
