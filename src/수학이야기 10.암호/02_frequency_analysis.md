# 02. 시저 암호의 붕괴점, 빈도 분석법 (Frequency Analysis)

## 1. 학습 목표 (Learning Objectives)
* 하나의 평문이 고정된 하나의 암호문으로 1:1로만 매칭될 때 생기는 패턴의 통계학적 취약점을 간파합니다.
* 파이썬의 시각화 도구인 **`matplotlib`**을 동원해, 컴퓨터가 텍스트의 파편 비율을 꺾은선 막대 그래프로 렌더링하고 암호를 박살 내는 과정을 시뮬레이션합니다.

## 2. 모음 'E'의 절대적인 지배력
시저 암호와 같이 1:1로 고정된 알파벳 치환을 '단일 대치(단일 대치) 암호'라고 부릅니다. 이 암호는 얼핏 보기엔 완벽해 보입니다. 키 값을 모르는 사람이 알파벳을 수작업으로 때려 맞추려면 $26!$(약 $4 \times 10^{26}$, 400조의 조 배) 이라는 우주가 멸망할 때까지 셀 수 없는 경우의 수가 나오기 때문입니다.

그런데 고대와 중세를 호령하던 이 암호막을 산산조각 낸 천재적인 수학 기법이 9세기 아랍의 수학자 알 킨디에 의해 발명됩니다. 바로 **'빈도 분석법'**입니다.

인간이 쓰는 말(언어 패턴)에는 강력한 지문이 있습니다. 영어로 쓰인 수만 권의 책을 긁어모아 글자 수를 세어보면, 가장 많이 튀어나오는 압도적 1위 알파벳은 무조건 모음 **'E (약 13%)'** 입니다. 그다음이 **T, A, O, I, N** 순으로 떨어집니다. 반대로 'Z, Q, X' 등은 코빼기도 보이지 않습니다.

어떤 알 수 없는 긴~ 암호문 편지를 주웠습니다. 이 암호문에서 이상하게 **'X'**라는 찌그러진 글자가 유독 13% 비율로 엄청나게 쏟아진다면 어떻게 될까요?
암호학자는 싱긋 웃으며 말합니다. "보나마나 원본의 'E'라는 글자들을 암호화 하면서 무조건 'X'로 둔갑시켜 놨구만! X를 싹 다 E로 돌려놔!"

1:1 치환 암호는 철자의 '얼굴'만 바꿨을 뿐, 그것이 문장 속에서 뛰노는 **'빈도 점유율'의 영혼**까지는 덮지 못한다는 엄청난 모순을 지니고 있습니다.

## 3. 파이썬과 `matplotlib`를 이용한 통계 차트 (Python)
이번엔 프로그래머의 무기인 `matplotlib` 라이브러리를 써서 텍스트의 글자 비율을 계측하고, 눈에 보이는 그래프로 출력하는 시각화 코드를 맛보겠습니다.
이 코드는 개발 환경(Jupyter, VS Code 등)에서 실행하면 정말 예쁜 통계 바 차트를 그려냅니다.

```python
import collections
# matplotlib 모듈: 수학 데이터를 시각적인 2D 그래프/차트로 아름답게 그려주는 파이썬 국민 라이브러리
import matplotlib.pyplot as plt

def plot_frequency_analysis(text, is_cipher=False):
    # 특수문자를 제거하고 영문 알파벳(대문자) 파편만 걸러냅니다
    letters_only = [char.upper() for char in text if 'a' <= char.lower() <= 'z']
    
    # 파이썬 내장 Counter를 써서 각 글자가 몇 개(개수) 떴는지 초고속 계측
    counter = collections.Counter(letters_only)
    total_chars = sum(counter.values())
    
    # 딕셔너리 정렬 (알파벳 A부터 Z 순서대로 정렬)
    sorted_freq = dict(sorted(counter.items()))
    
    # ----------------------------------------------------
    # Matplotlib을 이용해 화면에 막대 그래프(Bar Chart) 그리기
    # ----------------------------------------------------
    plt.figure(figsize=(10, 5))
    x_keys = list(sorted_freq.keys())
    
    # 개수를 백분율(Percentage, %) 피크 비율로 환산
    y_percents = [(count / total_chars) * 100 for count in sorted_freq.values()]
    
    color_theme = 'tomato' if is_cipher else 'royalblue'
    title_str = 'Cipher Text Frequency (%)' if is_cipher else 'Original Text Frequency (%)'
    
    plt.bar(x_keys, y_percents, color=color_theme)
    plt.title(title_str, fontsize=15, fontweight='bold')
    plt.xlabel('Alphabet', fontsize=12)
    plt.ylabel('Frequency (%)', fontsize=12)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    # 이 명령어를 치면 모니터 창에 화려한 차트가 팝업됩니다!
    # plt.show() 

# 길고 정상적인 영문 평문 원본
sample_text = """
Mathematical structures are beautifully logical. The encryption of secrets
and decryption using frequency analysis creates a stunning battle of minds and code!
Even the legendary Julius Caesar couldn't defeat the immense power of statistics.
"""

# 막대 그래프 차트를 생성
plot_frequency_analysis(sample_text, is_cipher=False)
```

위 코드를 직접 구동하면 파란색의 촘촘한 막대그래프가 나타납니다. 그중 $E$ 기둥이 무려 13%에 달하는 고공 점프를 하며 독보적인 통계적 위용을 뽐내는 것을 눈으로 똑똑히 볼 수 있습니다. 이것이 데이터 사이언스(Data Science)가 암호에 접목되는 빛나는 순간입니다.

## 4. 학습 정리 (Summary)
1. **단일 대치(치환) 암호의 약점**: 하나의 글자를 고정된 다른 모양의 글자로 1:1 바꿀 경우, 원래 글자가 인간의 언어에서 가지고 있는 버릇과 비율(통계적 지문)을 그대로 상속받습니다.
2. **빈도 분석법 (Frequency Analysis)**: 암호문이 아무리 복잡해도 영문법과 단어의 파편 통계치(예: E의 초고비율 등장)를 꺾은선과 막대로 나열하여 끼워 맞추는 궁극의 해독 스나이퍼 기술입니다.
3. 파이썬의 `matplotlib` 라이브러리는 방대한 알파벳 문자열 더미를 직관적인 UI 차트로 렌더링해주는 최고의 무기입니다.
