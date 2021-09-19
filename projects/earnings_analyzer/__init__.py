import pandas as pd


def std():
    # TODO: Figure out how to make sure that this file uses the directory of the script location
    # so that it is more portable
    df = pd.read_csv(r'./input/Dataframe1.csv')
    df_step = df.T
    df2 = pd.read_csv(r'./input/Dataframe2b.csv')
    df_3 = pd.read_csv(r'./input/Dataframe3b/Dataframe3b.csv')
    df_4a = pd.read_csv(r'./input/Dataframe4/Dataframe4a.csv')
    df_4b = pd.read_csv(r'./input/Dataframe4/Dataframe4b/Dataframe4b.csv')
    df_5b = pd.read_csv(r'./input/Dataframe5b.csv')
    df_6b = pd.read_csv(r'./input/Dataframe6b.csv')
    df_saved = df.drop(['0','1','2','3','4','5','6','7'], axis = 1)
    df_saved = df_saved.T
    std_dev = df_saved.std()
    df_2a = (df_step.iloc[30] - df_step)/std_dev
    df_3a = (df_step.iloc[30] - df_step)*100
    df_5a = ((df_step.iloc[30] - df_step)/(df_step))*100
    df_5a_final = df_5a.round(2).astype(str) + '%'
    df_3a_final = df_3a.T 
    df_3a_saved = df_3a_final.drop(['0','1','2','3','4','5','6','7'], axis = 1)
    print(df)
    print(std_dev)
    print(df2)
    print(df_2a)
    print(df_3)
    print(df_3a_saved)
    print(df_4a)
    print(df_4b)
    print(df_5a_final)
    print(df_5b)
    print(df_6b)
    
    return std_dev
std()
