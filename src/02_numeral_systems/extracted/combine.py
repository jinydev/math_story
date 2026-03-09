import os

ch_map = {
    1: (22, 48),
    2: (49, 69),
    3: (70, 97),
    4: (98, 133),
    5: (134, 151),
    6: (152, 175),
    7: (176, 193)
}

base_dir = r"d:\site\jinydev\math_story\src\수학이야기 07.기수법\extracted\md"
out_dir = r"d:\site\jinydev\math_story\src\수학이야기 07.기수법\extracted"

for ch, (start, end) in ch_map.items():
    combined_content = ""
    for i in range(start, end + 1):
        filename = f"{i:04d}.md"
        filepath = os.path.join(base_dir, filename)
        if os.path.exists(filepath):
            with open(filepath, 'r', encoding='utf-8') as f:
                combined_content += f"\n\n--- FILE: {filename} ---\n\n"
                combined_content += f.read()
    
    out_path = os.path.join(out_dir, f"ch{ch}_raw.txt")
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(combined_content)
    print(f"Created {out_path}")
