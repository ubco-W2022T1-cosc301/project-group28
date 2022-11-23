import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re
import project_functions1 as pf1


def remove_def(df):
    #Function that removes "SUB","RES","NA" to clean the data to make it more workable
    df = pd.Dataframe(df)
    df.drop(df[df['Position'] == 'SUB'].index, inplace = True)
    df.drop(df[df['Position'] == 'RES'].index, inplace = True)
    df.drop(df[df['Position'] == 'NA'].index, inplace = True)
    return df

def arrange_pos(df):
    for i in range(len(df)):
        attackers = ['ST','CF','RW','LW','RF','LF','LS','RS']
        pattern1 = '|'.join(attackers)
        midfielders = ['RM','LM','CAM','CM','CDM','LAM','RAM','CDM','LDM','RDM','RCM','LCM']
        pattern2 = '|'.join(midfielders)
        defenders = ['CB','LCB','RCB','LB','RB','LWB','RWB']
        pattern3 = '|'.join(defenders)
        
        if   df.Position[i].str.contains(pattern1):
                df["General Position"][i]=="Attacker"
        elif df.Position[i].str.contains(pattern2):
                df["General Position"][i]=="Midfielder"
        elif df.Position[i].str.contains(pattern3):
                df["General Position"][i]=="Defender"
        elif df.Position[i].str.contains(['GK']):
                df["General Position"][i]=="Goalkeeper"
        else:
                df["General Position"][i]=="Not Playing"
        return df

   # mylist = ['ST','CF','RW','LW','RF','LF','LS','RS']
#pattern = '|'.join(mylist)

#pattern
#'dog|cat|fish'

#frame.a.str.contains(pattern)
#def arrange_attribute(df) pace shooting defending dribbling passingphysical
