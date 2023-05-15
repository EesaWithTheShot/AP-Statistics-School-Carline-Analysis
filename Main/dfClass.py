import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import datetime
import os

class dfDay:
    def __init__(self, grade_level, date, df):
        self.df = df
        self.date = datetime.datetime.strptime(date, '%m-%d-%Y').date()
        self.redpalette = sns.color_palette("rocket_r")
        self.cmrpalette = sns.color_palette("CMRmap")
        sns.set_theme(style="darkgrid")
        self.clean()
        if(grade_level=="HS"):
            self.grade_level = "High School"
            self.release_time = "3:15"
        elif(grade_level=="MS"):
            self.grade_level = "Middle School"
            self.release_time = "IDK"
        else:
            self.grade_level = "Elementary School"
            self.release_time = "IDK"
        

    def clean(self):
        self.df["Time In"] = pd.to_datetime(self.df["Time In"])
        self.df["Time Out"] = pd.to_datetime(self.df["Time Out"])
        self.df["Difference"] = self.df["Time Out"] - self.df["Time In"]
        for index, row in hs1104df.iterrows():
            if (row["Difference"].total_seconds()/60) > 300:
                self.df.drop(index, inplace=True)
        self.df["Diff Mins"] = self.df["Diff Mins"].astype(int)
        self.df["Time release"] = self.df["Time release"].astype(int)                
    
    def scatter_release_timediff(self):
        '''Plots a scatter plot relating the time difference of entering from the release time to the Time difference from time in time out.'''
        fig, ax = plt.subplots()
        plot = sns.scatterplot(data=self.df,
                        x="Time release", y="Diff Mins", hue="Grade", palette=self.cmrpalette,s=70)
        fig.suptitle(f"{self.grade_level} {self.date.strftime(r'%A %B %d, %Y')} ",fontsize="48")
        plt.legend(fontsize="30")
        plt.xlabel(f"Time from release at {self.release_time} (minutes)",fontsize="30")
        plt.ylabel(f"Time spent in school (minutes)",fontsize="30")
        plt.show()
        

    def showData(self):
        return self.df
    def __str__(self):
        return f"{self.date} + {self.grade_level}"


absolute_path = os.path.abspath("")
hs1104df = pd.read_csv(absolute_path + "\cleanerHS1104.csv")
data = dfDay("HS","11-4-2022",hs1104df)
print(data)
print(data.scatter_release_timediff())
