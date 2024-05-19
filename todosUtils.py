FILEPATH = "todos.txt"


def getTodos(filepath=FILEPATH):
    with open(filepath, 'r') as file_:
        return file_.readlines()


def writeTodos(data=None, filepath=FILEPATH):
    if data is None:
        data = []
    with open(filepath, 'w') as file_:
        file_.writelines(data)
