import pandas as pd

file_name = 'data/student.csv'
file_name_clean_data = 'data/student_clean.csv'

try:
    data = pd.read_csv(file_name, nrows=500)
except FileNotFoundError:
    print(f"File {file_name} was not found.")
else:
    data.drop(['Gender', 'Student_ID', 'Age', 'Online_Courses_Completed'], inplace=True, axis=1)
    data.rename(columns={'Time_Spent_on_Social_Media (hours/week)': 'Free_Time (hours/week)'}, inplace=True)
    data.to_csv(file_name_clean_data, index=False)
