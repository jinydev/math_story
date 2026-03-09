import os, glob, re

src_dir = '/Users/hojin8/docs/070.강의/math_story/src'
missing_images = []

for entry in os.listdir(src_dir):
    if not ('수학이야기' in entry or '수학이야기' in entry):
        continue
    dir_path = os.path.join(src_dir, entry)
    if not os.path.isdir(dir_path):
        continue
        
    all_md = glob.glob(os.path.join(dir_path, '*.md'))
    for md_file in all_md:
        if 'index.md' in md_file:
            continue
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
            sections = re.split(r'\n## ', '\n' + content)
            for i, section in enumerate(sections):
                if i == 0: continue
                heading = section.split('\n')[0].strip()
                has_image = bool(re.search(r'!\[.*?\]\([^)]+\)|<img[^>]+>|<svg[^>]*>', section, re.IGNORECASE))
                if not has_image:
                    if any(x in heading for x in ['도입부', '학습 목표', '결론', '학습 정리']):
                        continue
                    # also ignore "1. 파이썬 주사위 오토 클릭 시뮬레이터" if it represents code block mostly?
                    # The instruction says "## 마다 최소한 1개 이상의 이미지"
                    missing_images.append(f"{entry}/{os.path.basename(md_file)} -> ## {heading}")
        except Exception as e:
            pass

print(f"Total ## sections missing images: {len(missing_images)}")
