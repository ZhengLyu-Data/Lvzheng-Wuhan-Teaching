## Overview 项目总览

A basic Python project demonstrating the logic of user-based collaborative filtering. Using a subset of the famous MovieLens dataset, this project simulates how recommendation engines identify similar users and suggest new content.

** 中文说明 (项目简介) ** 本项目是一个基于用户协同过滤推荐算法的教学示例，使用 MovieLens 的评分数据演示如何通过 Python 和 scikit-learn 找到相似用户并生成推荐结果。项目适合推荐系统教学入门或助教展示使用。

## Project Summary 项目摘要

** Goal|目标 ** Teach basic recommender system logic using user-based collaborative filtering  
  演示用户协同过滤推荐算法的基本原理和实现流程  

** Tools|工具 ** pandas, scikit-learn  
  使用 Python 的数据处理与建模库实现推荐流程  

** Output|输出 ** Top-N recommended movie IDs and similarity metrics  
  输出最相似用户及推荐电影 ID 与评分  

** Audience|受众 **Students or teaching assistants learning recommender systems  
  面向推荐系统初学者或助教教学展示使用

## Dataset 数据集说明

** Source|来源 ** [Kaggle – MovieLens 100k Subset](https://www.kaggle.com/datasets/abhikjha/movielens-100k)  

** Original File|原始文件 ** `basic_recommender_ratings.csv`  

** Cleaned Version|清洗后文件 ** `cleaned_recommender_data.csv`  

The dataset contains user IDs, movie IDs, and corresponding ratings.  
** 中文说明 ** 数据集包含用户对电影的评分信息，适用于教学用户推荐算法。

## Data Architecture 数据流程图

![Pipeline Diagram](movie_recommender_demo_pipeline.png)  

CSV 原始数据 → Python 清洗 → 建立评分矩阵 → 用户相似度计算 → 推荐输出

## Prerequisites 环境依赖

Python 3.x
Please make sure your local or Colab environment is running Python 3.
  
** 中文说明 ** 请确保你的本地或 Google Colab 环境为 Python 3 版本。

Install the required libraries:  
pip install pandas scikit-learn

** 中文说明 ** 依次安装本项目所需的 Python 库：pandas（用于数据处理），scikit-learn（用于相似度计算与推荐算法实现）。

## How to Run This Project 如何运行本项目

- Upload the dataset and scripts into your Colab or local environment  
  * 上传原始数据与 Python 脚本至 Colab 或本地环境
- Run the cleaning script: python clean_data.py
  * 运行数据清洗脚本：python clean_data.py 该脚本将读取原始数据，创建二分类标签，并生成清洗后的数据文件 wine_quality_cleaned.csv。
     ```bash
     python clean_data.py
     ```  
- This produces a cleaned version with pivot table
  * 该步骤将原始评分数据转化为透视表形式，为协同过滤推荐算法提供输入格式。
- Run the recommender engine: python recommder_demo.py
  * 运行推荐引擎脚本：python recommender_demo.py 该脚本将基于用户评分矩阵计算相似用户，并输出推荐的电影列表与相似度指标。
   ```bash
   python recommder_demo.py
   ```
- Outputs top 3 similar users and top 5 recommended movies
  * 输出与目标用户最相似的 3 位用户，以及推荐的前 5 部电影
- Final results are saved to `recommendation_output.txt` and downloaded
  * 最终推荐结果保存为 recommendation_output.txt 文件，并自动下载到本地
- This project can be executed both on Google Colab and local Jupyter Notebook.
  * 所有脚本支持在 Google Colab 中直接运行，同时也兼容本地 Jupyter Notebook 环境。只需确保 Python 3.x 与相关库已正确安装，即可在本地复现全部流程与输出结果。

## Lessons Learned 教学亮点

- How to construct a user-item matrix from raw ratings
  * 如何从原始评分构建用户-电影评分矩阵
- How to compute cosine similarity using scikit-learn  
  * 使用 scikit-learn 计算用户间余弦相似度的方法
- How to identify top similar users and generate movie recommendations 
  * 如何找到相似用户并根据其历史行为生成推荐内容
