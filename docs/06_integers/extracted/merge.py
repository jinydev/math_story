import os
import glob

base_dir = r"d:\site\jinydev\math_story\src\수학이야기 41.정수★\extracted\md"
output_file = r"d:\site\jinydev\math_story\src\수학이야기 41.정수★\extracted\merged_raw.txt"

# Get all .md files and sort them numerically
md_files = glob.glob(os.path.join(base_dir, "*.md"))
md_files.sort()

with open(output_file, 'w', encoding='utf-8') as outfile:
    for f in md_files:
        try:
            with open(f, 'r', encoding='utf-8') as infile:
                outfile.write(f"\n\n--- Source: {os.path.basename(f)} ---\n\n")
                outfile.write(infile.read())
        except Exception as e:
            outfile.write(f"\n\n--- Error reading {os.path.basename(f)}: {e} ---\n\n")

print(f"Successfully merged {len(md_files)} files into {output_file}")
