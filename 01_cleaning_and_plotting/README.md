## 01_cleaning_and_plotting_pipeline
A basic Python project for teaching data cleaning and visualization. This project uses a real-world medical appointment dataset from Kaggle to demonstrate how to process raw CSV data and create clear static visualizations using seaborn and matplotlib.

**中文简介**：
- 本项目是一个教学型数据清洗与可视化示例，使用来自 Kaggle 的巴西的医院的医疗预约数据，展示如何利用 Python（pandas + seaborn + matplotlib）完成从原始数据处理到图表输出的完整流程。项目特别适合作为助教展示或初学者教学材料，支持 Google Colab 与本地运行。

## Overview

- **Goal:** Teach basic data cleaning and plotting using Python
- **Tools:** pandas, seaborn, matplotlib
- **Output:** Cleaned CSV and 4 static PNG charts
- **Audience:** Students or teaching assistants learning data pipelines

## 🧾 Dataset

- **Source:** Kaggle – [Medical Appointment No Shows](https://www.kaggle.com/datasets/joniarroba/noshowappointments)
- **Original File:** `Kaggle_dataset.csv` (not uploaded)
- **Cleaned Version:** `appointments_cleaned.csv`

The dataset contains medical appointment records, including demographic information and whether the patient showed up.

## Data Visualization

Below are the final visualizations generated from the cleaned CSV:

| Chart Title                         | Filename                    | Description                                |
|------------------------------------|-----------------------------|--------------------------------------------|
| No-Show Rate by Gender             | `no_show_by_gender.png`     | Comparison of no-show rate by gender       |
| No-Show Rate by Age Group          | `no_show_by_age_group.png`  | Age-based grouping of no-show behavior     |
| No-Show Rate by Day of Week        | `no_show_by_dayofweek.png`  | Trends across weekdays                     |
| No-Show Rate by SMS Notification   | `no_show_by_sms.png`        | Impact of SMS reminder on no-shows         |

All charts are generated using `seaborn` and saved via `matplotlib.pyplot.savefig()`.

## Data Architecture

![Pipeline Diagram](cleaning_and_plotting_pipeline_architecture.png)

**Flow:**  
`Kaggle CSV` → `Python (pandas)` → `Cleaned CSV` → `seaborn/matplotlib visualizations`

## Prerequisites

- Python 3.x
- Install the required libraries:
- pip install pandas matplotlib seaborn
  
## How to Run This Project

# Step 1: Clean the raw dataset (if applicable)
python clean_data.py

# Step 2: Generate visualizations
python visualize.py
Cleaned file: appointments_cleaned.csv

Output images: 4 PNG files in the same folder

## Lessons Learned

- How to group and bin continuous variables using pd.cut()

- How to compute custom aggregation (e.g., no-show rate) in seaborn

- How to style and export professional-quality static charts using Python
