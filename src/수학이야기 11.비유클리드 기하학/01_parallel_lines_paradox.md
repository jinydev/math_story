# 01. 휘어진 공간의 충격: 평면과 곡면의 평행선

## 1. 학습 목표 (Learning Objectives)
* 종이처럼 팽팽한 평면에서만 통하던 유클리드의 평행선 제5공준이, 곡면(구, 말안장 등)으로 세계가 바뀌면 어떻게 붕괴하는지 직관적으로 사고합니다.
* 파이썬(Python)의 `matplotlib` 3D 렌더링 스크립트를 통해 평평한 2D 격자와 둥글게 입체적으로 말린 3D 구면 격자를 시뮬레이션해 봅니다.

## 2. 평행선은 정말 영원히 만나지 않을까?
"기찻길처럼 나란히 놓인 두 선분은 우주 끝까지 가도 절대 만나지 않는다." 
이것이 교과서에서 알려준 평면 세계(유클리드 평면)의 철칙입니다.

하지만 만약 우리가 책상 위에 펼쳐둔 평평한 도화지(격자무늬가 있는)를 두 손으로 잡고 공처럼 둥글게 말아버리면 어떻게 될까요? 그림을 그리던 2차원의 백지 위상 자체가 뒤틀려 곡면(Curved Surface)이 되어버립니다. 
분명히 평평할 때는 절대 만나지 않던 일직선의 두 평행선이었는데, 종이를 둥글게 마는 순간 선들이 등고선을 타고 흐르다가 지구의 북극점(꼭대기)에서 쾅! 하고 충돌해버리게 됩니다.

즉, **"내가 발을 딛고 있는 땅(공간) 자체가 평평한가, 아니면 둥글게 휘어져 있는가?"** 에 따라 수학의 기초 법칙이 완전히 반대로 뒤집힌다는 사실입니다.

## 3. 파이썬 3D 공간 렌더링 시뮬레이터 (Python)
프로그래밍으로 이 위대한 공간의 차이를 시각화해보겠습니다. 선형대수학과 3차원 미적분학의 행렬 렌더링을 돕는 파이썬 코드를 작성합니다.

```python
import numpy as np
import matplotlib.pyplot as plt

def render_spaces():
    # ----------------------------------------------------
    # 1. 평평한 유클리드 평면 (Flat Space)
    # ----------------------------------------------------
    fig = plt.figure(figsize=(12, 5))
    ax1 = fig.add_subplot(121) # 1행 2열 중 1번째
    
    # x, y축으로 평평한 격자망(Grid) 생성
    x = np.linspace(-5, 5, 10)
    for i in x:
        ax1.plot([i, i], [-5, 5], color='royalblue', alpha=0.5) # 세로선
        ax1.plot([-5, 5], [i, i], color='tomato', alpha=0.5)    # 가로선
    
    # 만나지 않는 평행선 2개 그리기 (두꺼운 빨간선)
    ax1.plot([-4, 4], [2, 2], color='red', linewidth=3)
    ax1.plot([-4, 4], [-2, -2], color='red', linewidth=3)
    
    ax1.set_title("Euclidean Space (Flat)\nParallel Lines Never Meet", fontweight='bold')
    ax1.set_aspect('equal')
    ax1.axis('off')

    # ----------------------------------------------------
    # 2. 비유클리드 곡면 - 구면 기하학 (Spherical Space)
    # ----------------------------------------------------
    ax2 = fig.add_subplot(122, projection='3d') # 3차원 투영
    
    # 구(Sphere)를 만들기 위한 삼각함수 표면 공식 적용
    u = np.linspace(0, 2 * np.pi, 30) # 경도
    v = np.linspace(0, np.pi, 15)     # 위도
    x_sphere = 5 * np.outer(np.cos(u), np.sin(v))
    y_sphere = 5 * np.outer(np.sin(u), np.sin(v))
    z_sphere = 5 * np.outer(np.ones(np.size(u)), np.cos(v))
    
    # 구의 뼈대를 투명하게 렌더링
    ax2.plot_wireframe(x_sphere, y_sphere, z_sphere, color='teal', alpha=0.2)
    
    # 구면 위의 '평행'해 보이는 두 대원(큰 원, 직선 역할) 궤도 그리기
    circle_u = np.linspace(0, 2 * np.pi, 100)
    # 첫번째 궤도선 (적도 등)
    ax2.plot(5 * np.cos(circle_u), 5 * np.sin(circle_u), 0, color='red', linewidth=3)
    # 두번째 궤도선 (세로 자오선) -> 분명 처음에 직각으로 만남
    ax2.plot(5 * np.cos(circle_u), np.zeros_like(circle_u), 5 * np.sin(circle_u), color='red', linewidth=3)
    
    ax2.set_title("Non-Euclidean (Spherical Curved)\nLines WILL Collide!", fontweight='bold')
    ax2.axis('off')
    
    plt.tight_layout()
    # plt.show() # 로컬 실행 시 활성화하면 3D 창이 뜹니다.

render_spaces()
```

위의 파이썬 코드를 실행하면, 좌측에는 모눈종이 위에 안정적으로 평행을 달리는 두 개의 빨간 선이 보이지만, 우측 공간(공 모양)에서는 선의 길이가 길어지면 길어질수록 궤도가 휘어지면서 결국 구의 양극점에서 충돌하는 3D 결과물을 체감할 수 있습니다. 

## 4. 학습 정리 (Summary)
1. **공간의 위상 변화**: 종이를 둥글게 말거나 말안장처럼 휘어버리면, 그 2차원 표면 위를 걷고 있는 개미 입장에서는 **'절대 변하지 않는 평면'**이라는 상식이 붕괴됩니다.
2. 파이썬 `matplotlib 3D` 모듈은 $z$축이라는 한 단계 높은 차원 벡터를 더하여, 유클리드의 평면 세계(2D)를 비유클리드의 곡률 기반 3D 세계로 시뮬레이션 해주는 강력한 수학 렌더링 도구입니다.
