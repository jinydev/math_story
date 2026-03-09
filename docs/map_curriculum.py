import os
import re
import unicodedata

# Read categories and elements
groups = {
    "초": [5, 33, 22, 62],
    "중": [3, 4, 7, 9, 12, 13, 14, 18, 20, 25, 26, 27, 28, 29, 30, 32, 41, 42, 44, 48, 54, 77, 84, 87],
    "고": [1, 2, 15, 24, 31, 34, 35, 36, 37, 39, 40, 43, 45, 46, 47, 49, 52, 53, 55, 56, 59, 60, 61, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 74, 78, 79, 80, 82, 83, 86],
    "대학": [11, 21, 23, 51, 81, 85, 88],
    "일반": [6, 8, 10, 16, 38, 50, 57, 58, 73, 75, 76]
}

src_dir = '/Users/hojin8/docs/070.강의/math_story/src'
dirs = [d for d in os.listdir(src_dir) if os.path.isdir(os.path.join(src_dir, d))]

parsed_dirs = []
for d in dirs:
    d_nfc = unicodedata.normalize('NFC', d)
    if '수학이야기' not in d_nfc:
        continue
    match = re.search(r'(\d+)\.\s*(.+)', d_nfc)
    if match:
        num = int(match.group(1))
        title = match.group(2).strip()
        
        # Count files to prefer the real directory
        full_path = os.path.join(src_dir, d)
        count = 0
        for _, _, files in os.walk(full_path):
            count += len(files)
            
        parsed_dirs.append((num, title, d, count))

# Sort by number, then by file count descending
parsed_dirs.sort(key=lambda x: (x[0], -x[3]))

# Remove duplicates based on num
unique_parsed = []
seen = set()
for p in parsed_dirs:
    if p[0] not in seen:
        unique_parsed.append(p)
        seen.add(p[0])

mapped = {"초": [], "중": [], "고": [], "대학": [], "일반": [], "미분류": []}

for num, title, origin, count in unique_parsed:
    found = False
    for g, nums in groups.items():
        if num in nums:
            mapped[g].append((num, title, origin))
            found = True
            break
    if not found:
        mapped["미분류"].append((num, title, origin))

plan_content = []
plan_content.append("# 📚 수학 이야기 커리큘럼 기반 폴더 재구성 계획 (Implementation Plan)\n")
plan_content.append("## 1. 개요\n")
plan_content.append("현재 출판 순서대로 번호가 부여되어 있는 폴더들을 대한민국 교육과정 순서(초 -> 중 -> 고 -> 대학 -> 일반)에 맞추어 `xx_챕터이름` 형태로 일괄 변경합니다. 새로운 번호 `xx`는 초등 01번부터 일반 86번까지 순차적으로 부여됩니다.\n")
plan_content.append(f"## 2. 변경 계획 (Total: {len(unique_parsed)} directories)\n")

new_idx = 1
rename_commands = []

for g in ["초", "중", "고", "대학", "일반", "미분류"]:
    if mapped[g]:
        plan_content.append(f"### 📍 {g}등/과정 ({len(mapped[g])}개)\n")
        for num, title, origin in mapped[g]:
            new_name = f"{new_idx:02d}_{title}"
            plan_content.append(f"- `[{g}]` `{origin}` ➡️ `{new_name}`\n")
            rename_commands.append(f'mv "{src_dir}/{origin}" "{src_dir}/{new_name}"')
            new_idx += 1
        plan_content.append("\n")

plan_content.append("## 3. 검토 요청 사항\n")
plan_content.append("제가 제안하는 교과과정 매핑(초/중/고/대학/일반)이 적절한지 확인 부탁드립니다. (예: `경우의수`를 중등으로 묶었으며 필요시 고등으로 변경 가능합니다.) 수정이 필요한 부분이 있다면 말씀해 주세요.\n")
plan_content.append("승인해 주시면 위의 계획대로 일괄 폴더명 변경 스크립트를 실행하겠습니다.\n")

with open('/Users/hojin8/.gemini/antigravity/brain/b4c08e32-d5d3-4249-8c9f-d844688d18ef/implementation_plan.md', 'w') as f:
    f.writelines(plan_content)

with open(f'{src_dir}/rename_script.sh', 'w') as f:
    f.write('\n'.join(rename_commands))
