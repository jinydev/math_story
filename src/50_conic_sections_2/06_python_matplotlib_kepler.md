---
layout: "docs"
title: '06. 여섯 번째 수업 파이썬으로 렌더링 하는 케플러의 우주 Python Matplotlib'
---

# 06. 여섯 번째 수업: 파이썬으로 렌더링 하는 케플러의 우주 (Python Matplotlib)

인수분해를 통해 도출된 타원(Ellipse) 과 쌍곡선(Hyperbola) 의 기하학적 수식을 종이 위에서 암기하는 것은 끝났습니다.
진짜 컴퓨터 공학도라면 이 행성 공전 궤도 코드를 파이썬 데이터 시각화의 제왕, `Matplotlib` 에 직접 박아 넣어서 우주 모델 시뮬레이션을 내 모니터 위에 라이브로 띄워 봐야 직성이 풀릴 것입니다.

두 개의 궤도를 하나의 캔버스 뷰포트(Viewport) 에 올려보겠습니다.

---

## 1. 닫힌 궤도(타원) & 무한 궤도(쌍곡선) 렌더링

![파이썬 렌더링 시뮬레이션](./img/06_python_kepler_python.png)

방정식 $y$ 값을 $\pm \sqrt{\ }$ 로 스왑 변환하여 우주 위, 아래쪽 패치 곡선을 따로 찢어 붙이는 로직은 지난번 포물선 렌더링과 완전히 동일한 트릭입니다.

```python
# [Python Code] 태양계의 행성 궤도(타원) vs 태양계 탈출 위성 궤도(쌍곡선)
import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# 1. 타원(Ellipse) 행성 궤적: x^2/25 + y^2/9 = 1
# ==========================================
a_el = 5  # 가로 반지름(장축) 최고 한계치
b_el = 3  # 세로 두께(단축) 
c_el = np.sqrt(a_el**2 - b_el**2)  # 초점 좌표 위치 계산 (피타고라스 차이)

# 타원의 X 좌표는 한계 허용치가 -5 ~ +5 로 100% 닫혀 있다. 
x_el = np.linspace(-a_el, a_el, 400)
# y = ± b * sqrt(1 - (x/a)^2) 로직으로 타원의 윗뚜껑과 아랫뚜껑 장착
y_el_top = b_el * np.sqrt(1 - (x_el**2 / a_el**2))
y_el_bot = -b_el * np.sqrt(1 - (x_el**2 / a_el**2))


# ==========================================
# 2. 쌍곡선(Hyperbola) 이탈 궤적: x^2/4 - y^2/9 = 1
# ==========================================
a_hy = 2  # 양옆 꼭짓점 열림 시작 위치
b_hy = 3  # 점근선 기울기를 결정하는 가상의 Y 오프셋

# X 좌표를 2부터 8까지만 추출 (무한대 우주 밖으로 도망가는 우측 궤도들만!)
x_hy = np.linspace(a_hy, 8, 400)
# y = ± b * sqrt((x/a)^2 - 1) 로직으로 쌍곡선의 위아래 방사 곡선 장착
y_hy_top = b_hy * np.sqrt((x_hy**2 / a_hy**2) - 1)
y_hy_bot = -b_hy * np.sqrt((x_hy**2 / a_hy**2) - 1)

# 무시무시한 유리벽 통제선 (점근선 Asymptotes)
x_asymp = np.linspace(-8, 8, 400)
y_asymp_1 = (b_hy / a_hy) * x_asymp
y_asymp_2 = -(b_hy / a_hy) * x_asymp


# ==========================================
# 3. 도화지 뷰포트 그리기 엔진 발사!
# ==========================================
plt.figure(figsize=(10, 8))

# 타원 (파란색 달걀 궤적) 과 두 개의 태양 블랙홀 초점(Red) 렌더링
plt.plot(x_el, y_el_top, 'b-', linewidth=2, label="Ellipse Orbit (Planet)")
plt.plot(x_el, y_el_bot, 'b-', linewidth=2)
plt.scatter([c_el, -c_el], [0, 0], color='r', s=80, label=f"Foci of Ellipse", zorder=5)

# 쌍곡선 (붉은색 우주 탈출 궤적) 과 한계 유리벽 점근선(점선) 렌더링
plt.plot(x_hy, y_hy_top, 'r-', linewidth=2, label="Hyperbola Escape Orbit")
plt.plot(x_hy, y_hy_bot, 'r-', linewidth=2)
plt.plot(-x_hy, y_hy_top, 'r-', linewidth=2)  # 좌측 데칼코마니 복사!
plt.plot(-x_hy, y_hy_bot, 'r-', linewidth=2)
plt.plot(x_asymp, y_asymp_1, 'k--', alpha=0.4, label="Asymptotes Limit Vector")
plt.plot(x_asymp, y_asymp_2, 'k--', alpha=0.4)

# 무대 UI 정교화 작업 (가로세로 축과 디자인)
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)
plt.xlim(-8, 8)
plt.ylim(-6, 6)
plt.title("Cosmic Orbit Simulation: Kepler's Ellipse vs Escape Hyperbola")
plt.legend()
plt.grid(True, linestyle=':', alpha=0.5)

plt.show()  # 모니터 출력 명령!
```

## 2. 렌더링 결과로 보는 우주의 민낯 (Insights)

코드 실행에 성공하고 모니터(결과 화면) 를 쳐다보면 소름 돋게 대비되는 우주의 규칙 2가지가 한 번에 섞여서 나타납니다.

1. 화면 가장 안쪽을 파랗게 점유하는 **닫힌 타원(Ellipse)**. 두 개의 붉은 태양(초점) 을 번갈아 빙빙 감싸 돌며 영원히 제자리로 단축/장축을 반복하는 행성의 안정적인 노예 궤도(케플러 법칙)가 보입니다. 
2. 그러나 더 바깥쪽을 점유하는 붉은색의 거대한 **쌍곡선(Hyperbola)** 줄기들을 보십시오! 좌우 모니터 양 끝에서 무한대로 도망가며 떨어져 나가는 위엄을 뽐냅니다. 그리고 그 선들의 끝은 방탄유리 레이저 결계 선인 까만 점선 $X$자(Asymptotes, 점근선) 에 거미줄처럼 위태롭게 달라붙어 평행으로 따라가지만 절대로 선로를 침범하지 못한 채 무한한 심연 밖으로 사라져 날아가 버립니다.

자! 우리가 배운 인수분해와 고대 기하학 원뿔 절단기 마법 스킬 편. 
그 모형이 곧 $2$차 방정식 $\rightarrow XY$ 함수 차트를 가로질러 마침내 파이썬 애니메이션 행성계 시뮬레이터로 시원하게 터져 나왔습니다. 

이차 곡선 단원을 여기, 케플러 우주의 정복으로 화려하게 스며들며 종료합니다! 
다음번에는 우주의 가장 막무가내 잡학 괴물 확률(Probability) 카지노 세계로 돌아와, 주사위의 도박수 패턴을 어떻게 컴퓨터 시스템 확률 공식 해킹으로 잡아 가두는지 배워보겠습니다. 수고하셨습니다!
