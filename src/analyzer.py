import pandas as pd
import math 
from tabulate import tabulate
class StudentPerformanceAnalyze:
    def __init__(self, df):
        self.df = df
        # self.__welcome_message()


    def welcome_message(self):
        print(f"\n\tWelcome to Student Analysis")
        print(f"Our Analysis is base on 500 dataset of student only.")


    def __assigment_complete_rate_avg(self,finalGrade, style):
        workHardstudentData = self.df[
            ((self.df["Final_Grade"] == finalGrade) & 
            (self.df["Learning_Style"] == style) & 
            ((self.df["Study/Week"] >= 30)))
        ]

        workSmartstudentData = self.df[
            ((self.df["Final_Grade"] == finalGrade) & 
            (self.df["Learning_Style"] == style) & 
            ((self.df["Study/Week"] < 30)))
        ]

        # print(type(workSmartstudentData))
        assignCompleteRateList = workHardstudentData["Assignment_Completion_Rate"].tolist()
        average = sum(assignCompleteRateList) / len(assignCompleteRateList)

        assignCompleteRateList1 = workSmartstudentData["Assignment_Completion_Rate"].tolist()
        average1 = sum(assignCompleteRateList1) / len(assignCompleteRateList1)

        myAssignmentAvgList = []
        myAssignmentAvgList.append(average)
        myAssignmentAvgList.append(average1)

        return myAssignmentAvgList
        
    def __attendance_rate_avg(self, finalGrade, style):
        workHardstudentData = self.df[
            ((self.df["Final_Grade"] == finalGrade) & 
            (self.df["Learning_Style"] == style) & 
            ((self.df["Study/Week"] >= 30)))
        ]

        workSmartstudentData = self.df[
            ((self.df["Final_Grade"] == finalGrade) & 
            (self.df["Learning_Style"] == style) & 
            ((self.df["Study/Week"] < 30)))
        ]

        attedanceRateList = workHardstudentData["Attendance_Rate"].tolist()
        average = sum(attedanceRateList) / len(attedanceRateList)

        attedanceRateList1 = workSmartstudentData["Attendance_Rate"].tolist()
        average1 = sum(attedanceRateList1) / len(attedanceRateList1)

        myAttendanceRateList = []
        myAttendanceRateList.append(average)
        myAttendanceRateList.append(average1)

        return myAttendanceRateList
    
    def __stu_stress_level(self, finalGrade, style):
        # Work hard students
        workHardstudentData = self.df[
            (self.df["Final_Grade"] == finalGrade) & 
            (self.df["Learning_Style"] == style) & 
            (self.df["Study/Week"] >= 30)
        ]
    
        countLowStress = (workHardstudentData["Stress_Level"] == "Low").sum()
        countMedStress = (workHardstudentData["Stress_Level"] == "Medium").sum()
        countHighStress = (workHardstudentData["Stress_Level"] == "High").sum()

        dictOfStressLevel = {"Low": countLowStress, "Medium": countMedStress, "High": countHighStress}
        highRate = max(dictOfStressLevel, key=dictOfStressLevel.get)

        # Work smart students
        workSmartStudentData = self.df[
            (self.df["Final_Grade"] == finalGrade) & 
            (self.df["Learning_Style"] == style) & 
            (self.df["Study/Week"] < 30)
        ]
    
        countLowStress1 = (workSmartStudentData["Stress_Level"] == "Low").sum()
        countMedStress1 = (workSmartStudentData["Stress_Level"] == "Medium").sum()
        countHighStress1 = (workSmartStudentData["Stress_Level"] == "High").sum()

        dictOfStressLevel1 = {"Low": countLowStress1, "Medium": countMedStress1, "High": countHighStress1}
        highRate1 = max(dictOfStressLevel1, key=dictOfStressLevel1.get)

        # Prepare the result
        highestStressLevelRate = [highRate, highRate1]
        return highestStressLevelRate

    def __free_time_avg(self, finalGrade, style):
        workHardstudentData = self.df[
            ((self.df["Final_Grade"] == finalGrade) & 
            (self.df["Learning_Style"] == style) & 
            ((self.df["Study/Week"] >= 30)))
        ]

        workSmartstudentData = self.df[
            ((self.df["Final_Grade"] == finalGrade) & 
            (self.df["Learning_Style"] == style) & 
            ((self.df["Study/Week"] < 30)))
        ]

        # print(type(workSmartstudentData))
        freeTimeList = workHardstudentData["Free_Time_/Week"].tolist()
        average = sum(freeTimeList) / len(freeTimeList)

        freeTimeList1 = workSmartstudentData["Free_Time_/Week"].tolist()
        average1 = sum(freeTimeList1) / len(freeTimeList1)

        stuAvgFreeTime = []
        stuAvgFreeTime.append(average)
        stuAvgFreeTime.append(average1)

        return stuAvgFreeTime
    
    def __online_course_completion_avg(self, finalGrade, style):
        workHardstudentData = self.df[
            ((self.df["Final_Grade"] == finalGrade) & 
            (self.df["Learning_Style"] == style) & 
            ((self.df["Study/Week"] >= 30)))
        ]

        workSmartstudentData = self.df[
            ((self.df["Final_Grade"] == finalGrade) & 
            (self.df["Learning_Style"] == style) & 
            ((self.df["Study/Week"] < 30)))
        ]

        # print(type(workSmartstudentData))
        onlineCourseList = workHardstudentData["Online_Courses_Completed"].tolist()
        average = sum(onlineCourseList) / len(onlineCourseList)

        onlineCourseList1 = workSmartstudentData["Online_Courses_Completed"].tolist()
        average1 = sum(onlineCourseList1) / len(onlineCourseList1)

        stuOnlineCourseCompletionAvgList = []
        stuOnlineCourseCompletionAvgList.append(math.floor(average))
        stuOnlineCourseCompletionAvgList.append(math.floor(average1))

        return stuOnlineCourseCompletionAvgList
    
    def __sleep_hour_avg(self, finalGrade, style):
        workHardstudentData = self.df[
            ((self.df["Final_Grade"] == finalGrade) & 
            (self.df["Learning_Style"] == style) & 
            ((self.df["Study/Week"] >= 30)))
        ]

        workSmartstudentData = self.df[
            ((self.df["Final_Grade"] == finalGrade) & 
            (self.df["Learning_Style"] == style) & 
            ((self.df["Study/Week"] < 30)))
        ]

        # print(type(workSmartstudentData))
        sleepHourList = workHardstudentData["Sleep/Night"].tolist()
        average = sum(sleepHourList) / len(sleepHourList)

        sleepHourList1 = workSmartstudentData["Sleep/Night"].tolist()
        average1 = sum(sleepHourList1) / len(sleepHourList1)

        stuSleepHourAvgList = []
        stuSleepHourAvgList.append(math.floor(average))
        stuSleepHourAvgList.append(math.floor(average1))

        return stuSleepHourAvgList

    def analyData(self, finalGrade, style):
       
        studentData = self.df[
            ((self.df["Final_Grade"] == finalGrade) & 
            (self.df["Learning_Style"] == style) & 
            ((self.df["Study/Week"] >= 30) | (self.df["Study/Week"] < 30)))
        ][["Learning_Style","Final_Grade","Study/Week", "Assignment_Completion_Rate", "Attendance_Rate","Stress_Level","Free_Time_/Week","Online_Courses_Completed", "Sleep/Night"]]

       
       # Visualize style Grade A, Hard work 
        studentData = studentData.sort_values(
            by=["Final_Grade","Study/Week"], 
            ascending=[True, False]  # Adjust order as needed
        )
        print(f"{studentData.to_string(index=False)}" )
       # the data set that we got from kaggle is very similar so let a general analyze since we can not distinguish the different between final grade 
       # and learning style 

        if style:
            print("\n")
            print(f"\nFor Grade: {finalGrade} Students")
            print(f"Hard Work Student Analysis:")
            print(f"\t- Their assignment completion rate is on average {self.__assigment_complete_rate_avg(finalGrade, style)[0]:.2f}%.")
            print(f"\t- Attendance rates are {self.__attendance_rate_avg(finalGrade, style)[0]:.2f}, except for one student. Mostly their stress level are {self.__stu_stress_level(finalGrade, style)[0]}.")
            print(f"\t- Their free time per are {self.__free_time_avg(finalGrade, style)[0]:.2f} hours per week in average.")
            print(f"\t- Their online course completion are {self.__online_course_completion_avg(finalGrade, style)[0]:.0f} in average.")
            print(f"\t- Their sleep hour in avg are {self.__sleep_hour_avg(finalGrade, style)[0]:.2f} \n")
        
            print(f"Smart Work Student Analysis:")
            print(f"\t- Their assignment completion rate is also {self.__assigment_complete_rate_avg(finalGrade, style)[1]:.2f}% on average.")
            print(f"\t- Attendance rates are {self.__attendance_rate_avg(finalGrade, style)[1]:.2f}. Mostly their stress level are {self.__stu_stress_level(finalGrade, style)[1]}.")
            print(f"\t- Their online course completion are {self.__online_course_completion_avg(finalGrade, style)[1]:.0f} in average.")
            print(f"\t- Their sleep hour in avg are {self.__sleep_hour_avg(finalGrade, style)[0]:.2f} \n")
    

    # analyse overall data set 

    def overall_stu_analysis(self):

        countAuStyle = self.df[(self.df["Learning_Style"] == "Auditory")].shape[0]
        countRWStyle = self.df[(self.df["Learning_Style"] == "Reading/Writing")].shape[0]
        countKStyle = self.df[(self.df["Learning_Style"] == "Kinesthetic")].shape[0]
        countVStyle = self.df[(self.df["Learning_Style"] == "Visual")].shape[0]

        countAuGradeA = self.df[(self.df["Learning_Style"] == "Auditory") & (self.df["Final_Grade"] == "A")].shape[0]
        countRWGradeA = self.df[(self.df["Learning_Style"] == "Reading/Writing") & (self.df["Final_Grade"] == "A")].shape[0]
        countKGradeA = self.df[(self.df["Learning_Style"] == "Kinesthetic") & (self.df["Final_Grade"] == "A")].shape[0]
        countVSGradeA = self.df[(self.df["Learning_Style"] == "Visual") & (self.df["Final_Grade"] == "A")].shape[0]

        countAuGradeB = self.df[(self.df["Learning_Style"] == "Auditory") & (self.df["Final_Grade"] == "B")].shape[0]
        countRWGradeB = self.df[(self.df["Learning_Style"] == "Reading/Writing") & (self.df["Final_Grade"] == "B")].shape[0]
        countKGradeB = self.df[(self.df["Learning_Style"] == "Kinesthetic") & (self.df["Final_Grade"] == "B")].shape[0]
        countVSGradeB = self.df[(self.df["Learning_Style"] == "Visual") & (self.df["Final_Grade"] == "B")].shape[0]

        countAuGradeC = self.df[(self.df["Learning_Style"] == "Auditory") & (self.df["Final_Grade"] == "C")].shape[0]
        countRWGradeC = self.df[(self.df["Learning_Style"] == "Reading/Writing") & (self.df["Final_Grade"] == "C")].shape[0]
        countKGradeC = self.df[(self.df["Learning_Style"] == "Kinesthetic") & (self.df["Final_Grade"] == "C")].shape[0]
        countVSGradeC = self.df[(self.df["Learning_Style"] == "Visual") & (self.df["Final_Grade"] == "C")].shape[0]

        countAuGradeD = self.df[(self.df["Learning_Style"] == "Auditory") & (self.df["Final_Grade"] == "D")].shape[0]
        countRWGradeD = self.df[(self.df["Learning_Style"] == "Reading/Writing") & (self.df["Final_Grade"] == "D")].shape[0]
        countKGradeD = self.df[(self.df["Learning_Style"] == "Kinesthetic") & (self.df["Final_Grade"] == "D")].shape[0]
        countVSGradeD = self.df[(self.df["Learning_Style"] == "Visual") & (self.df["Final_Grade"] == "D")].shape[0]
        

        overallData = []
        headers = ["Title","Kinesthetic", "Auditory", "Reading/Writing", "Visual"]
        numOfStuData = ["Number Of Student",countKStyle, countAuStyle, countRWStyle, countVStyle]
        numOfGradeA = ["Number Of Grade A",countKGradeA, countAuGradeA, countRWGradeA, countVSGradeA]
        numOfGradeB = ["Number Of Grade B",countKGradeB, countAuGradeB, countRWGradeB, countVSGradeB]
        numOfGradeC = ["Number Of Grade C",countKGradeC, countAuGradeC, countRWGradeC, countVSGradeC]
        numOfGradeD = ["Number Of Grade D",countKGradeD, countAuGradeD, countRWGradeD, countVSGradeD]
        
        overallData.append(numOfStuData)
        overallData.append(numOfGradeA)
        overallData.append(numOfGradeB)
        overallData.append(numOfGradeC)
        overallData.append(numOfGradeD)
        print(tabulate(overallData, headers, tablefmt="grid"))
     
    def general_analysis(self):
        print(f"\n\tGeneral Analysis base on data set and experience: \n")
        print(f"\t\tBy the data set given, we can see that some student have the same habit and learning style and effort,")
        print(f"\t\tbut why they end up in the different Grade ?")
        print(f"\t\tFirst of all Time spend: ")
        print(f"\t\tSome student spend a plently of time on learning but they did not spent it effectively.")
        print(f"\t\tTheir focus and concentration must be a big different for their understanding and long-term memory.")
        print(f"\t\tEven if they complete the same test and recieve the same result")
        print(f"\t\tdoes not mean they're on the same level.")
        print(f"\t\tsome of them might complete the test by their understand and some not")
        print(f"\t\they might get lucky sometime because the test and the lesson are the same(require the same solution)")
        print(f"\t\tMoreover, both mindset and mentality are also important.")
        print(f"\t\tFor student who have strong mentality they might have a chance to grow faster than other.")
        print(f"\t\tIt's a key or a disciplne for them to keep leaning, exploration, self-study and research. ")
        print(f"\t\tUnlike other student they might only want to complete the work which given by their lectreuer.")
        print(f"\t\tLastly, base on our experience we see that some student who have low metality")
        print(f"\t\tno matter how effort thier put, they will alway end up with low grade.")

if __name__ == "__main__":
    data = pd.read_csv("data/student_clean.csv")
    student_analyze = StudentPerformanceAnalyze(data)
    student_analyze.analyData("A", "Visual")
    student_analyze.analyData("B", "Visual")
    student_analyze.analyData("C", "Visual")
    student_analyze.analyData("D", "Visual")
    student_analyze.general_analysis()
    student_analyze.overall_stu_analysis()

