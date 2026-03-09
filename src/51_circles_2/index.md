---
layout: level_04
title: '수학이야기 72.원2'
parent: 수학이야기
nav_order: 72
has_children: true
---

# 수학이야기 72.원2 (Circle 2: Collision and Angles)

원 파트 1 (모듈 28) 에서는, 원이 혼자 평화롭게 놓여 있을 때 그 뱃속에 들어있는 지름, 호, $\pi$ 의 비율과 다각형 렌더링 면적(Area) 을 다루었습니다.
하지만 실전 게임 프로그래밍이나 물리 엔진에서는 동그라미가 혼자 가만히 있는 경우는 없습니다. 우주선이 둥근 행성을 향해 곤두박질치거나(할선), 미사일이 행성의 대기권 테두리를 아슬아슬하게 스치며 튕겨 나가거나(접선), 또는 두 개의 행성이 서로 부딪히는 '충돌(Collision)' 이벤트가 끊임없이 일어납니다.

이번 **원(Circle) 파트 2** 에서는, 원의 평화로운 방어막을 뚫고 들어오는 무자비한 직선 레이저들의 기하학적 난타전을 다룹니다.
직선이 원을 어떻게 해킹하는지(할선과 접선), 그리고 원의 껍데기에 반사되어 튀는 레이저의 각도(원주각) 가 어떻게 우주의 어느 위치에서든 완벽하게 똑같은 숫자로 유지되는지, 그 소름 돋는 '원주각 불변의 법칙' 코드까지 뜯어보겠습니다.

---

## 목차

- [00. 인트로: 방어막을 뚫는 레이저 빔 (Intro)](./00_intro/)
- [01. 첫 번째 수업: 아슬아슬한 스침, 접선(Tangent) 의 정의 (Tangent)](./01_tangent_of_circle/)
- [02. 두 번째 수업: 무자비한 관통, 할선(Secant) 과 방멱의 정리 (Secant)](./02_secant_and_power/)
- [03. 세 번째 수업: 허공의 마법, 원주각(Inscribed Angle) 의 탄생 (Inscribed Angle)](./03_inscribed_angle/)
- [04. 네 번째 수업: 원주각과 중심각의 $1:2$ 비율 해킹 (Angle Ratio)](./04_angle_ratio_theorem/)
- [05. 다섯 번째 수업: 원주각의 그림자 복제 (Clone) 마법 (Cloned Angles)](./05_cloned_angles/)
- [06. 여섯 번째 수업: 파이썬 파이게임(PyGame) 식 충돌 감지 매커니즘 (Python Collision)](./06_python_collision_detection/)
