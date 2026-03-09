import os

task_path = r"C:\Users\infoh\.gemini\antigravity\brain\924d21f9-c5ea-4107-9931-1d74d731a005\task.md"
plan_path = r"C:\Users\infoh\.gemini\antigravity\brain\924d21f9-c5ea-4107-9931-1d74d731a005\implementation_plan.md"

task_append = """
## Phase 21: Module 27 (인수분해1 - Factorization 1) [NEW BATCH: 7 Chapters]
- [ ] Create `index.md` spanning Chapters 00 to 06.
- [ ] Generate Webtoon image (Factoring factory) and SVG (Area puzzle).
- [ ] Integrate Python `sympy.factor()` usage.

## Phase 22: Module 55 (인수분해2 - Factorization 2) [NEW BATCH: 7 Chapters]
- [ ] Create `index.md` spanning Chapters 00 to 06.
- [ ] Generate Webtoon image (Polynomials) and SVG (Root finding).
- [ ] Integrate Python `sympy.roots()` usage.

## Phase 23: Module 45 (이차곡선1 - Conic Sections 1) [NEW BATCH: 7 Chapters]
- [ ] Create `index.md` spanning Chapters 00 to 06.
- [ ] Generate Webtoon image (Cone slicing) and SVG (Parabolas & Circles).
- [ ] Integrate Python ellipse/circle plotting equations.

## Phase 24: Module 56 (이차곡선2 - Conic Sections 2) [NEW BATCH: 7 Chapters]
- [ ] Create `index.md` spanning Chapters 00 to 06.
- [ ] Generate Webtoon image (Orbits) and SVG (Hyperbolas).
- [ ] Integrate Python conic focus calculations.

## Phase 25: Module 28 (원1 - Circle 1) [NEW BATCH: 7 Chapters]
- [ ] Create `index.md` spanning Chapters 00 to 06.
- [ ] Generate Webtoon image (Wheel creation) and SVG (Pi ratio).
- [ ] Integrate Python circle circumference/area loops.

## Phase 26: Module 72 (원2 - Circle 2) [NEW BATCH: 7 Chapters]
- [ ] Create `index.md` spanning Chapters 00 to 06.
- [ ] Generate Webtoon image (Geometry circles) and SVG (Secants & Tangents).
- [ ] Integrate Python angular distance algorithms.

## Phase 27: Module 25 (확률1 - Probability 1) [NEW BATCH: 7 Chapters]
- [ ] Create `index.md` spanning Chapters 00 to 06.
- [ ] Generate Webtoon image (Dice toss) and SVG (Coin tree).
- [ ] Integrate Python `random.randint` simulation.

## Phase 28: Module 46 (확률2 - Probability 2) [NEW BATCH: 7 Chapters]
- [ ] Create `index.md` spanning Chapters 00 to 06.
- [ ] Generate Webtoon image (Casino/Monte Carlo) and SVG (Combinations).
- [ ] Integrate Python Monte Carlo simulation loops.

## Phase 29: Module 64 (벡터 - Vector) [NEW BATCH: 7 Chapters]
- [ ] Create `index.md` spanning Chapters 00 to 06.
- [ ] Generate Webtoon image (Arrow winds) and SVG (Vector addition).
- [ ] Integrate Python Vector arrays (`numpy` arrays).

## Phase 30: Module 65 (미분1 - Derivative 1) [NEW BATCH: 7 Chapters]
- [ ] Create `index.md` spanning Chapters 00 to 06.
- [ ] Generate Webtoon image (Car speedometer) and SVG (Tangents).
- [ ] Integrate Python `sympy.diff()` basics.

## Phase 31: Module 66 (미분2 - Derivative 2) [NEW BATCH: 7 Chapters]
- [ ] Create `index.md` spanning Chapters 00 to 06.
- [ ] Generate Webtoon image (Optimization/Peaks) and SVG (Local Max/Min).
- [ ] Integrate Python gradient descent basics.

## Phase 32: Module 67 (미분3 - Derivative 3) [NEW BATCH: 7 Chapters]
- [ ] Create `index.md` spanning Chapters 00 to 06.
- [ ] Generate Webtoon image (Rollercoaster curve) and SVG (Concavity/Inflection).
- [ ] Integrate Python second derivative checks.

## Phase 33: Module 68 (미분4 - Derivative 4) [NEW BATCH: 7 Chapters]
- [ ] Create `index.md` spanning Chapters 00 to 06.
- [ ] Generate Webtoon image (Rocket trajectory) and SVG (Motion graphs).
- [ ] Integrate Python kinematics simulating derivatives.

## Phase 34: Module 69 (행렬 - Matrix) [NEW BATCH: 7 Chapters]
- [ ] Create `index.md` spanning Chapters 00 to 06.
- [ ] Generate Webtoon image (Grid screens) and SVG (Transformation).
- [ ] Integrate Python `numpy` matrix multiplication.

## Phase 35: Module 70 (무한급수 - Infinite Series) [NEW BATCH: 7 Chapters]
- [ ] Create `index.md` spanning Chapters 00 to 06.
- [ ] Generate Webtoon image (Achilles/Tortoise) and SVG (Geometric limit).
- [ ] Integrate Python `while` convergence loops.

## Phase 36: Module 71 (수열의 극한 - Limits of Sequences) [NEW BATCH: 7 Chapters]
- [ ] Create `index.md` spanning Chapters 00 to 06.
- [ ] Generate Webtoon image (Zooming strictly) and SVG (Limit epsilon barrier).
- [ ] Integrate Python `sympy.limit()`.

## Phase 37: Verification (Final Batch 4)
- [ ] Validate Jekyll rendering and LaTeX math formatting.
- [ ] Update walkthrough and notify user.
"""

plan_append = """
---

# NEW BATCH: Final Advanced Math Compilation (Modules 27, 55, 45, 56, 28, 72, 25, 46, 64, 65, 66, 67, 68, 69, 70, 71)

This batch finishes out the massive V3 rewrite, completing Algebra, Conics, Circles, Probability, Vectors, Calculus, Matrices, and Series.

### 18. Module 27: 인수분해1 (Factorization 1) [7 Chapters]
- Breakdown of polynomials. Common factors. Python `sympy.factor()`.

### 19. Module 55: 인수분해2 (Factorization 2) [7 Chapters]
- Advanced factoring (Quadratics, Cubics). Extracting roots. 

### 20. Module 45: 이차곡선1 (Conic Sections 1) [7 Chapters]
- Parabolas and Circles. Slicing cones. Distance definitions.

### 21. Module 56: 이차곡선2 (Conic Sections 2) [7 Chapters]
- Ellipses and Hyperbolas. Planetary orbits and Python plots.

### 22. Module 28: 원1 (Circle 1) [7 Chapters]
- Geometry of a circle. Radius, diameter, circumference ($\pi$). 

### 23. Module 72: 원2 (Circle 2) [7 Chapters]
- Angles, chords, tangents. The theorems of Thales and inscribed angles.

### 24. Module 25: 확률1 (Probability 1) [7 Chapters]
- Cases, basic probability `P(A)`. Python `random` simulation.

### 25. Module 46: 확률2 (Probability 2) [7 Chapters]
- Combinations, Permutations, Monte Carlo methods.

### 26. Module 64: 벡터 (Vector) [7 Chapters]
- Magnitude and direction. Dot/cross product logic. Numpy arrays.

### 27. Module 65: 미분1 (Derivative 1) [7 Chapters]
- Rates of change, limit definition. `sympy.diff()`.

### 28. Module 66: 미분2 (Derivative 2) [7 Chapters]
- Curve sketching, optimization, local max/min.

### 29. Module 67: 미분3 (Derivative 3) [7 Chapters]
- Second derivatives, concavity, inflection points.

### 30. Module 68: 미분4 (Derivative 4) [7 Chapters]
- Physics applications (Position, Velocity, Acceleration). 

### 31. Module 69: 행렬 (Matrix) [7 Chapters]
- Linear transformations, operations. Numpy matrix math.

### 32. Module 70: 무한급수 (Infinite Series) [7 Chapters]
- Zeno's paradox, Geometric series convergence. 

### 33. Module 71: 수열의 극한 (Limits of Sequences) [7 Chapters]
- Defining sequences, converging to a limit, approaching infinity.

## Verification Plan (Final Batch 4)
- Run `jekyll build` periodically to verify formatting.
- Check Python executions and SVG validities.
"""

with open(task_path, 'a', encoding='utf-8') as f:
    f.write(task_append)

with open(plan_path, 'a', encoding='utf-8') as f:
    f.write(plan_append)
print("Files appended successfully")
