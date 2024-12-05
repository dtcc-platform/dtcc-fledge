### Script to compile ( concat ) markdown files for each chapter to complete document

import glob
import os
from pathlib import Path
# Specify the directory where your chapter files are located
cwd = Path(os.path.dirname(os.path.realpath(__file__)))
chapters_dir = cwd/Path('./Chapters')
print(chapters_dir)
draft_filename = "Draft-Deliverable-1.3.md"
# Build the glob pattern to match all Markdown files in the Chapters directory
pattern = os.path.join(chapters_dir, '*.md')

# Get a sorted list of all matching files
files = sorted(glob.glob(pattern))

# Print the list of files found
print("Files to concatenate:", files)

# Open the output file
with open(draft_filename, 'w', encoding='utf-8') as outfile:
    # Iterate over each file in the list
    for index,filename in enumerate(files,start= 0):
        # Check if the file exists
        if os.path.isfile(filename):
            print(f"Processing file: {filename}")
            with open(filename, 'r', encoding='utf-8') as infile:
                # Read the content and write it to the output file
                content = infile.read()
                # Replace placeholder with the chapter number
                content = content.replace('<!-- CHAPTER_NUMBER -->X', str(index))
                outfile.write(content)
                outfile.write('\n---\n\n')  # Add spacing between files
        else:
            print(f"File not found: {filename}")