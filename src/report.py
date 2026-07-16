import csv
import os


def generate_csv_report(duplicates):

    os.makedirs("reports", exist_ok=True)

    report_path = os.path.join(
        "reports",
        "duplicate_report.csv"
    )

    with open(report_path,
              "w",
              newline="",
              encoding="utf-8") as csv_file:

        writer = csv.writer(csv_file)

        writer.writerow([
            "SHA256",
            "File Path"
        ])

        for file_hash, file_list in duplicates.items():

            if len(file_list) > 1:

                for file in file_list:

                    writer.writerow([
                        file_hash,
                        file
                    ])

    return report_path