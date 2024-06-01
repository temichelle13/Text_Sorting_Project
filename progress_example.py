
from tqdm import tqdm
import time  # This is just for demonstration purposes

def process_files(files):
    for file in tqdm(files, desc="Processing Files"):
        # Placeholder for file processing logic
        time.sleep(1)  # Simulate some processing time
    print("All files have been processed successfully!")

if __name__ == "__main__":
    files_to_process = ["file1.pdf", "file2.csv", "file3.png", "file4.docx"]  # Example file list
    process_files(files_to_process)
