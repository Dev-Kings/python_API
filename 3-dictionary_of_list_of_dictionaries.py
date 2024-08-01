#!/usr/bin/python3
"""
This script exports to-do-list information for all employees to a JSON file.
"""

import json
import requests

def fetch_all_users():
    """
    Fetches all users from JSONPlaceholder API.
    Returns:
        tuple: A list of user data.
    """
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    return response.json()

def fetch_todos_for_user(user_id):
    """
    Fetches TODO list for a specific user from the JSONPlaceholder API.
    Args:
        user_id (int): The ID of the user.
    Returns:
        list: A list of TODO data for the user.
    """
    url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"
    response = requests.get(url)
    return response.json()

def export_to_json():
    """
    Exports the TODO list for all employees to a JSON file.
    """
    users = fetch_all_users()
    all_data = {}

    for user in users:
        user_id = user.get("id")
        username = user.get("username")
        todos = fetch_todos_for_user(user_id)

        all_data[str(user_id)] = [
                {
                    "username": username,
                    "task": todo.get("title"),
                    "completed": todo.get("completed")
                }
                for todo in todos
        ]

    # Write data to JSON file
    with open("todo_all_employees.json", mode='w') as file:
        json.dump(all_data, file, indent=4)

    print(f"Data has been exported to todo_all_employees.json")

if __name__ == "__main__":
    export_to_json()
