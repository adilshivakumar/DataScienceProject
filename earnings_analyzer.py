import pandas as pd

# TODO: Figure out how to make sure that this file uses the directory of the script location
# so that it is more portable
df = pd.read_csv (r'./input/Dataframe1.csv')
print(df)


