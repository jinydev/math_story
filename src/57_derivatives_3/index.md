---
layout: level_05
title: '수학이야기 67.미분3'
parent: 수학이야기
nav_order: 67
has_children: true
---

# 수학이야기 67.미분3 (Derivative 3: 가속도와 등짝의 압력)

우린 앞선 두 번의 미분 단원을 통해 미분계수, 즉 $f'(x)$(순간 스피드) 레이더가 어떻게 기능하는지 마스터했습니다.
하지만 카트라이더 게임을 할 때 카트가 내는 속력만 중요한 게 아닙니다. 코너를 꺾으며 드리프트(Drift) 를 할 때 내 플레이어의 캐릭터가 **"오른쪽으로 미친 듯이 핸들을 꺾고 있는지, 왼쪽으로 확 꺾어 재끼는지" 그 핸들링(곡률) 의 쏠림 압력값**도 게임 엔진에 주입해야 완벽한 역학 모델이 렌더링 됩니다. 

이것을 알아내는 기술을 기하학에서는 곡선의 오목함(Concavity) 과 볼록함(Convexity) 이라고 하며, 물리 엔진에서는 이것을 **가속도 (Acceleration)** 라고 코딩합니다.
놀랍게도 아까 썼던 그 순간 스피드 미분 도함수 믹서기(`diff()`) 에다가 한 번 더 자동차를 밀어 넣고 **'미분을 두 번 쳐 버리면 (최강의 연속 해킹 콤보)'** 컴퓨터는 찰나의 속도가 아닌 가장 깊은 내면의 중력(G-force) 방향이라는 충격적인 압력 데이터를 모니터에 터트려 줍니다. 

**미분(Derivative) 3부** 단원에서는 도함수를 한 번 더 미분한 "이계도함수 $\mathbf{f''(x)}$" 의 파워를 이끌어 내어, 롤러코스터 그래프가 등판을 구부리는 무빙의 실체와 곡률이 뒤집히는 '변곡점(Inflection Point)' 의 버그 존을 사냥해 보겠습니다. 최후엔 파이썬 SymPy 로 2차 미분 오버클럭을 구현합니다.

---

## 목차

- [00. 인트로: 스피드의 스피드, G-Force 충격량 (Intro)](./00_intro/)
- [01. 첫 번째 수업: 속도 계기판 바늘마저 돌아가는 스피드, 이계도함수 $f''(x)$](./01_second_derivative_meaning/)
- [02. 두 번째 수업: 하늘정면 웃는 상($\cup$) vs 바닥 땅벌레 절망 상($\cap$) (Concave Up & Down)](./02_concave_up_down/)
- [03. 세 번째 수업: 중력 쏠림이 역전되는 찰나의 버그 충돌, 변곡점 (Inflection Point)](./03_inflection_points/)
- [04. 네 번째 수업: 나락의 폭주엔진! 가속도(Acceleration) 의 물리 렌더링 (Acceleration Physics)](./04_acceleration_physics/)
- [05. 다섯 번째 수업: 3D 심화 버그 디버깅, 기괴한 그래프 스캐닝 스킬 (Curve Sketching Advanced)](./05_curve_sketching_advanced/)
- [06. 여섯 번째 수업: 파이썬 SymPy 치트 중첩 시전! 미분기어 $2$단 터보 (Python Sympy Diff Diff)](./06_python_sympy_diff_diff/)
