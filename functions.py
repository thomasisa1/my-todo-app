FILEPATH = "todos.txt"

def get_todos(filepath = FILEPATH):
    """ Read a text file and return a list of
    to-do items. """
    try:
        with open(filepath, 'r') as file:
            todos = [line.strip() for line in file.readlines()]
        return todos
    except FileNotFoundError:
        # If file doesn't exist, create an empty file and return an empty list
        with open(filepath, 'w', encoding="utf-8") as file:
            pass
        return []

def write_todos( todos, filepath = FILEPATH):
    """ Write the to-do items list in the text file """
    with open(filepath, 'w', encoding="utf-8") as file:
        file.writelines([todo.strip() + '\n' for todo in todos])


print(__name__)
if __name__ == "__main__":
    print("Hello")
    print(get_todos())