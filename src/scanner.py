import os


def scan_directory(directory_path):
    """
    Scan a directory recursively.

    Parameters:
        directory_path (str): Path of the directory.

    Returns:
        tuple:
            all_files
            total_files
            total_folders
    """

    if not os.path.exists(directory_path):
        raise FileNotFoundError(f"Directory not found: {directory_path}")

    if not os.path.isdir(directory_path):
        raise NotADirectoryError(f"{directory_path} is not a directory")

    all_files = []
    folder_count = 0

    for root, directories, files in os.walk(directory_path):

        folder_count += len(directories)

        for file in files:
            full_path = os.path.join(root, file)
            all_files.append(full_path)

    return all_files, len(all_files), folder_count