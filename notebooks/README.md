# Notebooks Directory

This directory contains Jupyter notebooks for exploratory data analysis and cross-country comparison.

## Notebooks

### Country-Specific EDA
- `benin_eda.ipynb` - Exploratory data analysis for Benin
- `sierra_leone_eda.ipynb` - Exploratory data analysis for Sierra Leone
- `togo_eda.ipynb` - Exploratory data analysis for Togo

### Cross-Country Analysis
- `compare_countries.ipynb` - Comparative analysis across all three countries

## Usage

1. Ensure you have Jupyter installed:
   ```bash
   pip install jupyter ipykernel
   ```

2. Install the kernel:
   ```bash
   python -m ipykernel install --user --name=solar-challenge
   ```

3. Open notebooks:
   ```bash
   jupyter notebook
   ```

## Analysis Structure

Each country EDA notebook includes:
1. Data Loading and Initial Inspection
2. Summary Statistics & Missing Value Report
3. Outlier Detection & Cleaning
4. Time Series Analysis
5. Cleaning Impact Analysis
6. Correlation & Relationship Analysis
7. Wind & Distribution Analysis
8. Temperature Analysis
9. Bubble Charts
10. Data Export

The comparison notebook includes:
1. Data Loading
2. Metric Comparison (Boxplots)
3. Summary Statistics Table
4. Statistical Testing (ANOVA/Kruskal-Wallis)
5. Key Observations
6. Visual Summaries

