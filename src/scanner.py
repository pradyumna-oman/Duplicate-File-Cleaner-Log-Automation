import os


def scan_directory(directory_path):
    """
    Scan a directory (non-recursive).

    Parameters:
        directory_path (str): Path of the directory.

    Returns:
        tuple:
            items
            file_count
            folder_count
    """

    # Check whether directory exists
    if not os.path.exists(directory_path):
        raise FileNotFoundError(f"Directory not found: {directory_path}")

    # Check whether it is a directory
    if not os.path.isdir(directory_path):
        raise NotADirectoryError(f"{directory_path} is not a directory")

    # Get all files and folders
    items = os.listdir(directory_path)

    file_count = 0
    folder_count = 0

    # Count files and folders
    for item in items:

        full_path = os.path.join(directory_path, item)

        if os.path.isfile(full_path):
            file_count += 1

        elif os.path.isdir(full_path):
            folder_count += 1

    return items, file_count, folder_count