import pandas as pd # type: ignore

def laod_data(file_path):
    return pd.read_csv(file_path)