import os
import glob
import time
from google import genai
from PIL import Image

# ==========================================
# 1. 설정 (Configuration)
# ==========================================
API_KEY = "AIzaSyDcB9bdRZJib1tdYFy7dTq4a0RogBNhOZ4"

# 작업할 기본 폴더 경로
BASE_DIR = "/Users/hojin8/docs/070.강의/math_story/src"

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

PROMPT = """
이 이미지는 수학 책의 한 페이지입니다. 다음 규칙을 엄격히 시켜서 이미지의 내용을 텍스트로 추출해주세요.
1. 이미지의 내용을 1:1로 정확하게 마크다운(Markdown)으로 변환합니다.
2. 페이지 번호는 출력에서 제외합니다.
3. 수학 수식은 반드시 LaTeX($ 또는 $$)를 사용하여 작성합니다.
4. 표나 도식, 그림, 만화 등이 있다면 그 구조와 내용을 설명하거나 Mermaid(```mermaid)를 사용하여 유사하게 도식화해주세요.
5. 오직 변환된 마크다운 결과물만 출력합니다. (인사말 등 불필요한 말 제외)
"""

def setup_gemini():
    client = genai.Client(api_key=API_KEY)
    return client

def process_image(client, img_path):
    max_retries = 3
    for attempt in range(max_retries):
        try:
            img = Image.open(img_path)
            response = client.models.generate_content(
                model='gemini-2.5-flash',
                contents=[PROMPT, img]
            )
            return response.text
        except Exception as e:
            err_msg = str(e).lower()
            if "429" in err_msg or "quota" in err_msg or "exhausted" in err_msg:
                wait_sec = 20 * (attempt + 1)
                print(f" (할당량 초과/무료 한도 대기... {wait_sec}초 휴식) ", end="", flush=True)
                time.sleep(wait_sec)
            else:
                print(f"\n오류 발생 ({img_path}): {e}")
                time.sleep(5)
    return None

def create_index_md(chapter_dir, chapter_name, md_files):
    index_path = os.path.join(chapter_dir, "index.md")
    index_content = f"# {chapter_name}\n\n## 목차\n\n"
    for md_file in sorted(md_files):
        basename = os.path.basename(md_file)
        index_content += f"- [{basename}](extracted/md/{basename})\n"
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(index_content)
    print(f"\n[완료] {chapter_name} 의 index.md 가 생성되었습니다.")

def main():
    client = setup_gemini()
    folders_to_process = [os.path.join(BASE_DIR, ch) for ch in TARGET_CHAPTERS]
    
    for chapter_dir in folders_to_process:
        chapter_name = os.path.basename(chapter_dir)
        print(f"\n========================================")
        print(f"[{chapter_name}] Gemini API 기반 텍스트 추출 시작...")
        print(f"========================================")
        
        img_dir = os.path.join(chapter_dir, "extracted", "img")
        md_dir = os.path.join(chapter_dir, "extracted", "md")
        os.makedirs(md_dir, exist_ok=True)
        
        if not os.path.exists(img_dir):
            print(f"이미지 폴더 없음: {img_dir}")
            continue

        img_files = glob.glob(os.path.join(img_dir, "*.jpg")) + glob.glob(os.path.join(img_dir, "*.png"))
        img_files.sort()
        if not img_files:
            continue
            
        md_file_list = []
        total_images = len(img_files)
        
        for idx, img_path in enumerate(img_files, 1):
            basename = os.path.basename(img_path)
            md_filename = os.path.splitext(basename)[0] + ".md"
            md_path = os.path.join(md_dir, md_filename)
            md_file_list.append(md_path)
            
            if os.path.exists(md_path) and os.path.getsize(md_path) > 50:
                print(f"[{idx}/{total_images}] {basename} -> 이미 변환됨 (건너뜀)")
                continue
                
            print(f"[{idx}/{total_images}] {basename} 추출 중... ", end="", flush=True)
            text = process_image(client, img_path)
            if text:
                with open(md_path, "w", encoding="utf-8") as f:
                    f.write(text.strip())
                print("완료")
            else:
                print("실패 (최대 재시도 초과)")
            
            # API 분당 호출 제한(RPM) 우회를 위해 안전 대기 시간 증가
            time.sleep(4) 

        create_index_md(chapter_dir, chapter_name, md_file_list)

    print("\n🎉 전체 변환 완료!")

if __name__ == "__main__":
    main()
