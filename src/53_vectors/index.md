---
layout: level_05
title: '수학이야기 64.벡터'
parent: 수학이야기
nav_order: 64
has_children: true
---

# 수학이야기 64.벡터 (Vector: Arrows in Space)

지금까지 배운 수학(방정식, 넓이, 확률) 은 대부분 크기나 양(수치) 만 있는 데이터인 **'스칼라(Scalar)'** 의 세계였습니다.
"내 공격력이 $100$이다, 몬스터 체력이 $50$이다, 온도가 $30^\circ\text{C}$ 다." 이런 데이터들은 단순히 엑셀 칸 하나에 들어가는 숫자 쪼가리일 뿐, 화면상의 "움직임" 이나 "물리가 작용하는 힘" 을 구현해 낼 수 없습니다.

하지만 게임과 물리 엔진의 세계에서, 총알이 어느 쪽으로 날아갈지, 우주선이 어느 방향으로 가속 엔진을 터트릴지 결정하려면 숫자 하나로는 턱없이 부족합니다. 
우리에겐 **"얼마나 쎈 힘으로 (크기 Magnitude)" + "어디를 향해 (방향 Direction)"** 날아갈 것인지를 하나로 묶어놓은 위대한 화살표 데이터 팩토리얼 캡슐이 필요합니다.

이번 **벡터(Vector)** 단원에서는 2D/3D 공간에서 날아다니는 기하학의 화살표 렌더링을 뜯어봅니다. 단순히 길이를 갖는 몽둥이가 아니라, "방향" 이라는 영혼을 이식받은 화살표들이 어떻게 서로 꼬리를 물며 더해지고(합력), 충돌하며(차), 코딩 좌표평면 위를 찢고 날아가는지 파이썬 NumPy 배열 엔진과 함께 해부해 보겠습니다. 

---

## 목차

- [00. 인트로: 우주선의 가속 엔진과 방향타 (Intro)](00_intro)
- [01. 첫 번째 수업: 데이터의 영혼, 스칼라(Scalar) 와 벡터(Vector) (Scalar vs Vector)](01_scalar_vs_vector)
- [02. 두 번째 수업: 벡터를 쪼개라! X축과 Y축 컴포넌트 분해 (Vector Components)](02_vector_components)
- [03. 세 번째 수업: 화살표 꼬리 잡기 렌더링, 벡터의 덧셈 (Vector Addition)](03_vector_addition)
- [04. 네 번째 수업: 나를 향해 날아오는 과녁, 벡터의 뺄셈 (Vector Subtraction)](04_vector_subtraction)
- [05. 다섯 번째 수업: 에네르기파 뻥튀기! 스칼라 곱셈 (Scalar Multiplication)](05_scalar_multiplication)
- [06. 여섯 번째 수업: 파이썬 넘파이(NumPy) 우주선 가속도 시뮬레이터 (Python NumPy Vectors)](06_python_numpy_vectors)
