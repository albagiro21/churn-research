# Customer Churn Prediction – End-to-End Research Project

## 1. Project Overview

This project aims to predict customer churn in a telecom-like environment using tabular data.

The objective is to identify customers at risk of cancelling their subscription and evaluate different modeling approaches in a structured and reproducible research workflow.

Models explored:

- Logistic Regression
- Random Forest
- XGBoost

After systematic comparison, Logistic Regression was selected as the final champion model due to its strong performance, stability, and interpretability.

---

## 2. Business Objective

Customer churn directly impacts revenue and customer lifetime value.

The goal of this project is to:

- Predict the probability of churn for each customer.
- Optimize recall for churners while maintaining acceptable precision.
- Identify the key drivers of churn for business actionability.

---

## 3. Dataset

Dataset: Telco Customer Churn (public dataset)

- ~7,000 customers
- Demographics
- Contract information
- Billing data
- Service subscriptions

Target variable:

- `Churn` (Yes / No)

Class imbalance:

- ~26% churn
- ~74% non-churn

---

## 4. Project Structure

```text
churn-research/
│
├── data/
│   ├── raw/                    # Original dataset files (e.g. Telco churn CSV)
│   └── processed/              # Cleaned or transformed datasets (if needed)
│
├── notebooks/
│   ├── 01_eda.ipynb            # Exploratory Data Analysis
│   ├── 02_logistic_baseline.ipynb
│   │                           # Baseline Logistic Regression + improvements
│   └── 03_model_selection.ipynb
│                               # Model comparison (LR, RF, XGBoost) + SHAP
│
│
├── models/                     # Serialized trained pipelines
│
├── requirements.txt            # Project dependencies
│
└── README.md                   # Project documentation
```
---

## 5. Methodology

### 5.1 Data Preprocessing

- Conversion of `TotalCharges` to numeric
- Missing value handling
- One-hot encoding for categorical features
- Standard scaling for numerical features

All preprocessing steps are integrated into sklearn pipelines to prevent data leakage.

---

### 5.2 Experimental Setup

- Train / Validation / Test split
- No cross-validation for final evaluation
- Threshold tuning on validation set
- Final evaluation on test set only once

Evaluation metrics:

- ROC-AUC
- PR-AUC
- Recall (churn)
- Precision (churn)
- F1-score

---

## 6. Model Comparison

| Model | ROC-AUC | PR-AUC | Recall | Precision | F1 |
|--------|----------|----------|----------|------------|------|
| Logistic Regression | 0.847 | 0.660 | 0.717 | 0.570 | 0.635 |
| Random Forest | ~0.839 | 0.644 | 0.698 | 0.601 | 0.646 |
| XGBoost | 0.845 | 0.660 | 0.658 | 0.584 | 0.619 |

Observations:

- Logistic Regression achieved the highest ROC-AUC.
- It also achieved the highest recall for churn.
- Tree-based models provided marginal improvements but did not significantly outperform Logistic.

---

## 7. Interpretability

### Logistic Regression

- Contract type is the strongest driver.
- Low tenure strongly increases churn risk.
- High monthly charges increase churn probability.

### Random Forest

Feature importance confirmed similar patterns:

- Contract structure dominates.
- Tenure remains highly protective.
- Service add-ons impact churn.

### XGBoost (SHAP Analysis)

SHAP confirmed:

- Month-to-month contracts strongly increase churn.
- Short tenure significantly increases churn probability.
- Lack of security/support increases churn risk.
- High monthly charges increase churn likelihood.

The consistency across models indicates stable and robust predictive signals.

---

## 8. Final Model Selection

Logistic Regression was selected as the final model because:

- Highest ROC-AUC.
- Highest recall for churners.
- Strong interpretability.
- Simpler deployment and monitoring.
- Comparable performance to more complex models.

This makes it the most suitable candidate for production integration.

---

## 9. Next Steps

- Serialize full pipeline (preprocessing + model)
- Register model in MLflow
- Deploy via FastAPI
- Add monitoring & threshold recalibration strategy

---

## 10. Key Takeaways

- Churn is primarily driven by contract commitment and tenure.
- Pricing exposure and lack of additional services increase churn risk.
- Model selection must balance performance, complexity, and interpretability.
- Simpler models can outperform more complex ones when the signal is structurally strong.

---
