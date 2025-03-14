import os
import re

# Set the directory where the comic files are stored
folder_path = r"C:/Users/corsi/Comics/Seed"

# Regular expression to match files with format: "seed ChXXX.YYY.jpg"
pattern = re.compile(r"seed Ch(\d+)\.\d+\.jpg")

# Iterate over all files in the directory
for filename in os.listdir(folder_path):
    match = pattern.match(filename)

    if match:
        chapter = int(match.group(1))  # Extract chapter number

        # Only delete files from chapter 100 onward
        if chapter >= 100:
            file_path = os.path.join(folder_path, filename)
            
            try:
                os.remove(file_path)
                print(f"Deleted: {filename}")
            except Exception as e:
                print(f"Error deleting {filename}: {e}")

print("Deletion process completed.")
