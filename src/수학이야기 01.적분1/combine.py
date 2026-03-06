import os

md_dir = '/Users/hojin8/docs/070.강의/math_story/src/수학이야기 01.적분1/extracted/md'
target_dir = '/Users/hojin8/docs/070.강의/math_story/src/수학이야기 01.적분1'

chapters = [
    (0, 4, '00_책정보.md', '책 정보'),
    (5, 6, '01_추천사.md', '추천사'),
    (7, 8, '02_책머리에.md', '책머리에'),
    (9, 18, '03_차례_및_길라잡이.md', '차례 및 길라잡이'),
    (19, 27, '04_리만을_소개합니다.md', '리만을 소개합니다'),
    (28, 47, '05_첫_번째_수업_적분이란_무엇인가.md', '1. 첫 번째 수업: 적분이란 무엇인가?'),
    (48, 69, '06_두_번째_수업_적분의_원리.md', '2. 두 번째 수업: 적분의 원리'),
    (70, 97, '07_세_번째_수업_넓이구하기의_일반화.md', '3. 세 번째 수업: 넓이 구하기의 일반화 시도'),
    (98, 133, '08_네_번째_수업_적분기호.md', '4. 네 번째 수업: 적분 기호'),
    (134, 149, '09_다섯_번째_수업_dx의_딜레마.md', '5. 다섯 번째 수업: dx의 딜레마'),
    (150, 163, '10_여섯_번째_수업_적분과_넓이.md', '6. 여섯 번째 수업: 적분과 넓이'),
    (164, 182, '11_일곱_번째_수업_카발리에리의_원리.md', '7. 일곱 번째 수업: 카발리에리의 원리'),
    (183, 183, '12_저자_및_도서정보.md', '저자 및 도서 정보')
]

index_content = """# 수학자가 들려주는 수학 이야기 01 - 리만이 들려주는 적분 1 이야기

이 책은 복잡한 적분 계산보다는 적분이 등장하게 된 역사적 배경과 그 속에 담긴 수학자들의 고민을 통해 '적분'이라는 개념을 쉽고 직관적으로 이해할 수 있도록 구성되어 있습니다. 특히 도형의 넓이를 구하려는 소박한 열망에서 시작된 적분의 본질을 일곱 번의 수업을 통해 친절하게 안내합니다. 미적분을 처음 접하는 학생이나 기초를 다지고 싶은 분들에게 훌륭한 길라잡이가 될 것입니다.

## 학습 목표
* 수학에 얽힌 역사적 배경을 통해 수학을 거부감 없이 바라볼 수 있게 합니다.
* 적분의 필요성과 적분 기호 속에 담긴 적분의 진정한 의미를 이해합니다.
* 넓이 구하기 문제 해결을 통해 적분의 핵심 원리를 깨닫고 함수/그래프의 기초적 활용을 익힙니다.

## 목차
"""

for start, end, fname, title in chapters:
    content_lines = []
    for i in range(start, end + 1):
        md_file = os.path.join(md_dir, f"{i:03d}.md")
        if os.path.exists(md_file):
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read().strip()
                if content:
                    content_lines.append(f"<!-- page: {i:03d}.jpg -->\n" + content)
    
    out_path = os.path.join(target_dir, fname)
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write("\n\n<br><br>\n\n".join(content_lines))
    
    # 상대 경로 URI 형식 링크 (보통 현재 폴더의 파일은 상대 경로 파일명으로 직접 사용하거나 형식 지정)
    index_content += f"- [{title}](./{fname})\n"

index_path = os.path.join(target_dir, 'index.md')
with open(index_path, 'w', encoding='utf-8') as f:
    f.write(index_content)

print(f"Successfully created index.md and {len(chapters)} chapter files in {target_dir}")
