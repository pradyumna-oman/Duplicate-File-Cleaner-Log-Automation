import hashlib


def generate_md5(file_path):
    """
    Generate MD5 checksum for a file.
    """

    md5 = hashlib.md5()

    with open(file_path, "rb") as file:

        while True:
            data = file.read(4096)

            if not data:
                break

            md5.update(data)

    return md5.hexdigest()


def generate_sha256(file_path):
    """
    Generate SHA256 checksum for a file.
    """

    sha = hashlib.sha256()

    with open(file_path, "rb") as file:

        while True:
            data = file.read(4096)

            if not data:
                break

            sha.update(data)

    return sha.hexdigest()