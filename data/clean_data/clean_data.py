import pandas as pd

file_name = 'data/student.csv'
file_name_clean_data = 'data/student_clean.csv'

try:
    data = pd.read_csv(file_name, nrows=500)
except FileNotFoundError:
    print(f"File {file_name} was not found.")
else:
    data.drop(['Age', 'Use_of_Educational_Tech'], inplace=True, axis=1)
    data.to_csv(file_name_clean_data, index=False)
