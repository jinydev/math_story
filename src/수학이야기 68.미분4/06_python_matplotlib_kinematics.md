# 06. 여섯 번째 수업: 파이썬 Matplotlib 로켓 위치/속도 3단 그래프 시각화

지금까지 우리는 종이 위에 연필로 슥슥 찍 그으며 상상 임신으로 로켓을 날렸습니다. 
하지만 진짜 해커 관제탑은 코드를 짜는 순간 파이썬에 명령해 $X$시간당 $Y$높이, 속도 커브, 가속도 브레이크 이 3단 물리 패시브를 위아래 3줄 샌드위치 그래프로 아름다운 모니터 렌더링 시각 애니메이션 창에 뿌려버립니다!

`SymPy` 의 기호 미분 연산 머신으로 도함수와 2차 이계도함수 스크립트 공식을 $0.1$초 컷으로 모조리 뜯어내고, 그 공식에 시간($\mathbf{t}$) 초 단위 데이터 $100$개를 For 문으로 투척(`lambdify`) 하여 수천 개의 좌표 점 스파크 배열 리스트를 뽑아버립니다! 
그리고 궁극의 팩토리얼 데이터 페인터, **`Matplotlib`** 라이브러리가 그 파편 조각 점들을 아슬아슬하게 곡선 곡면 이음새를 스무스하게 연결 렌더링 해버리는, 그 미친 로켓 우주쇼의 막을 올립니다.

---

## 1. 3단 물리 엔진 통합 스캐너 스크립트 작성

```python
# [Python Code] 파이썬 관제 센터: 로켓 1차원 운동 3콤보 포물선(키네마틱스) 렌더링 UI
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# 1. 텍스트 심볼 방정식 t (Time 초) 할당. "이건 시간이 지배하는 우주 뼈대다!"
t = sp.Symbol('t')

# 2. 방금 우리가 던진 수류탄 로켓 위치 뼈대 무식한 포물선 방정식:
# h(t) = -5(t^2) + 30t  (1차 기초 맵 위치 x-좌표 데이터)
position_expr = -5 * t**2 + 30 * t

# 3. 2연타 미분 체인 발동! 맵 해킹 속도(1스택), 가속도(2스택) 엔진 센서 마스터키 획득!
velocity_expr = sp.diff(position_expr, t)
acceleration_expr = sp.diff(position_expr, t, 2)

# Sympy 기호 공식을 numpy 초고속 실수(float) 배열 연산 도가니 리스트 함수로 변형!
pos_func = sp.lambdify(t, position_expr, 'numpy')
vel_func = sp.lambdify(t, velocity_expr, 'numpy')
acc_func = sp.lambdify(t, acceleration_expr, 'numpy')

# 4. 물리 시뮬레이터 시간의 굴레(Time Bound) 타임라인 어레이 렌더링! (0초부터 ~ 6초까지)
# 파편 100개 점으로 촘촘히 썰어서 난사
t_vals = np.linspace(0, 6, 100)

# 도출해 낸 100개의 미세 오차 타임라인을 각 뼈대에 광속 대입!
p_vals = pos_func(t_vals)
v_vals = vel_func(t_vals)
# 가속도는 t가 없어도 그냥 항시 -10 중력 고정 상수 배열로 강제 복제!
a_vals = np.full_like(t_vals, acc_func(1)) 

# 5. ============= Matplotlib 도화지 3단 샌드위치 렌더링 UI 셋업 =============
# 화면에 상단, 중단, 하단 3개 팩토리얼 분할 보드로 도면 생성
fig, axs = plt.subplots(3, 1, figsize=(8, 10), sharex=True)

# [상단 도면] 로켓의 높이 (포물선 커브 U자)
axs[0].plot(t_vals, p_vals, 'g-', lw=3, label="Position h(t)")
axs[0].axvline(x=3, color='grey', linestyle='--', alpha=0.5) # 최고점 도달 3초 선 뷰어!
axs[0].set_ylabel('Height (m)')
axs[0].set_title('Rocket Physics Dashboard (Kinematics)')
axs[0].legend()
axs[0].grid(True)

# [중단 도면] 로켓의 순간 스피드 센서 속도계 (1차 미분 V)
axs[1].plot(t_vals, v_vals, 'b-', lw=3, label="Velocity v(t)")
axs[1].axhline(y=0, color='r', linestyle='--', alpha=0.5) # 정점 스피드 0 브레이크 턴 존!
axs[1].axvline(x=3, color='grey', linestyle='--', alpha=0.5)
axs[1].set_ylabel('Velocity (m/s)')
axs[1].legend()
axs[1].grid(True)

# [하단 도면] 중력 G-force 가속 압박 데미지 센서 (2차 더블 미분 A)
axs[2].plot(t_vals, a_vals, 'r-', lw=3, label="Acceleration a(t)")
axs[2].set_xlabel('Time (s)')
axs[2].set_ylabel('Acceleration (m/s^2)')
axs[2].legend()
axs[2].grid(True)

# 패널 간격 최적화 정렬 및 UI 플롯 폭발 모니터 표출 
plt.tight_layout()
plt.show() # (이 코드를 당신의 PC나 코랩 쥬피터에서 치면 기괴하고 압도적인 3단 맵핑 라인이 터집니다!)
```

## 2. 렌더링 결과의 충격: 모니터 뷰포트 해석

파이썬 창이 번쩍이며 뜨는 파란 배경 3단 그래프는 당신의 뒤통수를 칩니다.
1. 상단의 $h(t)$ 초록색 **위치 곡선**은 아름답고 높은 포물선 산 모양을 그리며 $t=3$ 초(가운데 지점) 에 수직 에베레스트 정상 높이 $45$m를 터치합니다. **이때 산꼭대기 수평선 기울기 계수는 제로 $\mathbf{0}$!** 
2. 그 순간! 바로 밑 칸 중단의 파란색 $v(t)$ **속도 일직선 빔**은 미친 듯한 마이너스 각도로 내려오고 있다가! 소름 돋게도 **정확히 $t=3$ 찰나의 프레임 스팟에서 붉은 눈금 $\mathbf{Y=0}$ (제로 속도 축 브레이크)** 를 바늘구멍 조준하듯 타격하고 음수 마이너스(하향 나락) 지옥으로 다이빙합니다! (속도가 완전히 역전됨)
3. 제일 하단의 시뻘건 $\mathbf{a(t)}$ 가속도 센서 엔진은 어떨까요? 애초에 시작 프레임($0$초) 부터 게임이 튕기는 최후 프레임($6$초) 까지 한 번도 굽어지지 않고, 그저 지독하게 차가운 파이프처럼 **$\mathbf{-10}$ 의 Y축 눈금에 일직선 상수 렌더링**을 수평으로 그으며 로켓을 땅으로 처박아 찢어 내리는 영원한 지구의 중력 G 를 디버깅해 냅니다.

미분 엔진이란 이렇게 하나의 $x^n$ 숫자 껍질을 연속 타격을 먹여서, 눈에 보이지 않던 스피드와 가속도의 숨겨진 매트릭스를 차례대로 해킹 추출해 내는 우주 최강의 스캐너 파츠였습니다! 
이제 이 잘게 부수고 쪼개 치졸한 기울기 프레임 단위로 만든 파편 쓰레기들을, 완전히 반대 방향 역추적 엔진을 역으로 점화시켜 조용히 쌓고 또 쌓아 영원한 2D 평면과 3D 부피 우주 맵 도형으로 마법처럼 합체 조립 복원해 버리는 거대한 스케일의 두 번째 모듈, **'적분(Integral Integration)' 1부 파트**로 화려하게 텔레포트 이동하겠습니다. 수고하셨습니다.
