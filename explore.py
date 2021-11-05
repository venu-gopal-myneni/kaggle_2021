import pandas as pd
from pprint import pprint as print
df = pd.read_csv("../data/kaggle_survey_2021_responses.csv")
# print(df.loc[0].tolist())
print(df["Q4"].describe)
print(df["Q4"].value_counts())