from src.scanner import scan_directory
from src.hasher import generate_md5, generate_sha256


def main():

    print("=" * 60)
    print("Duplicate File Cleaner & Log Automation")
    print("=" * 60)

    directory = input("Enter directory path: ")

    try:

        files, total_files, total_folders = scan_directory(directory)

        print("\nFile Checksums")
        print("-" * 60)

        for file in files:
            md5 = generate_md5(file)
            sha = generate_sha256(file)

            print(f"\nFile : {file}")
            print(f"MD5    : {md5}")
            print(f"SHA256 : {sha}")

        print("\nScan Completed Successfully")
        print("\nSummary")
        print("-" * 30)
        print(f"Total Files    : {total_files}")
        print(f"Total Folders  : {total_folders}")

    except Exception as error:
        print(error)


if __name__ == "__main__":
    main()