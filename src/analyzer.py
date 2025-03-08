import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class StudentPerformanceVisualize:
    def __init__(self, df):
        self.__df = df

    @property
    def df(self):
        return self.__df
    
    def study_hour_vs_final_grade(self):
        mean_study_hours = self.df.groupby('Final_Grade')['Study_Hours_per_Week'].mean().reset_index()
        ax = sns.barplot(x='Final_Grade', y='Study_Hours_per_Week', data=mean_study_hours, palette='viridis')
        plt.ylabel('Mean of Time')
        for container in ax.containers:
            ax.bar_label(container, fmt='%.0f')
        plt.title('Visualizing Study Hour Per Week with Final Grade\n', weight='bold', fontsize=13)
        plt.show()

    def learning_style_vs_grade(self):
        grade = ['A', 'B', 'C', 'D']

        plt.figure(figsize=(8, 8))
        plt.suptitle('Preferred Learning Style with Final Grade', weight='bold')

        for i in range(4):
            plt.subplot(2, 2, i + 1)
            students = self.df[self.df['Final_Grade'] == grade[i]]
            learning_style_counts = students['Preferred_Learning_Style'].value_counts()
            plt.pie(learning_style_counts, labels=learning_style_counts.index, autopct='%1.1f%%', textprops={'fontsize': 9})
            plt.title(f"Grade {grade[i]}", fontsize=9, weight='bold', color='red')

        plt.show()
        
    def discussion_vs_final_grade(self):
        ax = sns.countplot(data=self.df, x='Final_Grade', hue='Participation_in_Discussions', order=['A', 'B', 'C', 'D'])
        plt.title('Visualizing Participation with Final Grade', weight='bold', fontsize=13)
        for container in ax.containers:
            ax.bar_label(container)
        plt.show()
    
    def assignment_vs_final_grade(self):
        pivot_df = self.df.groupby('Final_Grade')['Assignment_Completion_Rate (%)'].mean().reset_index()
        sns.lineplot(x='Final_Grade', y='Assignment_Completion_Rate (%)', data=pivot_df, marker="o", color="darkred", linewidth=2)
        plt.show()

    def exam_score_vs_final_grade(self):
        pivot_df = self.df.groupby('Final_Grade')['Exam_Score (%)'].mean().reset_index()
        sns.lineplot(x='Final_Grade', y='Exam_Score (%)', data=pivot_df, marker="o", color="darkred", linewidth=2)
        plt.show()

    def attendance_vs_final_grade(self):
        pivot_df = self.df.groupby('Final_Grade')['Attendance_Rate (%)'].mean().reset_index()
        sns.lineplot(x='Final_Grade', y='Attendance_Rate (%)', data=pivot_df, marker="o", color="darkred", linewidth=2)
        plt.show()

    def use_educational_tech_vs_final_grade(self):
        ax = sns.countplot(data=self.df, x='Final_Grade', hue='Use_of_Educational_Tech', order=['A', 'B', 'C', 'D'])
        plt.title('Visualizing Edtech Students with Final Grade', weight='bold', fontsize=13)
        for container in ax.containers:
            ax.bar_label(container)
        plt.show()

    def stress_report_vs_final_grade(self):
        ax = sns.catplot(x=self.df['Final_Grade'], hue=self.df['Self_Reported_Stress_Level'], order=['A', 'B', 'C', 'D'], kind='count')
        plt.title('Visualizing Number of Students with Final Grade', weight='bold', fontsize=13)
        plt.ylabel('Number of Students')
        for container in ax.ax.containers:
            ax.ax.bar_label(container)

        plt.tight_layout()
        plt.show()

    def free_time_vs_final_grade(self):
        sns.displot(self.df, x="Free_Time (hours/week)", hue="Final_Grade", kind="kde", hue_order=['A', 'B', 'C', 'D'])
        plt.title("Comparison of Free Time (hours/week) by Grade")
        plt.show()

    def sleep_vs_final_grade(self):
        sns.displot(self.df, x="Sleep_Hours_per_Night", hue="Final_Grade", kind="kde", hue_order=['A', 'B', 'C', 'D'])
        plt.title("Comparison of Sleep Hours per Night by Grade")
        plt.show()

class StudentPerformanceAnalyze(StudentPerformanceVisualize):
    def __init__(self, df):
        super().__init__(df)