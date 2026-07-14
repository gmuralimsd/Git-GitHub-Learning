import os

def print_tree(path, indent=""):
    try:
        items = sorted(os.listdir(path))
        for item in items:
            full_path = os.path.join(path, item)
            print(indent + "|-- " + item)

            if os.path.isdir(full_path):
                print_tree(full_path, indent + "    ")
    except PermissionError:
        pass

print_tree("/")