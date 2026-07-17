import logging

from src.application import DuplicateCleanerApplication
from src.cli import get_arguments


def main():

    print("=" * 60)
    print("Duplicate File Cleaner & Log Automation")
    print("=" * 60)

    args = get_arguments()

    try:

        app = DuplicateCleanerApplication(args)

        app.run()

    except Exception as error:

        logging.exception(error)

        print(f"\nError : {error}")


if __name__ == "__main__":
    main()