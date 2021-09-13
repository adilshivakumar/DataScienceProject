import pandas as pd


def std():
    # TODO: Figure out how to make sure that this file uses the directory of the script location
    # so that it is more portable
    df = pd.read_csv(r'./input/Dataframe1.csv')
    df2 = pd.read_csv(r'./input/Dataframe2b.csv')
    df_saved = df.drop(['0','1','2','3','4','5','6','7'], axis = 1)
    df_saved = df_saved.T
    df_2a = df['-1'] - df['-30']
    std_dev = df_saved.std()
    print(df)
    print(std_dev)
    print(df2)
    print(df_2a)

    return std_dev
std()
