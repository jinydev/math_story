---
layout: default
title: '수학이야기 68.미분4'
parent: 수학이야기
nav_order: 68
has_children: true
---

# 수학이야기 68.미분4 (Derivative 4: 로켓의 속도와 궤적 시뮬레이터)

미분 1~3부를 거치며 여러분은 미분 도함수 믹서기가 어떤 물리법칙을 가지고 있는지 원리를 깨달았습니다. 함수를 한 번 갈아버리면 "순간 속도(Velocity)" 판독기로 바뀌고, 두 번 갈아버리면 탑승자의 몸을 비트는 "가속도(Acceleration)" 중력 센서로 뒤바뀐다는 우주 최강의 해킹 트리를 말입니다.

자, 수능이나 카카오 코딩 테스트에서 출제되는 '미분(Derivative) 4부 활용' 단원은, 이 강력한 스피드 센서 마스터키를 들고 허공이 아닌 **"실제 현실 세계의 물리 엔진 투사체(발사체)"** 코딩에 적용해 보는 실전 훈련 파트입니다. 
당신이 로켓을 공중 100미터 상공으로 수직 쏘아 올렸을 때, 이 깡통 로켓이 언제 중력을 이기지 못하고 스피드가 0으로 꺼져 바닥으로 추락하는지, 땅바닥에 꼬라박히는 순간 충돌 타격 데미지 스피드는 얼마인지를 모두 수학 공식 3줄로 찢어발려 예측하는 시뮬레이션을 돌리게 됩니다.

마지막 장에서는 파이썬 `Matplotlib` 과 `SymPy` 모듈을 조합해, 로켓의 위치/속도/가속도 파동 애니메이션을 3단 분리 렌더링 그래프로 뽑아내는 키네마틱스(Kinematics) 코드로 미분 단원의 최종장을 영광스럽게 장식해 보겠습니다.

---

## 목차

- [00. 인트로: 우주 발사체 물리 엔진 트레이닝 (Intro)](00_intro.md)
- [01. 첫 번째 수업: 브레이크 밟는 순간, 1차원 직선 운동 (1D Motion)](01_1d_motion.md)
- [02. 두 번째 수업: 속도(Velocity) 와 속력(Speed) 의 절대값 해킹 로직](02_velocity_and_speed.md)
- [03. 세 번째 수업: 허공에 던진 수류탄의 나락 다이브, 투사체 운동 (Projectile Motion)](03_projectile_motion.md)
- [04. 네 번째 수업: 1초당 떨어지는 HP 배터리 게이지, 변화율 (Related Rates)](04_related_rates.md)
- [05. 다섯 번째 수업: 가성비 극한의 도면 치수 재기 설계 (Optimization Applications)](05_optimization_applications.md)
- [06. 여섯 번째 수업: 파이썬 Matplotlib 로켓 위치/속도 3단 그래프 시각화 (Python Matplotlib Kinematics)](06_python_matplotlib_kinematics.md)
