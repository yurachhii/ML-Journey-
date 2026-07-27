# Lesson 4 – Gradient Descent

##  Table of Contents
- [1. Introduction to Gradient Descent](#1-introduction-to-gradient-descent)
- [2. Intuition & Mechanism](#2-intuition--mechanism)
- [3. Mathematical Implementation](#3-mathematical-implementation)
- [4. Correct Implementation: Simultaneous Updates](#4-correct-implementation-simultaneous-updates)
- [5. Derivative & Learning Rate Behavior](#5-derivative--learning-rate-behavior)
- [6. Behavior Near Local Minimum](#6-behavior-near-local-minimum)
- [7. Gradient Descent for Linear Regression](#7-gradient-descent-for-linear-regression)

---

## 1. Introduction to Gradient Descent

- **Broad Applicability:** Gradient descent is used all over Machine Learning, not just in Linear Regression.
- **General Minimization Algorithm:** It is an algorithm used to minimize *any* function, not exclusively a cost function in linear regression.
- **General Functions & Parameters:** Applies to general functions, including other cost functions that work with models having more than two parameters.

### Core Steps of Gradient Descent

1. Start with initial guesses for parameters `w` and `b`.
2. Keep changing `w` and `b` to reduce `J(w, b)`.
3. Continue until settling at or near a minimum.

> **Note:** A general cost function `J(w, b)` may have more than one local minimum. However, for Linear Regression, the cost function forms a **convex** shape (bowl or hammock shape) with a single **global minimum**.

---

## 2. Intuition & Mechanism

Imagine standing at a point on a hill: Gradient descent spins around 360° and asks:

> *"What direction should I step to go downhill as quickly as possible?"*

By taking that "baby step" downhill and repeating the process iteratively, you continue until reaching the local minimum (min).

---

## 3. Mathematical Implementation

The parameter update equations are defined as:

```
w := w - α · d/dw J(w, b)
b := b - α · d/db J(w, b)
```

**Meaning:** Update the current values of `w` and `b` by adjusting them by a small amount based on the derivative expression.

### Learning Rate (α)

- A positive number typically between 0 and 1.
- Controls the step size taken downhill.
  - If `α` is **large** → takes large steps downhill.
  - If `α` is **small** → takes baby steps downhill.

### Key Terms

- **Derivative Term:** Tells you which direction to take your step (the direction of steepest descent).
- **Convergence:** You repeat updates until reaching convergence — a point where parameters `w` and `b` no longer change significantly (a local minimum).

---

## 4. Correct Implementation: Simultaneous Updates

It is **critical** to update `w` and `b` **simultaneously**.

### Simultaneous Update Algorithm

```
temp_w = w - α · d/dw J(w, b)
temp_b = b - α · d/db J(w, b)
w = temp_w
b = temp_b
```

**Why?** If you update `w` first without using a temporary variable, the new value of `w` would feed into the derivative term for `b`, leading to incorrect calculations.

---

## 5. Derivative & Learning Rate Behavior

### Derivative Direction

The derivative represents the tangent line touching the curve at a specific point.

- If slope `d/dw J(w) > 0`: `w` decreases → moves left towards minimum.
- If slope `d/dw J(w) < 0`: `w` increases → moves right towards minimum.

### Impact of Learning Rate (α)

- **Too Small:** Gradient descent will work, but it takes many small steps and will be extremely slow.
- **Too Large / Overshoot:** May overshoot the minimum, fail to converge, or even diverge.

```
(a) Too Small: Slow Convergence          (b) Too Large: Overshoots

        *                                        *       *
      *                                        *           *
    *                                        *               *
  *___________ (many small steps)          *_________________* (jumps past minimum)
```

*Visualizing the effect of learning rate size on optimization trajectory.*

---

## 6. Behavior Near Local Minimum

- If parameters reach a local minimum, the slope of the cost function becomes zero (`d/dw J(w) = 0`).
- This leaves `w` unchanged (`w := w - 0 = w`), staying at the minimum.
- **Automatic Step Size Reduction:** As you approach a local minimum, the derivative naturally becomes smaller, causing gradient descent to automatically take smaller steps *without* changing `α`.

---

## 7. Gradient Descent for Linear Regression

Applying the specific derivative of the Mean Squared Error cost function for linear regression:

```
d/dw J(w, b) = 1/m · Σᵢ₌₁ᵐ (f_(w,b)(x⁽ⁱ⁾) - y⁽ⁱ⁾) · x⁽ⁱ⁾
```

### Full Batch Gradient Descent Algorithm

```
Repeat until convergence {
    w := w - α · 1/m · Σᵢ₌₁ᵐ (f_(w,b)(x⁽ⁱ⁾) - y⁽ⁱ⁾) · x⁽ⁱ⁾
    b := b - α · 1/m · Σᵢ₌₁ᵐ (f_(w,b)(x⁽ⁱ⁾) - y⁽ⁱ⁾)
}
```

> Note: `w` and `b` are updated **simultaneously** on each iteration, as covered in [Section 4](#4-correct-implementation-simultaneous-updates).

---

