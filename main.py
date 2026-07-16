from src.scanner import scan_directory
from src.duplicate_detector import find_duplicates
from src.report import generate_csv_report


def main():

    print("=" * 60)
    print("Duplicate File Cleaner & Log Automation")
    print("=" * 60)

    directory = input("Enter directory path: ")

    try:

        files, total_files, total_folders = scan_directory(directory)

        duplicates = find_duplicates(files)

        report = generate_csv_report(duplicates)

        print("\nDuplicate Report")
        print("-" * 60)

        duplicate_found = False

        for file_hash, file_list in duplicates.items():

            if len(file_list) > 1:

                duplicate_found = True

                print(f"\nSHA256 : {file_hash}")

                for file in file_list:
                    print(f"   {file}")

        if not duplicate_found:
            print("No duplicate files found.")

        print("\nSummary")
        print("-" * 30)
        print(f"Files   : {total_files}")
        print(f"Folders : {total_folders}")

        print("\nReport Generated Successfully")
        print(report)

    except Exception as error:
        print(error)


if __name__ == "__main__":
    main()