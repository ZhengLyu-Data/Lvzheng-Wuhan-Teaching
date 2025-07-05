## Overview 项目总览

This is a lightweight teaching project focused on dashboard design and KPI visualization using Tableau. Using a cleaned hotel booking dataset, the project demonstrates how to design clear, well-structured visualizations that communicate key business metrics effectively.

** 中文说明 **  这是一个专注于 Tableau KPI 仪表板设计的教学项目，使用酒店预订数据构建结构清晰的可视化图表，用于教学演示如何通过图表讲述数据故事。

## Project Summary 项目摘要

** Goal | 目标 **  Teach how to design Tableau dashboards with key performance indicators (KPIs) using real-world data.  
使用真实数据讲解 KPI 可视化和仪表板布局的基本设计原则。  

** Tools | 工具 **  pandas, Tableau  
使用 pandas 进行数据预处理，Tableau 进行图表构建与布局设计  

** Output | 输出 **  A Tableau dashboard with 3 charts: KPI comparison, booking trends, and geographic distribution  
一个包含 3 个图表的 Tableau 仪表板：KPI 对比、预订趋势、客户分布地图  

** Audience | 受众 **  Students or job candidates learning dashboard design for data storytelling  
适合需要掌握可视化呈现与数据讲述能力的学生、助教或求职者

## Dataset 数据集说明

** Source | 来源 **  [Kaggle – Hotel Booking Demand Dataset](https://www.kaggle.com/datasets/jessemostipak/hotel-booking-demand)

** Original File | 原始文件 **  
`hotel_booking_raw.csv`

** Cleaned Version | 清洗后文件 **  
`hotel_booking_cleaned.csv`

The dataset contains hotel booking records including booking status, country, arrival date, and customer details.

** 中文说明 **  数据集包含酒店预订记录信息，包括是否取消、客户国籍、到达日期与客户属性，用于构建多角度 KPI 可视化。

## Tableau Dashboard 仪表板结构

The dashboard is named: **hotel_booking_dashboard**

It includes the following three visualizations:

| Chart | Title                        | Description | 中文说明 |
|-------|------------------------------|-------------|----------|
| 1     | Hotel Cancellation Rate      | A bar chart comparing cancellation rates between hotel types | 不同类型酒店的取消率对比柱状图 |
| 2     | Monthly Booking Trend        | A line chart showing the number of bookings per month | 每月预订趋势折线图 |
| 3     | Booking Distribution by Country | A map showing number of bookings per customer country | 按国家显示客户预订分布的地图图表 |

All charts are part of a single Tableau dashboard with aligned layout, colors, and KPI emphasis.

** 中文说明 **  
所有图表整合为一个 Tableau 仪表板，通过统一布局与配色，聚焦关键指标的表达，展示数据驱动的分析思维。

## Data Architecture 数据流程图

Raw CSV → pandas cleaning → Tableau visualization → KPI storytelling dashboard

原始数据 → Python 清洗 → Tableau 制图 → KPI 图表讲解式仪表板

---

## Prerequisites 环境依赖

** Tools **  
- Tableau Public (or Tableau Desktop)  
- Python 3.x + pandas (for optional cleaning)  

** 中文说明 **  本项目可直接在 Tableau 中完成可视化，但推荐配合 Python 使用 pandas 进行基础数据清洗，以提升仪表板的可用性与一致性。



## How to Run This Project 如何运行本项目

1. Upload `hotel_booking_cleaned.csv` into Tableau  
   将清洗后的 CSV 数据导入 Tableau

2. Open Tableau and create a new dashboard  
   在 Tableau 中新建仪表板并添加 3 个图表：

   - Chart 1: Drag `hotel` to Columns, `is_canceled` (as percent) to Rows  
   - Chart 2: Use `arrival_date_month` and `hotel` to create a line chart  
   - Chart 3: Use `country` on a filled map with booking count as size  

3. Organize all charts into a dashboard named **hotel_booking_dashboard**  

** 中文说明 **  将三个图表整合到仪表板中，统一命名为 `hotel_booking_dashboard`，可用于教学演示或面试展示。

## Lessons Learned 教学亮点

- How to transform raw data into meaningful KPI charts  
  **中文说明：** 如何将原始数据转化为结构化 KPI 图表

- How to design clean and effective Tableau dashboards  
  **中文说明：** 如何构建清晰易懂的 Tableau 仪表板

- How to communicate business insight visually  
  **中文说明：** 如何通过图表表达业务洞察与对比信息
