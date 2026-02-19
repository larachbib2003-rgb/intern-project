# Week 1: Data Quality Report
Student Name: Lara chbib / malak kataya
Instructor: Ali Mzahem ,Suha Mneimneh

 1. Overview
In this first week, I focused on auditing the Olist E-commerce dataset. My main goal was to identify quality issues—specifically missing values and data inconsistencies—to ensure that our analytics pipeline starts with clean, reliable data.

 2. Methodology & Findings
During the exploration phase, I performed the following checks:

 A. Null Value Detection
* Orders Dataset: I found missing timestamps in columns like `order_approved_at` and `order_delivered_customer_date`.
* Products Dataset: I noticed some products had missing dimensions (length, height, weight) and category names.
* Order Items: Checked for missing price or freight values to ensure revenue calculations stay accurate.

 B. Cleaning Strategy (Data Transformation)
* To handle these issues, I implemented the `dropna()` method in my Python script. 
* By removing rows with critical missing data, I ensured that all 4 datasets are now "Validated" and "Cleaned."

 C. Duplicate & Primary Key Validation
* I verified that each table has a unique identifier (Primary Key):
    - `order_id` for Orders.
    - `customer_id` for Customers.
    - `product_id` for Products.

 3. Results (Final Output)
The cleaning script successfully processed the raw files and generated the following outputs in the `data/processed/` folder:
1. `cleaned_orders.csv`
2. `cleaned_customers.csv`
3. `cleaned_products.csv`
4. `cleaned_order_items.csv`

 4. Conclusion
The data is now "Validated." By removing incomplete records, the dataset is ready for the next phase: Revenue Enrichment and Analysis.