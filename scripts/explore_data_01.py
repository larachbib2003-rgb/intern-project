import pandas as pd

# 1. Define the file path for the customers dataset
file_path = "data/raw/brazilian-ecommerce/olist_customers_dataset.csv"

# 2. Read the CSV file using pandas
df = pd.read_csv(file_path)

# 3. Display the first 5 rows of the data
print("--- First 5 rows of the Customers Dataset ---")
print(df.head())

# 4. Show the total number of customers
print(f"\nTotal number of customers: {len(df)}")

# 5. Show the list of columns
print("\nDataset Columns:")
print(df.columns.tolist())
# 6. Top 5 cities with the most customers
print("\nTop 5 Cities by Customer Count:")
print(df['customer_city'].value_counts().head(5))