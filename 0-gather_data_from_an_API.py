#!/usr/bin/python3
"""
This script fetches TODO list progress for an employee from the
JSPNPlaceholder API.
It displays the number of completed and total tasks along with titles
of completed tasks.
"""

import requests
import sys

def fetch_employee_data(employee_id):
    """
    Fetches employee_data and TODO list from JSONPlaceholder API.
    Args:
        employee_id (int): The ID of the employee.
    Returns:
        tuple: A tuple containing user data and TODO list data.
    """
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_response = requests.get(user_url)
    user_data = user_response.json()

    todos_url = todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    return user_data, todos_data


def display_todo_progress(employee_id):
    """
    Displays the progress of the TODO list for a given employee ID.
    Args:
        employee_id (int): The ID of the employee.
    """
    user_data, todos_data = fetch_employee_data(employee_id)

    employee_name = user_data.get('name')
    total_tasks = len(todos_data)
    done_tasks = [task for task in todos_data if task.get('completed')]
    done_tasks_count = len(done_tasks)

    print(f"Employee {employee_name} is done with tasks({done_tasks_count}/{total_tasks}):")

    for task in done_tasks:
        print(f"\t {task.get('title')}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("The employee ID must be an integer.")
        sys.exit(1)

    display_todo_progress(employee_id)
