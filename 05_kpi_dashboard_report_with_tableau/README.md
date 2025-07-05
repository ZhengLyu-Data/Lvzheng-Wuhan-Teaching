## Overview 项目总览

A lightweight Tableau-based teaching project demonstrating how to design KPI dashboards using real hotel booking data. This project helps explain how to use visual analytics to convey operational trends, financial insights, and user behaviors.

** 中文说明 ** 本项目是一个基于 Tableau 的轻量级教学示例，使用酒店预订数据构建三个典型图表，演示如何通过可视化分析呈现业务趋势、用户行为与关键指标，适用于教学场景与面试展示。

## Project Summary 项目摘要

Goal | 目标
Teach dashboard reporting logic using Tableau with real-world booking data
** 中文说明 ** 通过真实酒店预订数据，讲解 KPI 指标设计与仪表板可视化结构

Tools | 工具
pandas (for cleaning), Tableau (for dashboard building)
** 中文说明 ** 使用 pandas 进行数据预处理，Tableau 构建仪表板

Output | 输出
Interactive Tableau dashboard with 3 charts
** 中文说明 ** 包含三个图表的交互式仪表板（hotel_booking_dashboard.pdf）

Audience | 受众
Students or job candidates learning dashboard design
** 中文说明 ** 适用于学习仪表板设计的学生、讲师或面试展示者


## Dataset 数据集说明

** Source | 来源 **  [Kaggle – Hotel Booking Demand Dataset](https://www.kaggle.com/datasets/jessemostipak/hotel-booking-demand)

** Original File | 原始文件 **  
`hotel_booking_raw.csv`

** Cleaned Version | 清洗后文件 **  
`hotel_booking_cleaned.csv`

The dataset contains hotel booking information from city and resort hotels, including reservation dates, lead time, customer types, cancellation status, and prices.

** 中文说明 ** 数据集包括城市与度假型酒店的预订记录，涵盖入住时间、提前预订天数、客户类型、取消状态与房价等关键变量。

## Tableau Dashboard 仪表板结构

The dashboard is named: **hotel_booking_dashboard**

It includes the following three visualizations:

** 中文说明 ** 这个Tableau仪表板包括三个图表

| Chart | Title                        | Description | 中文说明 |
|-------|------------------------------|-------------|----------|
| 1     | Average Daily Rate by Hotel Type| A bar chart comparing the average room price of City and Resort hotels | 比较城市与度假酒店的平均房价，用于教学财务类 KPI |
| 2     | Monthly Booking Volume by Status| A stacked bar chart showing the number of reservations by status each month | 展示每月预订数量及状态分布（入住、取消、未到） |
| 3     | Cancellation Rate by Lead Time Bucket| A bar chart showing how cancellation rates change by booking lead time | 展示不同提前预订时长下的取消率变化，适合讲解风险控制逻辑|

All charts are part of a single Tableau dashboard with aligned layout, colors, and KPI emphasis.

** 中文说明 **  所有图表整合为一个 Tableau 仪表板，通过统一布局与配色，聚焦关键指标的表达，展示数据驱动的分析思维。

## Data Architecture 数据流程图

![Data Architecture](supply_chain_data_pipeline_architecture.png)

Raw CSV → Data Cleaning (pandas) → Tableau Dashboard → 3 KPI Charts

** 中文说明 ** 原始数据 → Python 清洗 → Tableau 仪表板 → 三个关键指标图表

## Prerequisites 环境依赖

Python 3.x with pandas installed

** 中文说明 ** 请确保你的本地或者Google Colab 环境为 Python 3 版本及 pandas 库（用于清洗数据）

Tableau Public ** 中文说明 ** 可视化部分使用 Tableau Public 构建仪表板并导出 PDF

This project can be visualized directly in Tableau, but it is recommended to use Python with pandas for basic data cleaning to enhance dashboard usability and consistency.

** 中文说明 **  本项目可直接在 Tableau 中完成可视化，但推荐配合 Python 使用 pandas 进行基础数据清洗，以提升仪表板的可用性与一致性。

## How to Run This Project 如何运行本项目

1. Upload `hotel_booking_cleaned.csv` into Tableau
   
   ** 中文说明 ** 将清洗后的 CSV 数据导入 Tableau

3. Open Tableau and create a new dashboard
    
   ** 中文说明 ** 在 Tableau 中新建仪表板并添加 3 个图表：

   - Chart 1: Drag `hotel` to Columns, `is_canceled` (as percent) to Rows  
   - Chart 2: Use `arrival_date_month` and `hotel` to create a line chart  
   - Chart 3: Use `country` on a filled map with booking count as size

4. Organize all charts into a dashboard named **hotel_booking_dashboard**  

** 中文说明 ** 将三个图表整合到仪表板中，统一命名为 `hotel_booking_dashboard`，可用于教学演示或面试展示。

5.Export the dashboard as PDF

** 中文说明 ** 将仪表板导出为 PDF 文件，适合教学演示或求职材料展示

This project can be executed both on Google Colab and local Jupyter Notebook.

** 中文说明 ** 所有脚本支持在 Google Colab 中直接运行，同时也兼容本地 Jupyter Notebook 环境。只需确保 Python 3.x 与相关库已正确安装，即可在本地复现全部流程与输出结果。

## Lessons Learned 教学亮点

How to structure Tableau dashboards with KPI logic

** 中文说明 ** 如何基于 KPI 思维构建 Tableau 仪表板

How to analyze hotel behavior across time and customer segments

** 中文说明 ** 如何分析酒店预订行为的时间变化与人群差异

How to explain cancellation risk and financial indicators visually

** 中文说明 ** 如何通过图表解读取消风险与财务价格等关键指标
