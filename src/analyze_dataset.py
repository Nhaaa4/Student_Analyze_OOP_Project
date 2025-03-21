import seaborn as sns
import matplotlib.pyplot as plt

class AllStudentPerformanceVisualize:
    def __init__(self, df):
        self.__df = df

    @property
    def df(self):
        return self.__df

    # Visualize the distribution of final grade
    def final_grade_visualize(self):
        ax = self.df['Final_Grade'].value_counts(sort=False).sort_index().plot(kind='bar', color='royalblue')
        ax.bar_label(ax.containers[0], color='black')
        plt.title("Visualize Grade's Student Count\n", color='red', weight='bold')
        plt.xlabel('Final Grade', fontsize=12)
        plt.xticks(rotation=20, color='red')
        plt.ylabel('Number of Student', fontsize=12)

    # Visualize the distribution of study hours per week for a specific grade
    def study_hours_by_grade(self, grade):
        study_hours = self.df.groupby('Final_Grade')['Study/Week'].value_counts().loc[grade] # Get the study hours distribution for a specific grade

        x = study_hours.index  # Get the study hours
        y = study_hours.values  # Get the number of students for each study hours

        plt.hist(x, weights=y, color='skyblue', edgecolor='black', alpha=0.7)

        plt.xlabel('Study Hours per Week')
        plt.ylabel('Number of Students')
        plt.title(f'Study Hours Distribution for Students with Grade {grade}')

        plt.grid(axis='y', linestyle='--')
    
    # Visualize the distribution of learning style for a specific grade
    def study_hour_visualize(self):
        # Plot the average study hours per week for each grade use line plot
        self.df.groupby('Final_Grade')['Study/Week'].mean().plot(kind='line', marker='o', linestyle='-', grid=True) 

        plt.title("Average Study Hours per Week by Final Grade")
        plt.xlabel("Final Grade")
        plt.ylabel("Average Study Hours per Week")

    # Visualize the distribution of learning style for a specific grade 
    def learning_style_visualize(self):
        grade = ['A', 'B', 'C', 'D']

        plt.suptitle('Preferred Learning Style with Final Grade', weight='bold')
        # Use pie chart to visualize the distribution of learning style for each grade
        for i in range(4):
            # Create a subplot for each grade
            plt.subplot(2, 2, i + 1) # 2 rows, 2 columns
            students = self.df[self.df['Final_Grade'] == grade[i]]
            learning_style_counts = students['Learning_Style'].value_counts() # Get the count of each learning style
            plt.pie(learning_style_counts, labels=learning_style_counts.index, autopct='%1.1f%%', textprops={'fontsize': 9}) # autopct to show the percentage
            plt.title(f"Grade {grade[i]}", fontsize=9, weight='bold', color='red')

    # Visualize the distribution of participation in discussions for a specific grade
    def discussion_visualize(self):
        # Use boxplot
        plt.subplot(1, 2, 1)
        plt.title('Discussion: Yes')
        sns.boxplot(y=self.df[self.df['Participation_in_Discussions'] == 'Yes']['Final_Grade'])

        plt.subplot(1, 2, 2)
        plt.title('Discussion: No')
        sns.boxplot(y=self.df[self.df['Participation_in_Discussions'] == 'No']['Final_Grade'])

    # Visualize the distribution of assignment completion rate for a specific grade
    def assignment_rate_visualize(self):
        # Use line plot 
        df_line = self.df.groupby('Final_Grade')['Assignment_Completion_Rate'].mean().reset_index() # Get the average assignment completion rate for each grade

        sns.lineplot(x='Final_Grade', y='Assignment_Completion_Rate', data=df_line, marker='o')
        plt.title('Average Assignment Completion Rate by Final Grade')
        plt.xlabel('Final Grade')
        plt.ylabel('Average Assignment Completion Rate (%)')
        plt.grid(True) # Add grid

    # Visualize the distribution of exam score for a specific grade
    def exam_score_visualize(self):
        sns.boxplot(x=self.df['Final_Grade'], y=self.df['Exam_Score']) # get the exam score distribution for each grade
        plt.title("Exam Score Distribution by Final Grade")
        plt.xlabel("Final Grade")
        plt.ylabel("Percentage of Exam Score")

    # Visualize the distribution of attendance rate for a specific grade
    def attendance_rate_visualize(self):
        sns.displot(self.df, x="Attendance_Rate", hue="Final_Grade", kind="kde", hue_order=['A', 'B', 'C', 'D'])
        plt.title("Comparison of Attendance Reate by Grade")
        plt.xlabel('Attendance Rate (%)')

    # Visualize the distribution of self-reported stress level for a specific grade
    def stress_report_visualize(self):
        # get the number of students with each stress level for each grade
        ax = sns.catplot(x=self.df['Final_Grade'], hue=self.df['Stress_Level'], order=['A', 'B', 'C', 'D'], kind='count')
        plt.title('Visualizing Number of Students with Final Grade', weight='bold')
        plt.ylabel('Number of Students')
        for container in ax.ax.containers: # Add the number of students on top of each bar
            ax.ax.bar_label(container)

    # Visualize the distribution of free time for a specific grade
    def free_time_visualize(self):
        sns.displot(self.df, x="Free_Time_/Week", hue="Final_Grade", kind="kde", hue_order=['A', 'B', 'C', 'D'])
        plt.title("Comparison of Free Time (hours/week) by Grade")

    # Visualize the distribution of sleep hours per night for a specific grade
    def sleep_hours_visualize(self):
        sns.displot(self.df, x="Sleep/Night", hue="Final_Grade", kind="kde", hue_order=['A', 'B', 'C', 'D'])
        plt.title("Comparison of Sleep Hours per Night by Grade")

class AllStudentPerformanceAnalyze(AllStudentPerformanceVisualize):
    def __init__(self, df):
        super().__init__(df)

    # Analyze the final grade by visualizing the number of students in each grade
    def final_grade_analyze(self):
        print("1. Graph below show the number of student by final grade")
        self.final_grade_visualize() # get the graph
        plt.show()  # Show the graph
        # Describe the graph
        print("In this picture, there are bars chart that present the relationship between Number of Student \n"
              "and Final Grade. There are four categories of the student grade (A, B, C, D) and the limit of the \n"
              "number of student in each category is 140. The First pie chart present 108 student that has grade A, \n"
              "and it is the least amount of student among the grade, follow by Grade B that has 132 and Grade C \n"
              "that has 125 student, and Grade D has 135 student which is the most common grade in the chart.\n")

    # Analyze the study hours per week 
    def study_hour_analyze(self):
        print("2. Graph below show the study hours per week compare their grade")
        self.study_hour_visualize() # get the graph
        plt.show() # Show the graph
        # Describe the graph
        print("This is a line graph that present about the relationship between Average Study Hours per week with\n" 
              "Final Grade. For Grade A students spent less than 27 hours per week, followed by grade B student study\n" 
              "less than 26.5 hour per week, for grade C student spent less than 27.5 hours per week, while student with\n" 
              "Grade D student spent 28 hours per week. This graph show that student in Grade A spent their time efficient\n" 
              "than grade D which study more than 28 hours and did not get good result.\n")

    # Analyze the learning style
    def learning_style_analyze(self):
        print("3. Graph below show the preffferred learning style compare their grade")
        self.learning_style_visualize() # get the graph
        plt.show() # Show the graph
        # Describe the graph
        print("Describe: This is 4 pie charts which represent the relationship between learning style and final grade\n"
              "(A, B, C and D). Each chart categorize student into four learning style such as Visual, Kinesthetic, \n"
              "Auditory and Reading/Writing. Grade A student mostly prefered Visual learning (31.5%), followed Kinesthetic\n"
              "(26.9%) and Reading/Writing learning (23.1%), and Auditory learning (18.5%) is the least common learning \n"
              "style that student prefered. The second pie chart present the relationship between learning and final grade B.\n" 
              "Student grade B mostly prefered Auditory learnining (27.3%) which is the common learning style that the student\n" 
              "prefered in grade B, followed by Reading/Writing learning (26.5%) and Visual learning (25.8%), and Kinesthetic\n" 
              "(20.5%) the least common learning style in grade B represented chart. Grade C chart, Most student prefered Auditory\n" 
              "learning (26.4%), followed by Visual learning (25.6%) and Kinesthetic learning (23.2%), and Reading/Writing (23.25)\n" 
              "is the least common learning style prefered. Grade D, Reading/Writing (27.4%) is the most common learning, followed\n" 
              "by Kinesthetic learning (25.9%) and Visual learning (25.2%), and Auditory learning (21.5%) the least common learning\n" 
              "style in grade D. This chart suggest the student to prefered Visual learning becuase it is poppular in grade A. \n"
              "Student grade D mostly prefer Reading/Writing learning.\n")

    # Analyze the participation in discussions
    def discussion_analyze(self):
        print("4. Graph below show the participation in discussion compare their grade")
        self.discussion_visualize()
        plt.show()

        print("This is a box chart that present the relationship between Discussion and Final Grade. These chart mean that\n"
              "discussion does not affect on student grade since these chart are perfectly the same.\n")

    # Analyze the assignment completion rate
    def assignment_rate_analyze(self):
        print("5. Graph below show the assignment rate with their grade")
        self.assignment_rate_visualize()
        plt.show()

        print("This graph present about Average Assignment Completion Rate by Final grade The limit average assignment completion rate is 75%\n" 
              "and the Final Grad is A, B, C, and D. Student grade A has the highest assignment completion rate (more than 75%), student grade B\n"
              "has the lowest assignment completion rate (less than 72.5%), student grade C (less than 74%), student with grade D has 74.5%\n"
              "completion rate. This mean that the data is not have no affect on the grade.\n")

    # Analyze the exam score
    def exam_score_analyze(self):
        print("6. Graph below show the exam score with their grade")
        self.exam_score_visualize()
        plt.show()

        print("This is a box chart that present the Exam Score Distribution by Final Grade. The limit score is 100 percentage and Final Grade \n"
              "(A, B, C, D). Student Grade C has more than 60%, Student Grade D has less than 50%, Student Grade B has more than 70% but less\n"
              "than 80%, Student Grade A has more than 93%.\n")

    # Analyze the attendance rate
    def attendance_rate_analyze(self):
        print("7. Graph below show the attendace rate with their grade")
        self.attendance_rate_visualize()
        plt.show()

        print("This histogram show about the Comparison of Attendance Rate with Grade (A, B, C, D), Student Grade A attend the class less\n" 
              "than the other grade, Student Grade B attend class more than others, followed by Grade C and Grade D which attend the class\n" 
              "more than grade A. This histogram of Attendance Rate does not affect on the student grade.\n")

    # Analyze the self-reported stress level
    def stress_report_analyze(self):
        print("8. Graph below show the self reported stress level with their grade")
        self.stress_report_visualize()
        plt.show()

        print("This bar chart present the relationship between the number of student with final grade of student that have the level of stress.\n"
              "There are 3 level of stress such as High (Blue), Medium (Medium), Low (Low), Grade A student with the high stress(22), medium(54),\n" 
              "low(32), Student grade B, high level of stress (24), medium (73), low (35). Student Grade C, High(27), Medium (64), Low (34).\n"
              "Student with grade D, High (24), Medium (57), Low (54).This chart show that student with grade A has the least stress level High,\n"
              "Medium, Low compare to other Grade.\n")

    # Analyze the free time
    def free_time_analyze(self):
        print("9. Graph below show the free time with their grade")
        self.free_time_visualize()
        plt.show()

        print("This is a histogram that explain about the Comparison of Free Time (hours/week) by Grade. The limit of free time hour is \n"
              "from - 10 to 40 hours a week. The highest free time level of stress is  Grade B free time between 10 to 30  and Grade C  \n"
              "free time between 0 to 10 students, follow by Grade D student who has free time between 10 to 20 hours, Student Grade A has\n"
              "the least free time between 0 to 10 hours. This histogram show us about the performance of each grade of student, Student \n"
              "grade A has the least free time than grade B, C, and D.\n")

    # Analyze the sleep hours per night
    def sleep_hours_analyze(self):    
        print("10. Graph below show the sleep hours per night with their grade")
        self.sleep_hours_visualize()
        plt.show()

        print("This histogram explain about the comparison of sleep hour per night by grade. the limit of sleep hour is from 2 to 12 hour.\n"
              "Student grade sleep 8 hours a day. while grade B sleep between 6 to 8 hours. Grade C student sleep between 4 to 8 hours . \n"
              "Student Grade D sleep between 4 to more than 10 hours.\n")