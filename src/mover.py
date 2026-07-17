import os 
import shutil
import logging

def move_duplicates(duplicates):

    trash_folder = "Trash"

    os.makedirs(trash_folder, exist_ok=True)

    moved_files = 0

    for file_hash, file_list in duplicates.items():
        if len(file_list) > 1:

            # Keep up the first file
            original_file = file_list[0]

            # Move the remaining files
            for duplicate_file in file_list[1:]:
                try:
                    filename = os.path.basename(duplicate_file)

                    destination = os.path.join(
                        trash_folder,
                        filename
                    )

                    # Avoid overwriting if the same filename already exists
                    if os.path.exists(destination):
                        base, extension = os.path.splitext(filename)
                        counter = 1

                        while True:
                            new_name = f"{base}_{counter}{extension}"
                            destination = os.path.join(
                                trash_folder,
                                new_name
                            )
                            if not os.path.exists(destination):
                                break

                            counter += 1
                    shutil.move(
                        duplicate_file,
                        destination
                    )

                    logging.info(
                        f"Moved: {duplicate_file} -> {destination}"
                    )

                    moved_files += 1

                except Exception as error:
                    logging.exception(error)
        
    return moved_files