#  Boston Housing Price Prediction — Linear Regression

A simple linear regression model that predicts median home values (`medv`) in the classic **Boston Housing dataset**, using three features: crime rate, average number of rooms, and percentage of lower-status population.

> ⚠️ **Heads up:** this is a first-pass / learning-exercise model. As shown below, it currently produces **negative predicted home prices** — a clear sign the data wasn't cleansed before training. See [Known Issues](#-known-issues--why-the-model-underperforms) and [Roadmap](#-roadmap--improvements) below.

---

##   Table of Contents
- [Dataset](#-dataset)
- [Requirements](#-requirements)
- [Usage](#-usage)
- [Pipeline](#-pipeline)
- [Results](#-results)
- [Known Issues / Why the Model Underperforms](#-known-issues--why-the-model-underperforms)
- [Roadmap / Improvements](#-roadmap--improvements)
- [License](#-license)

---

##  Dataset

Loaded from `Boston.csv`, containing 13 predictor variables + 1 target (`medv`). This project only uses:

| Column | Description |
|--------|-------------|
| `crim` | Per-capita urban crime rate |
| `rm` | Average number of rooms per dwelling |
| `lstat` | % of population classified as "lower status" |
| `medv` *(target)* | Median value of owner-occupied homes, in $1000s |

---


##  Results

**Learned coefficients:**

| Feature | Coefficient |
|---------|-------------|
| `crim` | -0.1211 |
| `rm` | +5.0854 |
| `lstat` | -0.6109 |
| **Intercept** | -1.1485 |

**Mean Squared Error:** `29.96`
**Root Mean Squared Error:** `≈ 5.47` → average error of **~$5,470** on predictions

---

##  Known Issues / Why the Model Underperforms

The notebook checks for **duplicates only** — no missing-value check, no outlier handling, no scaling. This shows up directly in the output:

### 1. Negative predicted prices
```
predictions = [... -6.30, ... -0.89, ...]
```
Two test predictions are **negative** — a home "worth" negative dollars is physically impossible. This is the clearest symptom of an unclean, unscaled dataset feeding an unconstrained linear model.

### 2. Unhandled outliers in `crim`
Crime rate is heavily right-skewed in this dataset (most towns near zero, a few 100x higher). Left untreated, these extreme values distort the regression line for every prediction, not just the outlier rows.

### 3. No feature scaling
- `crim`: ~0–90
- `rm`: ~3–9
- `lstat`: ~1–38

Wildly different ranges make outliers in high-range features disproportionately influential and make coefficients harder to interpret or sanity-check.

### 4. No missing-value check
`df.isnull().sum()` was never run — no evidence `NaN`s were ruled out before fitting.

### 5. Only 3 of 13 available features used
Dropping features like `nox`, `dis`, `tax`, `ptratio` (known to correlate with home value) without justification discards signal and can bias remaining coefficients.

### 6. Dataset ceiling effect
`medv` is capped at 50.0 in the original Boston dataset (censored, not true, values), which biases predictions near the top of the price range.

**Bottom line:** relative to a `medv` range of roughly $5k–$50k, an average error of ~$5,470 is large — especially damaging for lower-priced homes.

---


