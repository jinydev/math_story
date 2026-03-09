---
layout: level_06
title: '수학이야기 46.확률2'
parent: 수학이야기
nav_order: 46
has_children: true
---

# 수학이야기 46.확률2 (Probability 2: Monte Carlo & Combinatorics)

확률 1부(모듈 25) 에서는 주사위 1개, 동전 2개처럼 "우리가 직접 머릿속으로 모든 평행우주 가지(Tree) 를 그릴 수 있는" 아주 원시적인 게임들을 다루었습니다.
하지만 카지노에 진격해서 **"트럼프 카드 52장 중에서 5장을 연달아 뽑아 플러쉬 조합을 띄울 확률"** 을 묻는다면? 머릿속으로 나무를 그리다간 뇌가 타버릴 것입니다. 가지 수가 수백만, 수천만 갈래로 찢어지기 때문입니다!

이번 **확률(Probability) 파트 2** 에서는 이렇게 폭발하는 노드 트리(가지 수) 를 손대지 않고 통째로 복사해서 접어버리는 두 가지 거대한 해킹 알고리즘, **순열(Permutation)** 과 **조합(Combination)** 이라는 곱셈 공장의 파이프라인 구조를 분해합니다.
그리고 이 미쳐버린 수학 공식조차 계산하기 힘들 만큼 복잡한 우주적 혼돈 모델을 마주했을 때, 현대 컴퓨터만이 쓸 수 있는 최후의 무식한 시뮬레이션 폭격, **'몬테카를로 방법(Monte Carlo Simulation)'** 파이썬 코드를 내 모니터 스크린에 터뜨려 보겠습니다!

---

## 목차

- [00. 인트로: 폭발하는 우주의 가지치기 (Intro)](00_intro)
- [01. 첫 번째 수업: 순서가 지배하는 권력, 순열 (Permutation)](01_permutation)
- [02. 두 번째 수업: 줄 세우기, 그리고 팩토리얼 (Factorial !)](02_factorial_logic)
- [03. 세 번째 수업: 순서를 붕괴시키는 평등의 바구니, 조합 (Combination)](03_combination)
- [04. 네 번째 수업: "대표 2명 뽑기" 가 조합이 되는 이유 (Why Combinations Work)](04_representative_combination)
- [05. 다섯 번째 수업: 연속 확률의 곱셈과 연속 뽑기의 함정 (Consecutive Draws)](05_consecutive_probability)
- [06. 여섯 번째 수업: 파이썬 몬테카를로! 원주율 $\pi$ 를 총 쏴서 맞추기 (Python Monte Carlo PI)](06_python_monte_carlo)
