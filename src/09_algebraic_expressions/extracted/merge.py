import os
import re

base_dir = r"d:\site\jinydev\math_story\src\수학이야기 32.식의계산\extracted"
md_dir = os.path.join(base_dir, "md")

chapters = [
    ("00_intro", 0, 23),
    ("01_첫_번째_수업", 24, 49),
    ("02_두_번째_수업", 50, 77),
    ("03_세_번째_수업", 78, 97),
    ("04_네_번째_수업", 98, 121),
    ("05_다섯_번째_수업", 122, 137),
    ("06_여섯_번째_수업", 138, 164),
    ("07_일곱_번째_수업", 165, 185),
    ("08_epilogue", 186, 187)
]

# regex to replace the absolute image path with a relative path
# Example: ![](/Users/hojin8/docs/070.강의/math_story/src/수학이야기 32.식의계산/extracted/img/0050.jpg) -> ![](./img/0050.jpg)
img_pattern = re.compile(r'!\[([^\]]*)\]\((?:[^)]*?/img/)([^)]+)\)')

for chapter_title, start_idx, end_idx in chapters:
    output_filename = f"{chapter_title}.md"
    output_path = os.path.join(base_dir, output_filename)
    
    combined_content = []
    
    for i in range(start_idx, end_idx + 1):
        filename = f"{i:04d}.md"
        filepath = os.path.join(md_dir, filename)
        
        if os.path.exists(filepath):
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                # Fix image paths
                content = img_pattern.sub(r'![\1](./img/\2)', content)
                combined_content.append(content.strip())
                
    # Join with newlines
    final_text = "\n\n".join(filter(None, combined_content))
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(final_text)
        
    print(f"Created {output_filename} with {end_idx - start_idx + 1} files.")

print("All chapters successfully merged.")
