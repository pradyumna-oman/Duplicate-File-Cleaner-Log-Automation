from src.scanner import scan_directory


def main():

    print("=" * 60)
    print("Duplicate File Cleaner & Log Automation")
    print("=" * 60)

    directory = input("Enter directory path: ")

    try:

        files, total_files, total_folders = scan_directory(directory)

        print("\nFiles Found")
        print("-" * 60)

        for file in files:
            print(file)

        print("\nSummary")
        print("-" * 30)
        print(f"Total Files    : {total_files}")
        print(f"Total Folders  : {total_folders}")

    except Exception as error:
        print(error)


if __name__ == "__main__":
    main()