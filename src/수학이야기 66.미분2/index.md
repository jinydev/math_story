---
layout: default
title: "수학이야기 66.미분2"
parent: 수학이야기
nav_order: 66
has_children: true
---

# 수학이야기 66.미분2 (Derivative 2: 게임의 지형도와 최강의 무기 셋업)

미분 1부(모듈 65) 에서는 컴퓨터 코드로 곡선의 단 1픽셀 "찰나의 스피드(접선의 기울기 $\mathbf{f'(x)}$)" 만을 찾아내는 해킹 스킬을 배웠습니다. 
자, 속도를 구했으면 이걸로 뭘 할까요? 단순한 과속 카메라 단속용일까요? 

아닙니다. 미분이 인류 최고 발명품 중 하나로 불리는 이유는, 바로 우리가 미개척 맵(미지의 함수 지도) 에 떨어졌을 때 이 "스피드 데이터 $f'(x)$" 하나만을 단서로 해서, 우주 전체 지도의 산봉우리가 어디 있고(Local Maximum), 깊은 함정 골짜기가 어디 있는지(Local Minimum) 를 컴컴한 어둠 속에서도 $100\%$ 완벽하게 스캔하고 3D 기하학으로 렌더링해 낼 수 있는 '만능 지형 탐지기 레이더' 기 때문입니다.

이번 **미분(Derivative) 2부** 단원에서는 도함수 자판기가 알려주는 "기울기 부호($+, -$)" 를 이용해 산맥의 오르막길과 내리막길을 구별하고, 곡선 롤러코스터가 정점에 다다라 엔진의 굉음이 $0$이 되는 순간인 극대/극소 스파크를 찾는 퀘스트를 수수께끼처럼 풀어봅니다. 마지막엔 이 미분 지형 스캐너를 파이썬 SciPy 모듈의 '최적화(Optimization)' 인공지능 탐지기로 가동해 보겠습니다.

---

## 목차

- [00. 인트로: 보이지 않는 우주 지형의 뼈대를 캐내다 (Intro)](00_intro.md)
- [01. 첫 번째 수업: 도함수 자판기의 $+ / -$ 스위치, 증가와 감소 (Increasing & Decreasing)](01_increasing_decreasing.md)
- [02. 두 번째 수업: 엔진 가속도가 멈추는 $0$ 의 찰나, 극댓값과 극솟값 (Local Extrema)](02_local_extrema.md)
- [03. 세 번째 수업: 우주 끝까지! 최대 랭킹과 최소 랭킹 방어 (Global Max & Min)](03_max_min_values.md)
- [04. 네 번째 수업: 나만의 미지의 외계 산맥 지도 렌더링하기 (Graph Drawing)](04_graph_drawing.md)
- [05. 다섯 번째 수업: 가성비 극한의 아이템 셋업! 최적화 문제 퀘스트 (Optimization Problems)](05_optimization_problems.md)
- [06. 여섯 번째 수업: 파이썬 SciPy AI로 굴곡의 정점 산책하기 (Python Optimize)](06_python_scipy_optimize.md)
