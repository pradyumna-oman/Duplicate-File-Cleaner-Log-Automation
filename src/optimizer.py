import os


def group_files_by_size(files):
    """
    Group files by their size in bytes.
    Returns a dictionary:
    {
        size: [file1, file2]
    }
    """

    size_map = {}

    for file in files:

        try:

            file_size = os.path.getsize(file)

            if file_size not in size_map:
                size_map[file_size] = []

            size_map[file_size].append(file)

        except Exception as error:
            print(f"Error reading {file}: {error}")

    return size_map

def get_duplicate_size_groups(size_map):
    """
    Return only groups having
    more than one file.
    """

    duplicate_size_groups = {}

    for size, file_list in size_map.items():

        if len(file_list) > 1:

            duplicate_size_groups[size] = file_list

    return duplicate_size_groups