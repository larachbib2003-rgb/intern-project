import opendatasets as od

# Dataset URL from Kaggle
dataset_url = "https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce"

# Download the dataset into the 'data/raw' directory
od.download(dataset_url, data_dir="data/raw")