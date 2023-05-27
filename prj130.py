import pandas as pd
import csv

df = pd.read_csv("cleaned_brown_dwarf_stars.csv")
print(df.shape)

del df["Unnamed: 0"]
print(df.shape)

df.to_csv("final.csv")