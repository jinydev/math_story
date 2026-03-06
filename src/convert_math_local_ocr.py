import os
import glob
import time
import pytesseract
from PIL import Image

# ==========================================
# 1. 설정 (Configuration)
# ==========================================
# 작업할 기본 폴더 경로
BASE_DIR = "/Users/hojin8/docs/070.강의/math_story/src"

# 변환하고 싶은 챕터 목록 (모든 추가 요청 폴더 포함)
TARGET_CHAPTERS = [
    "수학이야기 07.기수법",
    "수학이야기 20.좌표",
    "수학이야기 26.실수1",
    "수학이야기 36.복소수",
    "수학이야기 41.정수★",
    "수학이야기 62.자연수",
    "수학이야기 63.실수2",
    "수학이야기 83.적분2",
    "수학이야기 84.유리수",
    "수학이야기 02.집합",
    "수학이야기 05.약수와배수1",
    "수학이야기 33.약수와배수2",
    "수학이야기 76.선택과 배열",
    "수학이야기 77.근삿값과 오차"
]

def create_index_md(chapter_dir, chapter_name, md_files):
    # 챕터 폴더에 index.md 만들기
    index_path = os.path.join(chapter_dir, "index.md")
    
    index_content = f"# {chapter_name}\n\n"
    index_content += "## 목차\n\n"
    
    for md_file in sorted(md_files):
        basename = os.path.basename(md_file)
        index_content += f"- [{basename}](extracted/md/{basename})\n"
        
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(index_content)
    print(f"\n[완료] {chapter_name} 의 index.md 가 생성되었습니다.")

def main():
    folders_to_process = []
    if TARGET_CHAPTERS:
        folders_to_process = [os.path.join(BASE_DIR, chapter) for chapter in TARGET_CHAPTERS]
    else:
        # 모든 '수학이야기' 폴더 작업 (지정하지 않을 경우)
        for item in sorted(os.listdir(BASE_DIR)):
            if item.startswith("수학이야기") and os.path.isdir(os.path.join(BASE_DIR, item)):
                folders_to_process.append(os.path.join(BASE_DIR, item))

    for chapter_dir in folders_to_process:
        chapter_name = os.path.basename(chapter_dir)
        print(f"\n========================================")
        print(f"[{chapter_name}] **빠른 로컬 OCR 텍스트 변환** 시작...")
        print(f"========================================")
        
        img_dir = os.path.join(chapter_dir, "extracted", "img")
        md_dir = os.path.join(chapter_dir, "extracted", "md")
        
        # md 폴더가 없다면 생성
        os.makedirs(md_dir, exist_ok=True)
        
        if not os.path.exists(img_dir):
            print(f"이미지 폴더가 존재하지 않음: {img_dir}")
            continue

        # jpg, png 등 이미지 찾기
        img_files = glob.glob(os.path.join(img_dir, "*.jpg")) + glob.glob(os.path.join(img_dir, "*.png"))
        img_files.sort()
        
        if not img_files:
            print(f"이미지 파일이 없습니다: {img_dir}")
            continue
            
        md_file_list = []
        total_images = len(img_files)
        
        # 이미지 파일 끝까지 모두 순회
        for idx, img_path in enumerate(img_files, 1):
            basename = os.path.basename(img_path)
            md_filename = os.path.splitext(basename)[0] + ".md"
            md_path = os.path.join(md_dir, md_filename)
            md_file_list.append(md_path)
            
            # 이미 변환된 파일이 있다면 건너뛰기 
            if os.path.exists(md_path) and os.path.getsize(md_path) > 10:
                print(f"[{idx}/{total_images}] {basename} -> 마크다운 이미 존재함 (건너뜀)")
                continue
                
            print(f"[{idx}/{total_images}] {basename} 텍스트 추출 중...", end="", flush=True)
            
            try:
                img = Image.open(img_path)
                # pytesseract를 통해 한국어(kor)와 영어(eng) 동시 추출
                ocr_text = pytesseract.image_to_string(img, lang='kor+eng')
                
                with open(md_path, "w", encoding="utf-8") as f:
                    f.write(ocr_text.strip())
                print(" 완료.")
            except Exception as e:
                print(f" 실패: {e}")
                continue

        # 챕터 완료 후 index.md 생성
        create_index_md(chapter_dir, chapter_name, md_file_list)

    print("\n🎉 모든 폴더의 빠른 변환 작업이 끝났습니다!")

if __name__ == "__main__":
    main()
