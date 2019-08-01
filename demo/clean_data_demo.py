import pandas as pd
import numpy as np
import re


def exercise():
    """
    Goal: Read in a "dirty" data file and clean it up
    known problems with the data
    typos
    missing data
    incorrect formatting
    """
    # read data
    data = pd.read_csv('../src/data/WA_Fn-UseC_-Sales-Win-Loss-DIRTY.csv')
    print(data.head())
    print(data.columns)
    # remove anything that doesn't look right
    data = data.drop('Unnamed: 0', 1)
    data = data.drop('Opportunity Next Step', axis=1)

    # find typos for textual fields
    data['Supplies Group'].value_counts()

    # This replace all columns fields that can match the pattern
    # data = data.replace('.*r A.*', 'Car Accessories', regex=True)
    # data = data.replace('^P.*', 'Performance & Non-auto', regex=True)

    # only update the required column
    data['Supplies Group'] = data['Supplies Group'].apply(lambda s: re.sub('.*r A.*', 'Car Accessories', s))
    data['Supplies Group'] = data['Supplies Group'].apply(lambda s: re.sub('^P.*', 'Performance & Non-auto', s))
    data['Supplies Group'].value_counts()

    # handle missing data
    # it's ok to drop some nan data
    # but if the missing fields are a lot, probably we need to replace with some usefual data
    print(data['Region'].isnull().sum())
    data = data.dropna(subset=['Region'])
    print(data['Supplies Subgroup'].isnull().sum())
    data = data.replace(np.nan, 'Motorcycle Parts', regex=True)
    print(data['Supplies Subgroup'].value_counts())
    data['Supplies Subgroup'].isnull().sum()

    # Formatting errors
    print(data["Opportunity Amount USD"].value_counts())
    data['Opportunity Amount USD'] = data[
        'Opportunity Amount USD'].apply(lambda s: int(s.replace('$', '')))

    # write to csv file
    # data.to_csv('data/WA_Fn-UseC_-Sales-Win-Loss-CLEAN.csv')
