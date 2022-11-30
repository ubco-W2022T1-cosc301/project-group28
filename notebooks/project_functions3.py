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


'''def arrange_pos(df):
    attackers = ['ST','CF','RW','LW','RF','LF','LS','RS']
    pattern1 = '|'.join(attackers)
    midfielders = ['RM','LM','CAM','CM','CDM','LAM','RAM','CDM','LDM','RDM','RCM','LCM']
    pattern2 = '|'.join(midfielders)
    defenders = ['CB','LCB','RCB','LB','RB','LWB','RWB']
    pattern3 = '|'.join(defenders)

    GenPosition = []

    for i in range(len(df)df):
        if   str(df.Position[i]) in attackers:
                GenPosition.append("Attacker")
        elif str(df.Position[i]) in midfielders:
                GenPosition.append("Midfielder")
        elif str(df.Position[i]) in defenders:
                GenPosition.append("Defender")
        elif str(df.Position[i]) in (['GK']):
                GenPosition.append("Goalkeeper")
        else:
                GenPosition.append("Not Playing")
        

    print(len(GenPosition))
    df['GenPosition'] = GenPosition
    return df

#def arrange_attribute(df) pace shooting defending dribbling passingphysical'''
