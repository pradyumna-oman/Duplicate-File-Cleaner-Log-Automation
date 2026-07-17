import argparse

def get_arguments():

    parser = argparse.ArgumentParser(
        description="Duplicate File Cleaner & Log Automation"
    )

    parser.add_argument(
        "--path",
        required=True,
        help="Directory to scan"
    )

    parser.add_argument(
        "--report",
        action="store_true",
        help="Generate reports only"
    )

    parser.add_argument(
        "--move",
        action="store_true",
        help="Move duplicate files to Trash"
    )

    return parser.parse_args()