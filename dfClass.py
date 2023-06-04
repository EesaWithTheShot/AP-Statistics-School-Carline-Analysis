import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime
import os

class DataframeDay:
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
            self.release_time = "3:15"
        else:
            self.grade_level = "Elementary School"
            self.release_time = "2:00"
        

    def clean(self):
        self.df["Time In"] = pd.to_datetime(self.df["Time In"])
        self.df["Time Out"] = pd.to_datetime(self.df["Time Out"])
        self.df["Difference"] = self.df["Time Out"] - self.df["Time In"]
        for index, row in self.df.iterrows():
            if (row["Difference"].total_seconds()/60) > 300:
                self.df.drop(index, inplace=True)
        self.df["Diff Mins"] = self.df["Diff Mins"].astype(int)
        self.df["Diff Release"] = self.df["Diff Release"].astype(int)                
    
    def scatter_release_timediff(self):
        '''Plots a scatter plot relating the time difference of entering from the release time to the Time difference from time in time out.'''
        fig, ax = plt.subplots()
        plot = sns.scatterplot(data=self.df,
                        x="Diff Release", y="Diff Mins", hue="Grade", palette=self.cmrpalette,s=100)
        fig.suptitle(f"{self.grade_level} {self.date.strftime(r'%A %B %d, %Y')} ",fontsize="48")
        plt.legend(fontsize="30")
        plt.xlabel(f"Time from release at {self.release_time} (minutes)",fontsize="30")
        plt.ylabel(f"Time spent in school (minutes)",fontsize="30")
        plt.show()

    def scatter_in_timediff(self):
        '''Plots a scatter plot relating the ACTUAL time of entering from the release time to the Time difference from time in time out.'''
        fig, ax = plt.subplots()
        plot = sns.scatterplot(data=self.df,
                        x="Time In", y="Diff Mins", hue="Grade", palette=self.cmrpalette,s=100)
        fig.suptitle(f"{self.grade_level} {self.date.strftime(r'%A %B %d, %Y')} ",fontsize="48")
        plt.legend(fontsize="30")
        plt.xlabel(f"Time Arrived",fontsize="30")
        plt.ylabel(f"Time spent in school (minutes)",fontsize="30")
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%I:%M'))
        plt.tick_params(axis='both', which='major', labelsize=24)
        plt.show()


    def lmplot_release_timediff(self):
        '''Plots a scatter plot (with LSRL) relating the time difference of entering from the release time to the Time difference from time in time out.'''
        fig, ax = plt.subplots()
        plot = sns.lmplot(data=self.df,
                        x="Diff Release", y="Diff Mins", palette=self.cmrpalette)
        plt.title(f"{self.grade_level} {self.date.strftime(r'%A %B %d, %Y')} ",fontsize="36")
        plt.legend(fontsize="30")
        plt.xlabel(f"Time from release at {self.release_time} (minutes)",fontsize="30")
        plt.ylabel(f"Time spent in school (minutes)",fontsize="30")
        plt.show()

    def scatter_out_timediff(self):
        '''Plots a scatter plot relating the ACTUAL time of exit to the Time difference from time in time out.'''
        fig, ax = plt.subplots()
        plot = sns.scatterplot(data=self.df,
                        x="Time Out", y="Diff Mins", hue="Grade", palette=self.cmrpalette,s=100)
        fig.suptitle(f"{self.grade_level} {self.date.strftime(r'%A %B %d, %Y')} ",fontsize="48")
        plt.legend(fontsize="30")
        plt.xlabel(f"Time Exited",fontsize="30")
        plt.ylabel(f"Time spent in school (minutes)",fontsize="30")
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%I:%M'))
        plt.tick_params(axis='both', which='major', labelsize=24)
        plt.show()

    @staticmethod
    def oneDayScatter(df1, df2, df3):
        '''Creates a plot of all the grade levels from one singular day'''
        DFs = [df1.df,df2.df,df3.df]
        maindf = pd.concat(DFs)
        fig, ax = plt.subplots()
        plot = sns.scatterplot(data=maindf,
                        x="Time In", y="Diff Mins", hue="Level",s=100)
        fig.suptitle(f"All Levels {df1.date.strftime(r'%A %B %d, %Y')} ",fontsize="48")
        plt.legend(fontsize="30")
        plt.xlabel(f"Time Arrrived",fontsize="30")
        plt.ylabel(f"Time spent in school (minutes)",fontsize="30")
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%I:%M'))
        plt.tick_params(axis='both', which='major', labelsize=24)
        plt.show()



    def showData(self):
        return self.df
    def __str__(self):
        return f"{self.date} + {self.grade_level}"


# absolute_path = os.path.abspath("")

# TESThs1104df = pd.read_csv(absolute_path + "\maintestHS1104v2.csv")
# data = DataframeDay("HS","11-4-2022",TESThs1104df)
# print(data)
# print(data.scatter_in_timediff())

