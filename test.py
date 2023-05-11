# test file to look at the data and see how to use it
import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sns
import os

absolute_path = absolute_path = os.path.abspath("")

hs1104df = pd.read_csv(absolute_path + "\HS1104.csv")
hs1104df["Time Difference"] = pd.to_datetime(hs1104df["Time Difference"])
hs1104df