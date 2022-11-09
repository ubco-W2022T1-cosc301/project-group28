import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re
import project_functions1 as pf1


def remove_def(df):
    """Function that removes "SUB","RES","NA" to clean the data to make it more workable"""
    df = pd.Dataframe(df)
    df.drop(df[df['Position'] == 'SUB'].index, inplace = True)
    df.drop(df[df['Position'] == 'RES'].index, inplace = True)
    df.drop(df[df['Position'] == 'NA'].index, inplace = True)
    return df


  