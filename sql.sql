-- 1. Dimension Tables
-- Storing descriptive data about customers, products, and time

CREATE TABLE dim_customers (
    customer_key SERIAL PRIMARY KEY,      -- Surrogate Key for internal linking
    customer_id VARCHAR(50) UNIQUE,       -- Original Brazilian ID (Hash)
    customer_name VARCHAR(255),
    customer_city VARCHAR(100),
    customer_state CHAR(2)                -- State abbreviation (e.g., SP, RJ)
);

CREATE TABLE dim_products (
    product_key SERIAL PRIMARY KEY,
    product_id VARCHAR(50) UNIQUE,
    product_category_name VARCHAR(100),
    product_weight_g INT
);

CREATE TABLE dim_date (
    date_key SERIAL PRIMARY KEY,
    full_date DATE UNIQUE,
    year INT,
    month INT,
    day INT,
    weekday VARCHAR(20)
);

-- 2. Fact Table
-- The central table linking all dimensions and storing numerical measures

CREATE TABLE fact_orders (
    order_id VARCHAR(50) PRIMARY KEY,
    customer_key INT REFERENCES dim_customers(customer_key),
    product_key INT REFERENCES dim_products(product_key),
    date_key INT REFERENCES dim_date(date_key),
    price DECIMAL(10,2),
    freight_value DECIMAL(10,2)           --  data)
);
SELECT 
    'Total Revenue' AS Metric, 
    ROUND(SUM(price + freight_value)::numeric, 2) AS Value 
FROM fact_orders

UNION ALL

SELECT 
    'Total Order Count', 
    COUNT(*) 
FROM fact_orders

UNION ALL

SELECT 
    'Broken Links (Missing Customers)', 
    COUNT(*)
FROM fact_orders f
LEFT JOIN dim_customers c ON f.customer_key = c.customer_key
WHERE c.customer_key IS NULL

UNION ALL

SELECT 
    'Duplicate Order IDs', 
    COUNT(order_id) - COUNT(DISTINCT order_id)
FROM fact_orders;