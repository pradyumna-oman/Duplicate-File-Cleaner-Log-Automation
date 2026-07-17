from src.scanner import scan_directory
from src.duplicate_detector import find_duplicates
from src.report import generate_reports
from src.optimizer import (
    group_files_by_size,
    get_duplicate_size_groups
)
import logging
from src.logger import setup_logger
from src.mover import move_duplicates


def main():
    log_file = setup_logger()

    logging.info("Application Started")

    print("=" * 60)
    print("Duplicate File Cleaner & Log Automation")
    print("=" * 60)

    directory = input("Enter directory path: ")
    logging.info(f"Scanning Directory : {directory}")

    try:

        files, total_files, total_folders = scan_directory(directory)

        logging.info(f"Total Files : {total_files}")
        logging.info(f"Total Folders : {total_folders}")

        size_map = group_files_by_size(files)

        candidate_groups = get_duplicate_size_groups(size_map)

        logging.info(f"Candidate Groups : {len(candidate_groups)}")

        duplicates = find_duplicates(candidate_groups)

        duplicate_count = sum(
            len(file_list)
            for file_list in duplicates.values()
            if len(file_list) > 1
            )

        logging.info(f"Duplicate Files : {duplicate_count}")

        csv_report, json_report = generate_reports(duplicates)

        logging.info(f"CSV Report : {csv_report}")
        logging.info(f"JSON Report : {json_report}")

        logging.info("Application Finished Successfully")

        print("\nLog File")
        print(log_file)

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

        print("\nChoose an option")
        print("1. Move duplicate files to Trash")
        print("2. Skip")
        choice = input("\nEnter choice: ")
        if choice == "1":
            moved = move_duplicates(duplicates)
            logging.info(
                f"Moved Files : {moved}"
            )

            print(f"\nMoved {moved} duplicate files.")
        else:
            print("\nNo files moved.")

    except Exception as error:

        logging.exception(error)

        print(error)


if __name__ == "__main__":
    main()