---
layout: level_03
title: '수학이야기 69.행렬'
parent: 수학이야기
nav_order: 69
has_children: true
---

# 수학이야기 69.행렬 (Matrix: 우주를 찌그러뜨리는 선형 변환 마법진)

미분, 적분이 곡선이라는 슬라임을 다루는 칼날이었다면, **행렬(Matrix)** 은 프로그래밍에서 이 세계(좌표 평면 격자) 전체 공간을 통째로 움켜쥐고 늘리고 비틀고 짓이겨 버리는 물리적 시공간 왜곡 스펠(마법진) 입니다.

영화 "매트릭스(Matrix)" 에서 네오가 멈춰버린 총알의 격자 코드를 보는 것처럼, 엑셀 표처럼 네모나게 줄지어 정렬된 숫자들의 박스가 바로 행렬입니다. 딥러닝 AI 파면에서 "텐서(Tensor)" 라고 부르는 것이 바로 고차원 행렬이며, ChatGPT 의 뇌 또한 수천억 개의 행렬 곱셈 부품이 미친 듯이 연산을 토해내는 공장일 뿐입니다.

수학이야기 69, 이번 **행렬(Matrix)** 단원에서는 배열 안에 숫자를 정리하는 단순한 데이터베이스 표로서의 행렬을 넘어, 두 행렬이 충돌했을 때 일어나는 기괴한 '행렬의 곱셈(Matrix Multiplication)' 과, 그래픽 엔진에서 오브젝트를 회전시키고 왜곡시키는 '선형 변환(Linear Transformation)' 의 진짜 마법을 시각적으로 렌더링 해보겠습니다. 

이 단원을 마치면 파이썬 Numpy 배열이 왜 행렬인지 직감하게 됩니다. 

---

## 목차

- [00. 인트로: 엑셀 표가 아닌 우주의 마법 주문 배열 (Intro)](00_intro)
- [01. 첫 번째 수업: 데이터베이스 격자 타일링, 행렬의 구조 (What is Matrix)](01_what_is_matrix)
- [02. 두 번째 수업: 같은 크기 픽셀끼리의 병합, 덧셈과 뺄셈 (Addition & Subtraction)](02_addition_subtraction)
- [03. 세 번째 수업: 전체 스케일 폭주 버프, 실수배 (Scalar Multiplication)](03_scalar_multiplication)
- [04. 네 번째 수업: 내적(Dot) 충돌 데미지 매트릭스, 행렬의 곱셈 (Matrix Multiplication)](04_matrix_multiplication)
- [05. 다섯 번째 수업: 시공간을 늘리고 비틀어라! 선형 변환 (Linear Transformation)](05_linear_transformation)
- [06. 여섯 번째 수업: 파이썬 NumPy AI 텐서 행렬 폭격 연산 (Python NumPy Matrix)](06_python_numpy_matrix)
