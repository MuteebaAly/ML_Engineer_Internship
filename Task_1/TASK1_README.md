# Task 1 — Explore & Visualize Dataset

## Overview

In this task I explored and visualized the **Iris Dataset** — one of the most well known datasets in machine learning. The goal was to understand the data before building any model on top of it, because good data understanding is the foundation of any good ML project.

---

## Dataset

**Iris Dataset** — contains measurements of 150 flowers from 3 different species:
- Setosa
- Versicolor
- Virginica

Each flower has 4 features: sepal length, sepal width, petal length, and petal width — all measured in centimeters.

---

## What I Did

**Data Exploration**
- Loaded the dataset using Seaborn
- Checked the shape, column names, and data types
- Looked at the first few rows to understand the structure
- Used `describe()` to get a statistical summary of all features

**Visualizations**
- Scatter plots to see the relationship between petal length vs petal width, and sepal length vs sepal width — colored by species so you can clearly see how the species separate
- Histograms to understand how flowers are distributed across different measurement ranges — both overall and per species
- Box plots to detect outliers in each feature — found outliers mainly in the sepal width column

---

## Key Findings

- Setosa is very clearly separated from the other two species when looking at petal measurements
- Versicolor and Virginica overlap a bit which makes them harder to distinguish
- Outliers were detected in sepal width for Setosa and Virginica

---

## Note on the Notebook

I tried multiple approaches to get the `.ipynb` file to render on GitHub — clearing outputs, reducing file size — but GitHub kept showing "An error occurred" because of a known bug in its notebook renderer. So I converted the notebook to a `.py` script which works perfectly on GitHub, and I am sharing the Colab link for anyone who wants to see the full outputs and graphs.

---

## Files

| File | Description |
|---|---|
| `Explore_Visualize_Dataset.py` | Python script — view directly on GitHub |
| `Explore_Visualize_Dataset.ipynb` | Original Jupyter Notebook |

---

## Links

🐍 [View Python Script](Explore_Visualize_Dataset.py)
📊 [View Full Notebook with Outputs on Google Colab](https://colab.research.google.com/drive/13iP2PNFTPVG-4lpiIRBmVt6CoEFS3nz3#scrollTo=5441d661)
