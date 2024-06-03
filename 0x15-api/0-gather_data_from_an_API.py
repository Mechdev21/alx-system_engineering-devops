#!/usr/bin/python3
"""
place holder
"""

import json
import requests
import sys

def get_employee(argument):
    base_url = f"https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{argument}"
    todo_url = f"{base_url}/users/{argument}/todos"

    try:
        user_response = requests.get(user_url)
        user_response.raise_for_status()
    except requests.exceptions.HTTPError:
        print(f"User with ID {argument} not found.")
        return
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return

    user_data = user_response.json()
    employee_name = user_data.get('name')

    try:
        todo_response = requests.get(todo_url)
        todo_response.raise_for_status()
    except requests.exceptions.HTTPError:
        print("Could not retrieve todos.")
        return
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return

    todo_data = todo_response.json()
    done_tasks = [todo for todo in todo_data if todo.get('completed')]
    total_tasks = len(todo_data)
    num_done_tasks = len(done_tasks)

    print(f"Employee {employee_name} is done with tasks({num_done_tasks}/{total_tasks}):")

    for task in done_tasks:
        print(f"\t {task.get('title')}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: script.py <employee_id>")
        sys.exit(1)
    
    try:
        argument = int(sys.argv[1])
    except ValueError:
        print("Please provide a valid employee ID.")
        sys.exit(1)

    get_employee(argument)
