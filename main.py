import dfClass as dfcl
import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime

absolute_path = os.path.abspath("")

#importing all the data
hs1104df = pd.read_csv(absolute_path + "\Data\HS_11-04-2022.csv")
hs1102df = pd.read_csv(absolute_path + "\Data\HS_11-02-2022.csv")
ms1104df = pd.read_csv(absolute_path + "\Data\MS_11-04-2022.csv")
ms1102df = pd.read_csv(absolute_path + "\Data\MS_11-02-2022.csv")
es1104df = pd.read_csv(absolute_path + "\Data\ES_11-04-2022.csv")
es1102df = pd.read_csv(absolute_path + "\Data\ES_11-02-2022.csv")

# defining all the objects for all entries
hs11_04_2022 = dfcl.DataframeDay("HS", "11-4-2022",hs1104df)
hs11_02_2022 = dfcl.DataframeDay("HS", "11-2-2022",hs1102df)

ms11_04_2022 = dfcl.DataframeDay("MS", "11-4-2022",ms1104df)
ms11_02_2022 = dfcl.DataframeDay("MS", "11-2-2022",ms1102df)

es11_04_2022 = dfcl.DataframeDay("ES", "11-4-2022",es1104df)
es11_02_2022 = dfcl.DataframeDay("ES", "11-2-2022",es1102df)

