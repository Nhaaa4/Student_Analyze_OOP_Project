from src.data_loader import laod_data
from src.analyzer import StudentPerformanceAnalyze

file_path = 'data/student_clean.csv'

data = laod_data(file_path)
student_analyze = StudentPerformanceAnalyze(data)

student_analyze.stress_report_vs_final_grade()