import pandas as pd


def std():
    # TODO: Figure out how to make sure that this file uses the directory of the script location
    # so that it is more portable
    df = pd.read_csv(r'./input/Dataframe1.csv')
    df = df.drop(['0','1','2','3','4','5','6','7'], axis = 1)
    df_t = df.T
    std_dev = df_t.std()
    print(df)
    print(std_dev)

    return std_dev
std()
