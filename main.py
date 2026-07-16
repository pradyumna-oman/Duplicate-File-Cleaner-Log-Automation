from src.scanner import scan_directory
from src.duplicate_detector import find_duplicates
from src.report import generate_reports


def main():

    print("=" * 60)
    print("Duplicate File Cleaner & Log Automation")
    print("=" * 60)

    directory = input("Enter directory path: ")

    try:

        files, total_files, total_folders = scan_directory(directory)

        duplicates = find_duplicates(files)

        csv_report, json_report = generate_reports(duplicates)

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
        
        print(f"CSV  : {csv_report}")
        print(f"JSON : {json_report}")

    except Exception as error:
        print(error)


if __name__ == "__main__":
    main()