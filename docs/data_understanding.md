Document: Data Understanding Report
Academic Year: 2026
Course: IDS - Data Science
Prepared by: Lara Chbib / Malak Kataya
Instructor: Ali Mzahem
1. Introduction
The objective of this document is to provide a comprehensive understanding of the Olist E-commerce dataset structure. This phase is crucial for ensuring that the subsequent data transformation and analysis stages are built on a solid foundation of data logic and relational integrity.
2. Dataset Entity Analysis
We have analyzed and processed four primary entities within the dataset ecosystem:
• Customers Entity: Contains the demographic distribution and unique identifiers for each client.
• Orders Entity: Serves as the central transaction log, capturing purchase status and logistics timestamps.
• Order Items Entity: A granular-level table that links individual products to specific orders, including financial metrics such as price and freight.
• Products Entity: Stores metadata for all inventory items, including categorical classifications and physical dimensions.
3. Relational Schema & Integrity (Primary Keys)
To maintain the relational integrity of our database, we identified the following Primary Keys (PK) and relationships:
• Primary Keys:
• order_id uniquely identifies each record in the Orders table.
• customer_id serves as the unique identifier for the Customers table.
• product_id uniquely identifies individual items in the Products table.
• Data Relationships:
• A One-to-Many relationship exists between Customers and Orders (One customer can place multiple orders).
• Orders are linked to Products through the Order Items bridge table.
4. Empirical Findings (Data Quality Issues)
During the initial exploration, several data quality issues were identified that required intervention:
• Missing Values (Nulls): We detected 2,965 missing records in critical delivery timestamps and identified several products without assigned category names.
• Logical Inconsistencies: Some records lacked physical dimensions, which would impede shipping cost analysis.
5. Conclusion
Based on this understanding, we have implemented a Python-based transformation script (cleaning.py) to resolve these issues. The dataset is now validated and ready for high-level analytical modeling.
