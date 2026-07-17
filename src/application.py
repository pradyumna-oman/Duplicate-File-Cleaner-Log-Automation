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


class DuplicateCleanerApplication:

    def __init__(self, args):
        self.args = args
        self.log_file = setup_logger()

    def display_duplicate_report(self, duplicates):
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

    def display_summary(
        self,
        total_files,
        total_folders,
        duplicate_count,
        csv_report,
        json_report,
    ):

        print("\nSummary")
        print("-" * 30)

        print(f"Files             : {total_files}")
        print(f"Folders           : {total_folders}")
        print(f"Duplicate Files   : {duplicate_count}")

        print("\nReports Generated")

        print(f"CSV  : {csv_report}")
        print(f"JSON : {json_report}")

        print("\nLog File")
        print(self.log_file)

    def run(self):

        logging.info("Application Started")
        
        directory = self.args.path

        logging.info(f"Scanning Directory : {directory}")

        files, total_files, total_folders = scan_directory(directory)

        logging.info(f"Total Files : {total_files}")
        logging.info(f"Total Folders : {total_folders}")

        size_map = group_files_by_size(files)

        candidate_groups = get_duplicate_size_groups(size_map)

        logging.info(
            f"Candidate Groups : {len(candidate_groups)}"
        )

        duplicates = find_duplicates(candidate_groups)

        duplicate_count = sum(
            len(file_list)
            for file_list in duplicates.values()
            if len(file_list) > 1
        )

        logging.info(
            f"Duplicate Files : {duplicate_count}"
        )

        csv_report, json_report = generate_reports(
            duplicates
        )

        logging.info(f"CSV Report : {csv_report}")
        logging.info(f"JSON Report : {json_report}")

        self.display_duplicate_report(
            duplicates
        )

        if self.args.move:

            moved = move_duplicates(
                duplicates
            )

            logging.info(
                f"Moved Files : {moved}"
            )

            print(
                f"\nMoved {moved} duplicate files."
            )

        else:

            print("\nMove operation skipped.")

        self.display_summary(
            total_files,
            total_folders,
            duplicate_count,
            csv_report,
            json_report,
        )

        logging.info(
            "Application Finished Successfully"
        )