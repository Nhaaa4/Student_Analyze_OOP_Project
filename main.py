from src.data_loader import laod_data
from src.analyzer import StudentPerformanceAnalyze

file_path = 'data/student_clean.csv'

data = laod_data(file_path)
student_analyze = StudentPerformanceAnalyze(data)

# student_analyze.study_hour_vs_final_grade()
# student_analyze.learning_style_vs_grade()
# student_analyze.discussion_vs_final_grade()
# student_analyze.assignment_vs_final_grade()
# student_analyze.exam_score_vs_final_grade()
# student_analyze.attendance_vs_final_grade()
# student_analyze.use_educational_tect_vs_final_grade()
# student_analyze.stress_report_vs_final_grade()
# student_analyze.free_time_vs_final_grade()
# student_analyze.sleep_vs_final_gradea()