import json
import pandas as pd
        
def student_info(self):
        return f"\n\nStudy Hour: {self.Study_Hour_per_Week} \n Preffered Learning Style:{self.Preffered_Learning_Style} \n Assignment Completion Rate:{self.Assignment_Completion_Rate} \n Exam Score: {self.Exam_Score} \n Attendance Rate: {self.Attendance_Rate} \n Report Stress Level: {self.Self_Reported_Stress_Level} \n Time Spent on Socail Media: {self.Time_spent_on_Social_Media_Hour_per_Week} \n Sleep Hour: {self.Sleep_Hour_per_Night} \n Final Grade: {self.Final_Grade}"

class Student:
    def __init__(self, study_hours, assigment_rate, attendance_rate, stress_level, free_time, sleep_hour, final_grade, learning_style, participate, online_course):
        self.study_hours = study_hours
        self.attendance_rate = attendance_rate
        self.assignment_rate = assigment_rate
        self.stress_level = stress_level
        self.free_time = free_time
        self.sleep_hour = sleep_hour
        if (final_grade == 'D'):
            self.final_grade = 'C'
        elif (final_grade == 'C'):
            self.final_grade = 'B'
        elif (final_grade == 'B'):
            self.final_grade = 'A'
        elif (final_grade == 'A'):
            self.final_grade = 'A'
        self.learning_style = learning_style
        self.participate = participate
        self.online_course = online_course

with open("data/student_clean.csv", "r") as f:
    df = pd.read_csv(f)


def studentSleepStress(student):
    stress = ['Medium', 'High']
    with open("data/model.json", "r") as file:
            data = json.load(file)
    if student.sleep_hour <= 6 and student.stress_level in stress:
        print('    Your sleep will effect on your Stress level.')
    
    #sleep hour
    print("- Sleep hour")
    if student.sleep_hour <= 6:
        sleepHour = data['General Suggestion']['Sleep Hour Per Night']['Low']
        if isinstance(sleepHour, str) and sleepHour:
            print(f"    {sleepHour}")
        else:
            print("File did not read")
    elif student.sleep_hour > 6:
        sleepHour = data['General Suggestion']['Sleep Hour Per Night']['Low']
        if isinstance(sleepHour, str) and sleepHour:
            print(f"    {sleepHour}")
        else:
            print("File did not read")
    #stress
    print("- Stress level")
    stressLevel = data['General Suggestion']['Self Report Stress Level'][student.stress_level]
    if isinstance(stressLevel, str) and stressLevel:
        print(f"    {stressLevel}")
    else:
        print("File did not read")
    

def general(student):
    #Study Hour
    print("- Study hour")
    with open("data/model.json", "r") as file:
            data = json.load(file)
    if student.study_hours <= 24:
        studyHour = data[student.learning_style][student.final_grade]['studyHour']['smart']
        if isinstance(studyHour, str) and studyHour:
            print(f"    {studyHour}")
        else:
            print("File did not read")
    elif student.study_hours >= 24 and student.study_hours <= 100:
        studyHour = data[student.learning_style][student.final_grade]['studyHour']['hard']
        if isinstance(studyHour, str) and studyHour:
            print(f"    {studyHour}")
        else:
            print("File did not read")
    else:
        print("NO data in file")
    #Assignment Completion
    print("- Assignment Completion")
    if student.assignment_rate >= 1 and student.assignment_rate < 71:
            assignmentCompleteBad = data[student.learning_style][student.final_grade]['Assignment_Completion_Rate']["Bad"]
            if isinstance(assignmentCompleteBad, str) and assignmentCompleteBad:
                print(f"    {assignmentCompleteBad}")
            else:
                print("File did not read")
    elif student.assignment_rate > 70:
            assignmentCompleteGood = data[student.learning_style][student.final_grade]['Assignment_Completion_Rate']["Good"]
            if isinstance(assignmentCompleteGood, str) and assignmentCompleteGood:
                print(f"    {assignmentCompleteGood}")
            else:
                print("File did not read")
    
    #Attendence Rate
    print("- Attendence rate")
    if student.attendance_rate < 50:
            attendence = data["General Suggestion"]["Attendence Rate"]["Low"]
            if isinstance(attendence, str) and attendence:
                print(f"    {attendence}")
            else:
                print("File did not read")
    elif student.attendance_rate >= 50 and student.attendance_rate <= 100:
            attendence = data["General Suggestion"]["Attendence Rate"]["High"]
            if isinstance(attendence, str) and attendence:
                print(f"    {attendence}")
            else:
                print("File did not read")  

    #Participation
    print("- Participation")
    if student.participate == "Yes":
        Participate = data['General Suggestion']['Participation']['Yes']
        if isinstance(Participate, str) and Participate:
            print(f"    {Participate}")
        else:
            print("File did not read")
    elif student.participate == "No":
        Participate = data['General Suggestion']['Participation']['No']
        if isinstance(Participate, str) and Participate:
            print(f"    {Participate}")
        else:
            print("File did not read")
    
    #Online course
    print("- Online course")
    if student.online_course >= 35 or student.online_course <= 168:
        onlineCourse = data['General Suggestion']['Course Completion']['Less']
        if isinstance(onlineCourse, str) and onlineCourse:
            print(f"    {onlineCourse}")
        else:
            print("File did not read")
    elif student.online_course < 35 or student.online_course > 0:
        onlineCourse = data['General Suggestion']['Course Completion']['More']
        if isinstance(onlineCourse, str) and onlineCourse:
            print(f"    {onlineCourse}")
        else:
            print("File did not read")
    
    #Free Time
    print("- Free time")
    if student.free_time >= 35 or student.free_time <= 168:
        FreeTime = data['General Suggestion']['Free time (hour/week)']['Less']
        if isinstance(FreeTime, str) and FreeTime:
            print(f"    {FreeTime}")
        else:
            print("File did not read")
    elif student.free_time < 35 or student.free_time > 0:
        FreeTime = data['General Suggestion']['Free time (hour/week)']['More']
        if isinstance(FreeTime, str) and FreeTime:
            print(f"    {FreeTime}")
        else:
            print("File did not read")
    

# Time management_inf
def time_management_inf(student):
        time_list = []
        free_time_aday = student.free_time / 7
        study_time_aday = student.study_hours / 7
        print(f"Time Management:\n    {study_time_aday / 24 * 100:0.0f}%/day for study, {free_time_aday / 24 * 100:0.0f}%/day for free and {student.sleep_hour / 24 * 100:0.0f}% for sleep")
        print(f"    Total: {round(study_time_aday / 24 * 100) + round(free_time_aday / 24 * 100) + (student.sleep_hour / 24 * 100):0.0f}%")

class studentPerformance:
    def __init__(self, study_hours, learning_style):
        self.Study_Hours_per_Week = study_hours
        self.Preferred_Learning_Style = learning_style
    def filter_data(self):
        df = pd.read_csv("data/student_clean.csv", usecols=["Study/Week","Learning_Style", "Final_Grade"])
        Best_grade = df[(df['Final_Grade'] == 'A') & (df['Study/Week'] == self.Study_Hours_per_Week) & (df['Learning_Style'] == self.Preferred_Learning_Style) ]
        return(len(Best_grade))
# Motivation
class Motivation(studentPerformance):
    def suggestMotivation(self):
        len = self.filter_data()
        if (len > 0):
            return (f"PROVIDE MOTIVATION\n"    
                     "You are not alone.\n"    
                    f"There are {len}/500 students that was spend {self.Study_Hours_per_Week} hour per week \n"
                    f"and has learning style {self.Preferred_Learning_Style} like you and their got good grade \n"     
                     "so you could make it, too.")

def U_Input_Output():
    print("Welcome to sugesstion")
    # valid
    learn_style_valid = ['Visual', 'Auditory', 'Reading/writing', 'Kinesthetic']
    stress_level_valid = ['High', 'Medium', 'Low']
    Final_Grade_valid = ['A', 'B', 'C', 'D']
    #input
    while(True):
        try:
            studyHour = int(input("Study Hour: "))
        except:
            print('Your input was wrong. please enter a number.')
        else:
            if(studyHour in range(0, 168)):
                break
            else:
                print('Are you joking to me !(-_-)')
    while(True):
        try:
            AssignmetnComplitionRate = int(input("Assignment Complete Rate: "))
        except:
            print('Your input was wrong. please enter a number.')
        else:
            if(AssignmetnComplitionRate in range(0, 100)):
                break
            else:
                print('Are you joking to me !(-_-)')
    while(True):
        try:
            AttendanceRate = int(input("Give me your attendance rate: "))
        except:
            print('Your input was wrong.')
        else:
            if(AttendanceRate in range(0, 100)):
                break
            else:
                print('Are you joking to me !(-_-)')
    while(True):
        StressLevel = input("Your Stress level(High, Medium, Low): ").lower().capitalize()
        if(StressLevel in stress_level_valid):
            break
    while(True):
        try:
            SleepHour = int(input("Sleep Hour: "))
        except:
            print('Your input was wrong.')
        else:
            if(SleepHour in range(0, 24)):
                break
            else:
                print('Are you joking to me !(-_-)')
    while(True):
        learning_style = input("Enter Learning Style (Visual, Auditory, Reading/Writing, Kinesthetic): ").lower().capitalize()
        if(learning_style in learn_style_valid):
            break
    while(True):
        participation = input("Do you participate in discussions? (Yes/No): ").lower().capitalize()
        if(participation in ['Yes', 'No']):
            break
    while(True):
        try:
            onlineCourse = int(input("How many online course that you was learn?: "))
        except:
            print('Your input was wrong.')
        else:
            if(onlineCourse in range(0, 100)):
                break
            else:
                print('Are you joking to me !(-_-)')
    while(True):
        try:
            free_time = int(input("Your Free time for hour a week: "))
        except:
            print('Your input was wrong.')
        else:
            break
    while(True):
        FinalGrade = input("Final Grade(A, B, C, D): ").lower().capitalize()
        if(FinalGrade in Final_Grade_valid):
            break
    #Output
    student = Student(studyHour, AssignmetnComplitionRate, AttendanceRate, StressLevel, free_time, SleepHour, FinalGrade, learning_style, participation, onlineCourse)
    motivation = Motivation(studyHour,  learning_style)
    print(student.__dict__)
    print("\nSUGGESTION:")
    general(student)
    studentSleepStress(student)
    time_management_inf(student)
    print(motivation.suggestMotivation())

if __name__ == '__main__':
    #valid
    learn_style_valid = ['Visual', 'Auditory', 'Reading/writing', 'Kinesthetic']
    stress_level_valid = ['High', 'Medium', 'Low']
    Final_Grade_valid = ['A', 'B', 'C', 'D']
    #input
    while(True):
        try:
            studyHour = int(input("Study Hour: "))
        except:
            print('Your input was wrong.')
        else:
            if(studyHour in range(0, 168)):
                break
            else:
                print('Are you joking to me !(-_-)')
    while(True):
        try:
            AssignmetnComplitionRate = int(input("Assignment Complete Rate: "))
        except:
            print('Your input was wrong.')
        else:
            if(AssignmetnComplitionRate in range(0, 100)):
                break
            else:
                print('Are you joking to me !(-_-)')
    while(True):
        try:
            AttendanceRate = int(input("Give me your attendance rate: "))
        except:
            print('Your input was wrong.')
        else:
            if(AttendanceRate in range(0, 100)):
                break
            else:
                print('Are you joking to me !(-_-)')
    while(True):
        StressLevel = input("Your Stress level(High, Medium, Low): ").lower().capitalize()
        if(StressLevel in stress_level_valid):
            break
    while(True):
        try:
            SleepHour = int(input("Sleep Hour: "))
        except:
            print('Your input was wrong.')
        else:
            if(SleepHour in range(0, 24)):
                break
            else:
                print('Are you joking to me !(-_-)')
    while(True):
        learning_style = input("Enter Learning Style (Visual, Auditory, Reading/Writing, Kinesthetic): ").lower().capitalize()
        if(learning_style in learn_style_valid):
            break
    while(True):
        participation = input("Do you participate in discussions? (Yes/No): ").lower().capitalize()
        if(participation in ['Yes', 'No']):
            break
    while(True):
        try:
            onlineCourse = int(input("How many online course that you was learn?: "))
        except:
            print('Your input was wrong.')
        else:
            if(onlineCourse in range(0, 100)):
                break
            else:
                print('Are you joking to me !(-_-)')
    while(True):
        try:
            free_time = int(input("Your Free time for hour a week: "))
        except:
            print('Your input was wrong.')
        else:
            break
    while(True):
        FinalGrade = input("Final Grade(A, B, C, D): ").lower().capitalize()
        if(FinalGrade in Final_Grade_valid):
            break


    #Output
    student = Student(studyHour, AssignmetnComplitionRate, AttendanceRate, StressLevel, free_time, SleepHour, FinalGrade, learning_style, participation, onlineCourse)
    motivation = Motivation(studyHour,  learning_style)
    print(student.__dict__)
    print("\nSUGGESTION:")
    general(student)
    studentSleepStress(student)
    time_management_inf(student)
    print(motivation.suggestMotivation())