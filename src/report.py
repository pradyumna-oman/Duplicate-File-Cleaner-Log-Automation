import csv
import json
import os
from datetime import datetime


def generate_reports(duplicates):

    os.makedirs("reports", exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    csv_path = os.path.join(
        "reports",
        f"duplicate_report_{timestamp}.csv"
    )

    json_path = os.path.join(
        "reports",
        f"duplicate_report_{timestamp}.json"
    )

    report_data = []

    with open(csv_path,
              "w",
              newline="",
              encoding="utf-8") as csv_file:

        writer = csv.writer(csv_file)

        writer.writerow([
            "SHA256",
            "File Name",
            "File Path",
            "Size (Bytes)",
            "Last Modified"
        ])

        for file_hash, file_list in duplicates.items():

            if len(file_list) > 1:

                for file in file_list:

                    size = os.path.getsize(file)

                    modified = datetime.fromtimestamp(
                        os.path.getmtime(file)
                    )

                    writer.writerow([
                        file_hash,
                        os.path.basename(file),
                        file,
                        size,
                        modified
                    ])

                    report_data.append({
                        "sha256": file_hash,
                        "file_name": os.path.basename(file),
                        "file_path": file,
                        "size": size,
                        "last_modified": str(modified)
                    })

    with open(json_path,
              "w",
              encoding="utf-8") as json_file:

        json.dump(
            report_data,
            json_file,
            indent=4
        )

    return csv_path, json_path