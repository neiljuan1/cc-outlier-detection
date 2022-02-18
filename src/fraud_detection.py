
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os



def initialize_df(file_name: str, path: str)->pd.DataFrame:
    return pd.read_csv(os.path.join(path, file_name))


file_name = "creditcard.csv"
path = "D:/Datasets/CreditCardsKaggle"
df = initialize_df(file_name, path)

print(df.describe())