---
layout: level_02
title: '수학이야기 55.인수분해2'
parent: 수학이야기
nav_order: 55
has_children: true
---

# 수학이야기 55.인수분해2 (Factorization 2: The Deep Hack)

인수분해 파트 1 (모듈 27) 에서 우리는 공통인수 뽑기와 합차공식 같은 기본적인 2차식 해제 코드를 배웠습니다. 
하지만 실제 물리 시뮬레이션이나 우주 궤도 예측 시스템에서 쏟아지는 방정식들은 고작 2차원(Area)에 머물지 않습니다. $3$차(부피), $4$차(초공간)로 꼬여버린, 인간의 암산 범위를 넘어선 거대한 괴수 방정식들이 도사리고 있습니다.

이번 **인수분해 2부** 에서는, 도저히 풀리지 않는 철벽같은 다항식을 부수는 특수 해체 장비들을 다룹니다.
복잡한 식을 치환 기법(은폐)으로 작게 접어버리기, $3$차원 큐브를 분해하는 곱셈공식, 그리고 그 어떤 다항식이든 조립 부품($x=a$) 하나만 때려 맞추면 연쇄적으로 붕괴하는 '인수정리와 조립제법(Synthetic Division)' 메커니즘까지, 프로 수준의 수학적 해킹 기술을 체득해 보겠습니다.

---

## 목차

- [00. 인트로: 복잡함과의 전쟁, 특수 해킹 장비들 (Intro)](./00_intro/)
- [01. 첫 번째 수업: 치환, 긴 변수를 하나로 숨기는 은폐술 (Substitution)](./01_substitution_method/)
- [02. 두 번째 수업: $3$차 방정식의 해체, 큐브를 분해하라 (Cubic Factorization)](./02_cubic_factorization/)
- [03. 세 번째 수업: 복이차식, $x^2$ 을 조종하는 이중 트릭 (Biquadratic Equations)](./03_biquadratic_equations/)
- [04. 네 번째 수업: 내림차순 정리, 혼돈 속의 뼈대 찾기 (Sorting by Degree)](./04_sorting_descending/)
- [05. 다섯 번째 수업: 궁극의 해머 조립제법과 인수정리 (Synthetic Division)](./05_synthetic_division/)
- [06. 여섯 번째 수업: 파이썬 루트(Roots) 추적기와 방정식의 붕괴 (Python SymPy Roots)](./06_python_sympy_roots/)
