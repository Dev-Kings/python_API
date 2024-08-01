#!/usr/bin/python3
"""
This script exports to-do-list information for a given employee
ID to a JSON file.
"""

import json
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

def export_to_json(employee_id):
    """
    Exports the TODO list of the given employee to a JSON file.
    Args:
        employee_id (int): The ID of the employee.
    """
    user_data, todos_data = fetch_employee_data(employee_id)
    username = user_data.get("username")

    # Prepare the data in the specified format
    data = {
            str(employee_id): [
                {
                    "task": todo.get("title"),
                    "completed": todo.get("completed"),
                    "username": username
                }
                for todo in todos_data
            ]
    }

    # Create the filename
    filename = f"{employee_id}.json"

    # Write data to JSON file
    with open(filename, mode='w') as file:
        json.dump(data, file, indent=4)

    print(f"Data has been exported to {filename}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("The employee ID must be an integer.")
        sys.exit(1)

    export_to_json(employee_id)
