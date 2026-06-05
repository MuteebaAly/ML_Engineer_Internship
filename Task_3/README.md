# Task 3 — Heart Disease Prediction

## Overview

In this task I built a machine learning model to predict whether a patient is at risk of heart disease based on their clinical health data. The goal was to go through the full ML pipeline — from cleaning messy medical data to training, evaluating, and interpreting two classification models.

---

## Dataset

**Heart Disease UCI Dataset** — contains health records of 920 patients from 4 different locations (Cleveland, Hungary, Switzerland, VA Long Beach).

Each patient has 13 clinical features:

| Feature | Description |
|---------|-------------|
| `age` | Age of the patient |
| `sex` | Gender |
| `cp` | Chest pain type |
| `trestbps` | Resting blood pressure |
| `chol` | Serum cholesterol |
| `fbs` | Fasting blood sugar |
| `restecg` | Resting ECG results |
| `thalch` | Maximum heart rate achieved |
| `exang` | Exercise-induced angina |
| `oldpeak` | ST depression induced by exercise |
| `slope` | Slope of peak exercise ST segment |
| `ca` | Number of major vessels colored by fluoroscopy |
| `thal` | Thalassemia type |

Target variable `num` → converted to binary: **0 = Healthy, 1 = At Risk**

---

## What I Did

**Data Cleaning**
- Dropped irrelevant columns (`id`, `dataset`)
- Handled missing values carefully based on column type:
  - Numerical columns (`chol`, `trestbps`, `thalch`, `oldpeak`) → filled with **Median** because outliers were present
  - Categorical columns (`fbs`, `restecg`, `exang`) → filled with **Mode** (most frequent value)
  - `ca` column → assigned **-1** as a new category because 60% of its data was missing
- Applied One-Hot Encoding on categorical columns
- Converted multi-class target (0,1,2,3,4) to binary (0 or 1)

**Exploratory Data Analysis**
- Checked null values, data types, and statistical summary
- Detected outliers using IQR method for all numerical columns
- Checked correlations between key features using a heatmap
- Analyzed demographic trends — heart disease ratio by gender and average age by class

**Model Training & Evaluation**
- Split data: 80% training, 20% testing
- Applied StandardScaler for feature scaling
- Trained two models: Logistic Regression and Decision Tree
- Evaluated using Accuracy, Confusion Matrix, and ROC-AUC Score

---

## Results

| Model | Accuracy |
|-------|----------|
| Logistic Regression | 79.89% |
| Decision Tree | 76.09% |

> Logistic Regression performed better on this dataset so detailed evaluation was done on it.

---

### Confusion Matrix — Logistic Regression

|  | Predicted: Healthy | Predicted: Risk |
|--|-------------------|-----------------|
| **Actual: Healthy** | 60 ✅ | 15 ❌ |
| **Actual: Risk** | 22 ❌ | 87 ✅ |

- **60** healthy patients correctly identified
- **87** at-risk patients correctly identified
- **15** healthy patients wrongly flagged as risk (False Alarm)
- **22** at-risk patients missed by the model — this is the most critical error in a medical context

---

### ROC-AUC Score — Logistic Regression

**AUC = 0.89**

An AUC of 0.89 means the model has a strong ability to distinguish between healthy and at-risk patients. A perfect model scores 1.0 and random guessing scores 0.5 — so 0.89 is a very good result for medical data.

---

## Key Findings

- **Male patients** have a significantly higher risk of heart disease compared to females in this dataset
- **High `oldpeak`** (ST depression) is a strong indicator of heart disease risk
- Patients with **atypical chest pain** (`cp_atypical angina`) are mostly healthy and less likely to have heart disease
- The Logistic Regression model outperformed Decision Tree, suggesting the data has a relatively linear decision boundary

---

## Files

| File | Description |
|------|-------------|
| `Heart_Diseases_prediction.ipynb` | Main Jupyter Notebook with full code and outputs |

---

## Libraries Used

```
pandas | scikit-learn | matplotlib | seaborn
```


