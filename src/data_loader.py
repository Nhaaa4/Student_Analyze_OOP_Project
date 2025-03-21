import pandas as pd 

class DataLoader:   
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = pd.read_csv(self.file_path)

    def get_data(self):
        return self.df
    
    def data_sample(self):
        return self.df.sample(10)
    
    def data_info(self):
        return self.df.info()
    
    def data_describe(self):
        return self.df.describe()