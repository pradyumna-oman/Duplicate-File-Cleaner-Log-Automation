import logging

from src.scanner import scan_directory
from src.duplicate_detector import find_duplicates
from src.report import generate_reports
from src.optimizer import (
    group_files_by_size,
    get_duplicate_size_groups
)
from src.logger import setup_logger
from src.mover import move_duplicates
from src.cli import get_arguments


def main():
    # -------------------------------
    # Initialize Logger
    # -------------------------------
    log_file = setup_logger()

    logging.info("Application Started")

    print("=" * 60)
    print("Duplicate File Cleaner & Log Automation")
    print("=" * 60)

    # -------------------------------
    # Read Command Line Arguments
    # -------------------------------

    args = get_arguments()
    directory = args.path
    logging.info(f"Scanning Directory : {directory}")

    try:
        # -------------------------------
        # Scan Directory
        # -------------------------------
        files, total_files, total_folders = scan_directory(directory)

        logging.info(f"Total Files : {total_files}")
        logging.info(f"Total Folders : {total_folders}")

        # -------------------------------
        # Size Optimization
        # -------------------------------
        size_map = group_files_by_size(files)

        candidate_groups = get_duplicate_size_groups(size_map)

        logging.info(f"Candidate Groups : {len(candidate_groups)}")

        # -------------------------------
        # Find Duplicates
        # -------------------------------
        duplicates = find_duplicates(candidate_groups)

        duplicate_count = sum(
            len(file_list)
            for file_list in duplicates.values()
            if len(file_list) > 1
            )

        logging.info(
            f"Duplicate Files : {duplicate_count}"
            )
        
        # -------------------------------
        # Generate Reports
        # -------------------------------
        csv_report, json_report = generate_reports(duplicates)

        logging.info(f"CSV Report : {csv_report}")
        logging.info(f"JSON Report : {json_report}")

        # -------------------------------
        # Display Duplicate Report
        # -------------------------------

        print("\nDuplicate Report")
        print("-" * 60)

        duplicate_found = False

        for file_hash, file_list in duplicates.items():

            if len(file_list) > 1:
                duplicate_found = True
                print(f"\nSHA256 : {file_hash}")

                for file in file_list:print(f"   {file}")

        if not duplicate_found:
            print("No duplicate files found.")

        # -------------------------------
        # Move Duplicates (Optional)
        # -------------------------------
        if args.move:
            moved = move_duplicates(duplicates)

            logging.info(f"Moved Files : {moved}")

            print(f"\nMoved {moved} duplicate files.")
        else:
            print("\nMove operation skipped.")

        # -------------------------------
        # Display Summary
        # -------------------------------
        print("\nSummary")
        print("-" * 30)
        print(f"Files   : {total_files}")
        print(f"Folders : {total_folders}")
        print(f"Duplicate Files   : {duplicate_count}")

        print("\nReport Generated Successfully")
        
        print(f"CSV  : {csv_report}")
        print(f"JSON : {json_report}")

        print("\nLog File")
        print(log_file)
        
        logging.info("Application Finished Successfully")
        print("\nApplication Finished Successfully.")

    except Exception as error:
        logging.exception(error)
        print(f"\nError: {error}")

if __name__ == "__main__":
    main()