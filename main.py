from src.data_loader import DataLoader
from src.analyze_dataset import AllStudentPerformanceAnalyze
from src.analyzer import StudentPerformanceAnalyze
from src.userinput import U_Input_Output

# Function to analyze all students
def all_students_analyze(data, all_std_ana):

    print(data.data_sample())
    print(data.data_info())
    print(data.data_describe())

    all_std_ana.final_grade_analyze()
    all_std_ana.study_hour_analyze()
    all_std_ana.learning_style_analyze()
    all_std_ana.discussion_analyze()
    all_std_ana.assignment_rate_analyze()
    all_std_ana.exam_score_analyze()
    all_std_ana.attendance_rate_analyze()
    all_std_ana.stress_report_analyze()
    all_std_ana.free_time_analyze()
    all_std_ana.sleep_hours_analyze()

# Function to analyze a student
def analyze_student(student_analyze):
    while(True):
        print("\n\tStudent Analysis")
        print("1. Analyze Student")
        print("2. General Analysis")
        print("3. Back to Main Menu")
        while(True):
            try:
                a = int(input("Choose your option: "))
            except:
                print('Your input was wrong.')
            else:
                break
        match a:
            case 1:
                while(True):
                    FinalGrade = input("Final Grade(A, B, C, D): ").lower().capitalize()
                    if(FinalGrade in ['A', 'B', 'C', 'D']):
                        break
                while(True):
                    learning_style = input("Enter Learning Style (Visual, Auditory, Reading/Writing, Kinesthetic): ").strip().lower().capitalize()
                    if(learning_style in ['Visual', 'Auditory', 'Reading/writing', 'Kinesthetic']):
                        break
                student_analyze.analyData(FinalGrade, learning_style)
            case 2:
                student_analyze.general_analysis()
                student_analyze.overall_stu_analysis()
            case 3:
                main()
            case _:
                break
# Main function
def main():
    while(True):
        print('\n\tWelcome to Student Performance Analysis Program')
        print('1. Analyze Dataset')
        print('2. Student Analysis')
        print('3. Suggestions')
        print('4. End Program')

        while(True):
            try:
                op = int(input("Choose your pbtion: "))
            except:
                print('Your input was wrong. Please input number')
            else:
                break

        match op:
            case 1:
                all_students_analyze(data, all_std_ana)
            case 2:
                analyze_student(student_analyze)
            case 3:
                U_Input_Output()
            case 4:
                print("End Program")
                exit()
            case _:
                print("Choose a valid option")

# Main function to run the program
file_path = 'data/student_clean.csv' # Path to the dataset

data = DataLoader(file_path)
df = data.get_data() # Get the dataset

all_std_ana = AllStudentPerformanceAnalyze(df) # Create an object of AllStudentPerformanceAnalyze
student_analyze = StudentPerformanceAnalyze(df) # Create an object of StudentPerformanceAnalyze

main()