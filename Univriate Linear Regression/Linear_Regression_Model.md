# Lesson 3 – Linear Regression Model

##  Table of Contents
- [1. Introduction & Terminology](#1-introduction--terminology)
- [2. Model Representation](#2-model-representation)
- [3. Cost Function](#3-cost-function)
- [4. Cost Function Examples & Outlier Sensitivity](#4-cost-function-examples--outlier-sensitivity)
- [5. Mathematical Derivation of Parameters (Closed-Form Solution)](#5-mathematical-derivation-of-parameters-closed-form-solution)
- [6. Scikit-Learn Implementation & Practical Notes](#6-scikit-learn-implementation--practical-notes)

---

## 1. Introduction & Terminology

**Goal:** Predict the price of a house based on its size.

- Build a fitted straight line across the data points.
- Pick a specific size value on the x-axis to predict its corresponding house price.

### Key Concepts

- **Supervised Learning:** The training data includes the "right answers" (labeled outputs).
- **Regression Model:** Predicts a numerical/continuous value (infinitely many possible outputs).

### Terminology & Notation

| Symbol | Meaning |
|--------|---------|
| `x` | Input variable / Feature (e.g., House sizes) |
| `y` | Output variable / Target / "Right answer" (e.g., Price) |
| `m` | Total number of training examples |
| `(x, y)` | A single training example |
| `(x⁽ⁱ⁾, y⁽ⁱ⁾)` | The *i*-th training example (`i` = position/index in the dataset, **not** exponentiation) |

### Model Flow

```
Training Set → Learning Algorithm → Produces Function f (Hypothesis / Model)
                                          │
                              Feature x ──┤
                                          └──> Prediction ŷ
```

---

## 2. Model Representation

How do we represent the function `f`? What mathematical formula do we use?

**Univariate Linear Regression Formula:**

```
f_(w,b)(x) = w·x + b   ≡   f(x) = w·x + b
```

Where `w` and `b` are the **parameters** of the model (weights/coefficients), and `x` is a single variable/feature.

---

## 3. Cost Function


**Definition:** The Cost Function measures model performance to evaluate how well it fits the data and guide improvements.

**Parameters (w, b):** Variables adjusted during training to optimize the model (also called coefficients/weights).

- Changing `w` and `b` yields a different straight line fit each time.

### Linear Function Plot Example

- For `w = 0, b = 1.5` → `f(x) = 1.5` (where `b` is the y-intercept).
- For `w = 0.5, b = 0` → slope = `0.5`.

**Goal:** Find `w` and `b` such that prediction `ŷ⁽ⁱ⁾` is close to target `y⁽ⁱ⁾` for all training examples `(x⁽ⁱ⁾, y⁽ⁱ⁾)`.

### Error Calculation & Formulation

**Single example error:**

```
error = (ŷ⁽ⁱ⁾ − y⁽ⁱ⁾)²
```

**Summed over all training examples:**

```
Σᵢ₌₁ᵐ (ŷ⁽ⁱ⁾ − y⁽ⁱ⁾)²
```

Since `m` is large, summing raw errors yields very large numbers. Thus we compute the **average** squared error instead of the total, and multiply by `1/2` for differentiation convenience:

> **Cost Function Formula:**
>
> ```
> J(w, b) = 1/(2m) × Σᵢ₌₁ᵐ (ŷ⁽ⁱ⁾ − y⁽ⁱ⁾)²
> ```

---

## 4. Cost Function Examples & Outlier Sensitivity

**Why use Squared Error instead of Absolute Error (|y − ŷ|)?**

- **Differentiation:** Smooth, continuous derivatives facilitate calculus optimization.
- **Sensitivity to Outliers / Penalty Reason:** Penalizes larger errors much more heavily than small ones.

### Goal: Minimize J(w, b)

For simplicity, assume `b = 0`, simplifying the model to `f(x) = w·x`.

| Case | Parameter Choice | Dataset Points (x, y) | Calculations | Cost J(w) |
|------|------------------|------------------------|---------------|-----------|
| Case 1 | `w = 1` | (1,1), (2,2), (3,3) | `ŷ = x` → errors are all 0 | `J(1) = 0` |
| Case 2 | `w = 0.5` | (1,1), (2,2), (3,3) | `m = 3`; `ŷ₁=0.5, ŷ₂=1, ŷ₃=1.5`; `J(0.5) = (1/6)[(0.5−1)² + (1−2)² + (1.5−3)²] = (1/6)[0.25+1+2.25] = 3.5/6` | `J(0.5) ≈ 0.58` |
| Case 3 | `w = 0` | (1,1), (2,2), (3,3) | `ŷ = 0`; `J(0) = (1/6)[(0−1)² + (0−2)² + (0−3)²] = (1/6)[1+4+9] = 14/6 = 7/3` | `J(0) ≈ 2.33` |

**Cost Function Plot:** Plotting `J(w)` against `w` yields a **parabola (bowl shape)**, where each parameter choice corresponds to a different straight-line fit, and the minimum cost is reached at `w = 1`.

```
J(w)
 3 |                                   *
 2 |*                              *
 1 |    *                     *
   |         *  Min J(w)=0 at w=1  *
 0 |______________●________________________ w
       0.5    1      2      3      4
```

---

## 5. Mathematical Derivation of Parameters (Closed-Form Solution)

Our goal is to find the parameter values `b` and `w` that reach the global minimum of `J(w, b)` by setting partial derivatives to 0:

```
∂J/∂b = 0   and   ∂J/∂w = 0
```

### Derivation for Bias (b)

```
∂J/∂b = -(1/m) Σᵢ₌₁ᵐ ( y⁽ⁱ⁾ - (b + w·x⁽ⁱ⁾) ) = 0

(1/m) Σ y⁽ⁱ⁾ - b - (w/m) Σ x⁽ⁱ⁾ = 0

b + (w/m) Σ x⁽ⁱ⁾ = (1/m) Σ y⁽ⁱ⁾
```

**Equation 1:**

```
b = (1/m) [ Σ y⁽ⁱ⁾ − w Σ x⁽ⁱ⁾ ]
```

### Derivation for Weight (w)

```
∂J/∂w = -(1/m) Σ [ x⁽ⁱ⁾y⁽ⁱ⁾ - b·x⁽ⁱ⁾ - w·(x⁽ⁱ⁾)² ] = 0

Σ x⁽ⁱ⁾y⁽ⁱ⁾ - b Σ x⁽ⁱ⁾ - w Σ (x⁽ⁱ⁾)² = 0
```

Substitute `b` from Equation 1 into the equation above:

```
w Σ (x⁽ⁱ⁾)² + Σ x⁽ⁱ⁾ [ (1/m) Σ y⁽ⁱ⁾ - (w/m) Σ x⁽ⁱ⁾ ] = Σ x⁽ⁱ⁾y⁽ⁱ⁾

w [ Σ (x⁽ⁱ⁾)² - (1/m)(Σ x⁽ⁱ⁾)² ] = Σ x⁽ⁱ⁾y⁽ⁱ⁾ - (1/m) Σ x⁽ⁱ⁾ Σ y⁽ⁱ⁾
```

**Equation 2:**

```
w = [ m·Σ x⁽ⁱ⁾y⁽ⁱ⁾ − (Σ x⁽ⁱ⁾)(Σ y⁽ⁱ⁾) ] / [ m·Σ (x⁽ⁱ⁾)² − (Σ x⁽ⁱ⁾)² ]
```

---

## 6. Scikit-Learn Implementation & Practical Notes

### Class Syntax

```python
from sklearn.linear_model import LinearRegression

model = LinearRegression(
    fit_intercept=True,
    normalize=False,
    copy_X=True,
    n_jobs=1
)
```

### Parameter Details & Explanations

| Parameter | Description |
|-----------|--------------|
| `fit_intercept` | Determines whether to calculate the intercept (`b` / bias) of the model.<br>• `True` → calculates `b` in `y = w·x + b`.<br>• `False` → sets `b = 0` (forces line through the origin `(0,0)`). |
| `normalize` | Normalizes feature data before fitting. It's usually advisable to perform feature scaling/normalization on input data prior to model fitting. |
| `copy_X` | Whether to create a copy of the original input data or overwrite/modify the original dataset directly. |
| `n_jobs` | Number of CPU cores used for computational speedup.<br>• `1` → uses 1 CPU core.<br>• `-1` → uses all available CPU cores. |

### How to Train Your Model

```python
model.fit(X, y)
```

>  **Important Requirement:** Input data `X` must be structured as a **2D array**, even if training on a single feature.

```python
# Example: single feature reshaped to 2D
X = X.reshape(-1, 1)
model.fit(X, y)
```

---

