import os


def remove_extension_name(filename):
    base_name, extension = os.path.splitext(filename)

    return base_name


def add_file_extension(filename, new_extension):
    base_name, _ = os.path.splitext(filename)
    new_file_name = f'{base_name}.{new_extension}'

    return new_file_name
