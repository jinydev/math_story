import os
import re
import glob

src_dir = '/Users/hojin8/docs/070.강의/math_story/src'
unwritten = []
missing_images = []

for entry in os.listdir(src_dir):
    if not ('수학이야기' in entry or '수학이야기' in entry):
        continue
    dir_path = os.path.join(src_dir, entry)
    if not os.path.isdir(dir_path):
        continue
    
    # Check if written (has 01*.md)
    md_files = glob.glob(os.path.join(dir_path, '01*.md'))
    if not md_files:
        unwritten.append(entry)
        continue
        
    # Check for missing images under ## headings
    all_md = glob.glob(os.path.join(dir_path, '*.md'))
    for md_file in all_md:
        if 'index.md' in md_file:
            continue
        with open(md_file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Split by ##
        sections = re.split(r'\n## ', '\n' + content)
        for i, section in enumerate(sections):
            if i == 0: continue # Skip before first ##
            
            # Extract heading name
            heading = section.split('\n')[0].strip()
            
            # Check if there is an image (SVG, PNG, JPG, or <img> tag)
            has_image = bool(re.search(r'!\[.*?\]\([^)]+\)|<img[^>]+>|<svg[^>]*>', section, re.IGNORECASE))
            if not has_image:
                # ignore '학습 목표' or '도입부' or '결론' or '학습 정리'
                if any(x in heading for x in ['도입부', '학습 목표', '결론', '학습 정리']):
                    continue
                missing_images.append(f"{md_file} -> ## {heading}")

print("=== Unwritten Chapters ===")
for u in sorted(unwritten):
    print(u)

print("\n=== Missing Images in Written Chapters ===")
for m in sorted(missing_images):
    print(m)

