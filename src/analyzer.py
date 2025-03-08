import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class StudentPerformanceAnalyze:
    def __init__(self, df):
        self.__df = df

    @property
    def df(self):
        return self.__df
    
    def stress_report_vs_final_grade(self):
        ax = sns.catplot(x=self.df['Final_Grade'], hue=self.df['Self_Reported_Stress_Level'], order=['A', 'B', 'C', 'D'], kind='count')
        plt.title('Visualizing Number of Students with Final Grade', weight='bold', fontsize=13)
        plt.ylabel('Number of Students')
        for container in ax.ax.containers:
            ax.ax.bar_label(container)

        plt.tight_layout()
        plt.show()

        # df_count = self.df.groupby('Final_Grade')['Self_Reported_Stress_Level'].value_counts().reset_index(name='Count')
        # pivot_table = df_count.pivot_table(index='Final_Grade', columns='Self_Reported_Stress_Level', values='Count', fill_value=0)

        # print(f"According the chart, Students with high stress are consistently fewer across all grades, suggesting that extreme stress may be less common or that students under high stress struggle academically")

    # def 