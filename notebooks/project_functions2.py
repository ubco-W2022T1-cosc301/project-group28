import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re
import project_functions1 as pf1

# Cleaning method
def df_clean(df):
    '''
    Removes excess columns that have no meaning to the research question and gives meaningful
    values to the Position column of the data. Returns an edited pandas dataframe.
    '''
    df = df.copy().drop(['Best Position', 'Height', 'Weight', 'Aggression', 'Jersey Number', 'GKDiving', 'GKHandling', 'GKKicking', 'GKPositioning', 'GKReflexes', 'Special', 'Skill Moves', 'International Reputation', 'Potential', 'Marking', 'Vision', 'Curve', 'Balance', 'Jumping', 'Reactions', 'Agility', 'Composure', 'Volleys', 'HeadingAccuracy', 'Weak Foot', 'ID', 'FKAccuracy', 'Release Clause', 'Preferred Foot', 'Photo', 'Nationality', 'Flag', 'Club Logo', 'Value', 'Wage', 'Work Rate', 'Body Type', 'Real Face', 'Joined', 'Loaned From', 'Contract Valid Until', 'Finishing'], axis=1)

    df.nunique(axis=0)
    df.describe().apply(lambda s: s.apply(lambda x: format(x,'f')))

    df.columns.unique()
    # Calls custom function clean_position()
    df['Position'] = df['Position'].map(lambda x: pf1.clean_position(x))

    return df

def clean_position(pos):
    """Function to clean the position column of the data set to extract important information"""
    if isinstance(pos, str) == False:
        pos_cleaned = "NA"
    else:
        pos_cleaned = ''.join([a for a in pos if a.isupper()])
    return pos_cleaned