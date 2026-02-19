import pandas as pd

# 1. Load the dataset (Make sure to place your file path here later)
def load_data(file_path):
    df = pd.read_csv(file_path)
    return df

# 2. Clean the data (Targeting the 2,965 missing values)
def clean_orders(df):
    # Removing rows where delivery date is missing
    df_cleaned = df.dropna(subset=['order_delivered_customer_date'])
    print(f"Success! Data cleaned. Missing values removed.")
    return df_cleaned

# Note to mentor: This code is ready to process the CSV file once connected.
import pandas as pd

# 1. Function to load the dataset
def load_data(file_path):
    df = pd.read_csv(file_path)
    return df

# 2. Function to clean the orders data
def clean_orders(df):
    # Removing rows where the delivery date is missing
    df_cleaned = df.dropna(subset=['order_delivered_customer_date'])
    print("Success! Data cleaned. Missing values removed.")
    return df_cleaned

# --- FINAL EXECUTION CODE ---

# Define the path to your file
file_path = "data/raw/brazilian-ecommerce/olist_orders_dataset.csv"

# Run the cleaning process
df_raw = load_data(file_path)
df_final = clean_orders(df_raw)

# Print the final summary to verify
print("\n--- Summary After Cleaning ---")
print(df_final.info())
# --- Customers Data Cleaning ---

# 1. Define the path for the customers dataset
customers_file_path = "data/raw/brazilian-ecommerce/olist_customers_dataset.csv"

# 2. Load the customers data
df_customers = load_data(customers_file_path)

# 3. Clean the data (removing any missing values)
df_customers_cleaned = df_customers.dropna()

# 4. Print the summary to verify
print("\n--- Summary After Cleaning Customers ---")
print(df_customers_cleaned.info())
import os

# 1. Create the 'processed' directory if it doesn't exist
output_dir = "data/processed"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
    print(f"Directory created: {output_dir}")

# 2. Save the cleaned Orders dataset
orders_out = os.path.join(output_dir, "cleaned_orders.csv")
df_final.to_csv(orders_out, index=False)
print(f"Success! Saved: {orders_out}")

# 3. Save the cleaned Customers dataset
customers_out = os.path.join(output_dir, "cleaned_customers.csv")
df_customers_cleaned.to_csv(customers_out, index=False)
print(f"Success! Saved: {customers_out}")
# --- Products Data Cleaning ---
products_file_path = "data/raw/brazilian-ecommerce/olist_products_dataset.csv"
df_products = load_data(products_file_path)
df_products_cleaned = df_products.dropna()

print("\n--- Summary After Cleaning Products ---")
print(df_products_cleaned.info())

# Save the cleaned Products dataset
products_out = os.path.join(output_dir, "cleaned_products.csv")
df_products_cleaned.to_csv(products_out, index=False)
print(f"Success! Saved: {products_out}")
# --- Order Items Data Cleaning ---
items_file_path = "data/raw/brazilian-ecommerce/olist_order_items_dataset.csv"
df_items = load_data(items_file_path)

# Cleaning: Remove rows with missing prices or freight values
df_items_cleaned = df_items.dropna(subset=['price', 'freight_value'])

print("\n--- Summary After Cleaning Order Items ---")
print(df_items_cleaned.info())

# Save the cleaned Order Items dataset
items_out = os.path.join(output_dir, "cleaned_order_items.csv")
df_items_cleaned.to_csv(items_out, index=False)
print(f"Success! Saved: {items_out}")