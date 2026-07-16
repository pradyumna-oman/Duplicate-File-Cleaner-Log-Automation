from src.scanner import scan_directory


def main():

    print("=" * 60)
    print("Duplicate File Cleaner & Log Automation")
    print("=" * 60)

    directory = input("Enter directory path: ")

    try:

        items, files, folders = scan_directory(directory)

        print("\nDirectory Contents")
        print("-" * 30)

        for item in items:
            print(item)

        print("\nSummary")
        print("-" * 30)
        print(f"Files      : {files}")
        print(f"Folders    : {folders}")
        print(f"Total Items: {len(items)}")

    except Exception as error:
        print(f"\nError: {error}")


if __name__ == "__main__":
    main()