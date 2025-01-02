# Customer Segmentation with E-Commerce Data

This project uses **clustering techniques** to segment customers based on their purchasing behavior. It aims to group customers into clusters that share similar characteristics, enabling businesses to better understand their customers and tailor marketing strategies.

## Table of Contents
1. [Project Overview](#project-overview)
2. [Dataset](#dataset)
3. [Tools and Libraries](#tools-and-libraries)
4. [Steps Performed](#steps-performed)
5. [Results](#results)
6. [How to Use](#how-to-use)
7. [Conclusion](#conclusion)

---

## Project Overview
The main goal of this project is to segment customers using **K-Means clustering**. The segmentation is based on three features:
- **Number of Purchases**
- **Total Quantity Purchased**
- **Monetary Value**

This segmentation can help businesses identify high-value customers, frequent purchasers, and other key customer groups.

---

## Dataset
- The dataset used is the [UCI Online Retail Data](https://archive.ics.uci.edu/ml/datasets/online+retail) which contains transactions from a UK-based online retailer.

---

## Tools and Libraries
The following tools and libraries were used in this project:
- **Python**: Programming language.
- **Google Colab**: Development environment.
- **Libraries**:
  - `Pandas`: Data manipulation and preprocessing.
  - `Scikit-learn`: Clustering and scaling.
  - `Matplotlib` and `Seaborn`: Data visualization.

---

## Steps Performed
1. **Data Loading**:
   - Imported the dataset from an Excel file.
   
2. **Data Cleaning**:
   - Removed missing and invalid entries.
   - Filtered only relevant transactions.

3. **Feature Engineering**:
   - Aggregated customer data into three key metrics:
     - Number of Purchases
     - Total Quantity Purchased
     - Monetary Value

4. **Data Scaling**:
   - Scaled the features using `StandardScaler` to normalize the data.

5. **K-Means Clustering**:
   - Used the Elbow Method to determine the optimal number of clusters.
   - Applied K-Means clustering to group customers.

6. **Cluster Analysis**:
   - Visualized the clusters using scatter plots.
   - Summarized cluster characteristics.

---

## Results
The customers were segmented into four clusters:
1. **Cluster 0**: Low spenders and infrequent purchasers.
2. **Cluster 1**: High spenders with large quantities purchased.
3. **Cluster 2**: Moderate spenders with medium purchasing frequency.
4. **Cluster 3**: Frequent purchasers but lower spending.

---
Conclusion
This project demonstrates how clustering techniques like K-Means can be used to analyze customer behavior and create meaningful customer segments. These insights can help businesses in targeted marketing, improving customer retention, and increasing revenue.

Author
This project was created by zhekayur.
