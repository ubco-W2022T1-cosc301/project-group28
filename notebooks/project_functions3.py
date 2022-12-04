import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re
import project_functions1 as pf1
import project_functions2 as pf2

def remove_def(df):
    #Function that removes "SUB","RES","NA" to clean the data to make it more workable
    df = pd.DataFrame(df)
    df.drop(df[df['Position'] == 'SUB'].index, inplace = True)
    df.drop(df[df['Position'] == 'RES'].index, inplace = True)
    df.drop(df[df['Position'] == 'NA'].index, inplace = True)
    return df

def remove_exs(df):
    # Removes excess columns and returns a workable pandas dataframe.
    
    df = df.copy().drop(['ID', 'Name', 'Club', 'Value', 'Wage',
       'Preferred Foot', 'International Reputation', 'Weak Foot',
       'Skill Moves', 'Body Type', 'Jersey Number', 'Joined',
       'Contract Valid Until', 'Height', 'Weight', 'GKDiving',
       'GKHandling', 'GKKicking', 'GKPositioning', 'GKReflexes',
       'Release Clause','LoanedFrom','OnLoan'], axis=1)

    df.nunique(axis=0)
    df.describe().apply(lambda s: s.apply(lambda x: format(x,'f')))
    df.columns.unique()
    # Calls custom function clean_position()
    df['Position'] = df['Position'].map(lambda x: pf1.clean_position(x))

    return df


