import inspect
import helpers

def list_functions():
    functions_list = inspect.getmembers(helpers, inspect.isfunction)
    for name, _ in functions_list:
        print(name)