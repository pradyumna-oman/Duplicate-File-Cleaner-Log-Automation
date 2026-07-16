from src.hasher import generate_sha256


def find_duplicates(size_groups):
    """
    Detect duplicate files using SHA256.
    """

    duplicate_map = {}

    for file_list in size_groups.values():

        for file in file_list:

            file_hash = generate_sha256(file)

            if file_hash not in duplicate_map:
                duplicate_map[file_hash] = []

            duplicate_map[file_hash].append(file)

    return duplicate_map