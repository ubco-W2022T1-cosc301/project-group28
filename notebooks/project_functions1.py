import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re

def convert_with_text_to_number(value):
    '''Converts values with text and currency logo from a string with currency logo and short form for million and kilo to only numbers'''
    try:
        if "€" in value:
            value = str(value).strip('€')
            if "M" in value:
                value = re.sub("[^0-9]", "", value)
                value = float(value)*1000000
            elif "K" in value: 
                value = re.sub("[^0-9]", "", value)
                value = float(value)*1000
        else:
            value = ''.join([i for i in value if i.isdigit()])
    except TypeError:
        value = 0
    return(float(value))


def clean_position(pos):
    """Function to clean the position column of the data set to extract important information"""
    if isinstance(pos, str) == False:
        pos_cleaned = "NA"
    else:
        pos_cleaned = ''.join([a for a in pos if a.isupper()])
    return pos_cleaned

def clean_name(name):
    name_cleaned = ''.join(map(lambda c: '' if c in '0123456789' else c, name)).strip()
    return name_cleaned

def get_cleaned_data(location):
    """Function to clean the data to make it more workable"""
    df = pd.read_csv(location)

    df_cleaned = (df
      .drop(["Photo", "Flag", "Club Logo", "Potential", "Special", "Work Rate", "Marking", "Best Position", "Best Overall Rating","DefensiveAwareness", "Real Face" ], axis = 1)
      .rename(columns = {'Weekly Wage':'Wage', "FKAccuracy" : "Freekick Accuracy", "Loaned From" : "LoanedFrom"})
      .sort_values("Name", ascending=True)
      .assign(OnLoan=lambda x: np.where(x.LoanedFrom.notnull, "No", "Yes"))
     )

    df_cleaned['Value'] = df_cleaned['Value'].map(lambda x: convert_with_text_to_number(x))
    df_cleaned['Wage'] = df_cleaned['Wage'].map(lambda x: convert_with_text_to_number(x))
    df_cleaned['Release Clause'] = df_cleaned['Release Clause'].map(lambda x: convert_with_text_to_number(x))
    df_cleaned['Position'] = df_cleaned['Position'].map(lambda x: clean_position(x))
    df_cleaned['Name'] = df_cleaned['Name'].map(lambda x: clean_name(x))
    df_cleaned['Weight'] = df_cleaned['Weight'].map(lambda x: convert_with_text_to_number(x))
    df_cleaned['Height'] = df_cleaned['Height'].map(lambda x: convert_with_text_to_number(x))

    return df_cleaned
  