# 06. 여섯 번째 수업: 파이썬 Matplotlib 로 그리는 우주의 궤적 (Python Plotting)

수학은 단순히 시험지에서 $X, Y$ 를 까맣게 칠하는 것이 아닙니다. 진짜 코더들은 데카르트 형님이 만들어둔 $XY$ 좌표계 평면 위에 파이썬 `Matplotlib` 이라는 붓을 들어 방금 배운 "이차 곡선 포물선 방정식" 코드를 직접 쏘아 올려 렌더링 시킵니다.

바로 눈으로 확인해 보겠습니다!

---

## 1. 파이썬 그래픽스(Matplotlib) 와 포물선의 만남

위성 안테나의 기본 식인 $y^2 = 4px$ 를 그려볼 것입니다. 
파이썬은 보통 $y = f(x)$ 의 형태로 그림을 잘 그리기 때문에, 수식을 살짝 변형해 주면 아주 편합니다.

* $y^2 = 4px \quad \rightarrow \quad y = \pm\sqrt{4px}$
* 여기서 위쪽 입술 곡선($+$) 과 아래쪽 입술 곡선($-$) 두 개를 그려서 붙여 렌더링을 칠 겁니다. (포물선은 함수가 아니라 $y$값이 2개씩 점 찍히는 곡선 집합이기 때문이죠!)

```python
# [Python Code] 이차곡선: 포물선(Parabola)과 초점(Focus) 렌더링
import numpy as np
import matplotlib.pyplot as plt

# 1. 포물선 마스터 키 p 설정 (초점 좌표)
p = 3  
# 안테나 수신칩(Focus)의 X 좌표 위치는 3 미터 공중입니다.

# 2. X 좌표 픽셀을 0 부터 10 까지 100조각으로 아주 잘게 썰어서 준비
# 포물선은 x가 양수인 오른쪽에서만 열리므로 0부터 시작합니다.
x_vals = np.linspace(0, 10, 100)

# 3. Y 좌표 로직 렌더링 (y^2 = 4px -> y = 루트(4px), -루트(4px))
y_vals_positive = np.sqrt(4 * p * x_vals)  # 포물선의 위쪽 절반 뚜껑
y_vals_negative = -np.sqrt(4 * p * x_vals) # 포물선의 아래쪽 절반 바닥

# 4. 그림 그리기 시작 (도화지 세팅)
plt.figure(figsize=(8, 6))

# 위아래 포물선 곡선 찢어 그리기 (색상은 미래적인 Cyan 블루!)
plt.plot(x_vals, y_vals_positive, color='c', linewidth=2, label=f'y² = {4*p}x')
plt.plot(x_vals, y_vals_negative, color='c', linewidth=2)

# 5. 초점(Focus) 점 찍기
# 좌표 (p, 0) 즉, (3, 0) 지점에 붉은 수신기 점을 박아 넣는다.
plt.scatter(p, 0, color='r', s=100, zorder=5, label=f'Focus ({p}, 0)')

# 6. 버팀목 준선(Directrix) 그리기
# 초점이 3이라면, 반대쪽 벽면 준선은 x = -3 벽이 되어야 한다.
plt.axvline(x=-p, color='m', linestyle='--', label=f'Directrix x={-p}')

# 디자인 정리, 격자(Grid) 넣고 렌더링 샷 출력!
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend()
plt.title("Parabolic Antenna Focus & Directrix (Python Simulation)")
plt.axhline(0, color='black',linewidth=1)
plt.axvline(0, color='black',linewidth=1)
plt.xlim(-5, 12)
plt.ylim(-12, 12)
plt.show() # 모니터로 발사!
```

## 2. 코드 실행과 로켓 궤도의 이해

위 코드를 파이썬 IDE 쥬피터나 콜랩(Colab) 에서 `Shift + Enter` 로 날려보십시오!

거대한 흰색 도화지 정중앙 (점 $(0,0)$ 원점 꼭짓점) 에 닿아있던 푸른색 곡선이 오른쪽을 향해 아가리를 미친 듯이 벌리며 열리는 포물선(Parabola) 이 스크린에 강렬하게 렌더링 되어 출력될 것입니다.
그리고 정확히 그 궤적의 푹 파인 내장 안쪽 중심부 공중 허공 $(3, 0)$ $X$축 좌표 위치에, 붉고 강렬한 **붉은색 안테나 초점(Focus 점)** 이 떠 있습니다.

우측 무한대 우주 밖에서 저 푸른색 홈통 곡선 안쪽으로 어떤 레이저 전파 평행광선을 일직선으로 쏴대더라도, 그 빛은 무조건 둥근 거울 벽면(포물선) 에 부딪혀 직각으로 꺾인 다음, 붉은색 수신기(초점 $F$) 타겟 머리 위로 한 방울의 오차도 영원히 모여서 수렴하게 됩니다.

이 매끈한 타원 곡선의 수식 $y^2 = 12x$ 가 얼마나 기적 같은 로직을 품고 있는지 코드로 전율이 느껴지셨나요? 
이차곡선 파트 1에서는 포물선의 세계를 모험했습니다. 다음 파트 (모듈 56) 에서는 행성들의 움직임이자 기묘한 궤적의 제왕, "타원(Ellipse)" 과 우주 폭풍 이탈 "쌍곡선(Hyperbola)" 의 다중 렌더링 전투로 복귀하겠습니다! 
컴퓨터 모니터의 우주는 넓고, 당신이 칠 수 있는 함수 렌더링 코끼는 무궁무진합니다!
