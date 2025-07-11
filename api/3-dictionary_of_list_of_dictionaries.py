#!/usr/bin/python3
"""
This module uses this REST API(https://jsonplaceholder.typicode.com/)to records all
tasks from all employees in json format
to a file called todo_all_employees.json
"""

import json
import requests
import sys

if __name__ == "__main__":

    # TODO and User endpoints for getting data
    todo_url = "https://jsonplaceholder.typicode.com/todos"
    user_url = f"https://jsonplaceholder.typicode.com/users"
    all_tasks = {}

    # Fetch data for employees' details
    user_response = requests.get(user_url)
    userjson = user_response.json()

    # Loop through each user and collect tasks
    for user in userjson:
        empl_name = user.get("username")
        empl_id = user.get("id")

        # Fetch todos for this user
        todos = requests.get(todo_url, params={"userId": empl_id}).json()

        # List to hold all task dicts for this user
        task_list = []

        for i in todos:
            task_dict = {
                "username": empl_name,
                "task": i.get("title"),
                "completed": i.get("completed")
                }
            task_list.append(task_dict)

            # Add to main dictionary
            all_tasks[empl_id] = task_list

    # Open CSV file for writing
    filename = "todo_all_employees.json"

    with open(filename, "w") as jsonfile:
        json.dump(all_tasks, jsonfile)
