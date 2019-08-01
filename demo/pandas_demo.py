import numpy as np
import pandas as pd


def exercise():
    data = pd.read_csv('../src/data/Consumer_Complaints.csv')

    # Create a new DataFrame with only the 'Abbrev' and 'Population' columns
    states = pd.read_csv('../src/data/states.csv')
    states = states[['Abbrev', 'Population']]
    states.columns = ['State', 'Population']

    # merge the data and states
    data = pd.merge(data, states, on='State')

    # Generate a new DataFrame that contains the number of
    # complaints per state and keeps track of those counts
    by_state = pd.DataFrame(data['State'].value_counts().reset_index())
    by_state.columns = 'State Count'.split()

    # We need to group by State, which will produce and then count the
    # number of complaints per state, which we can do with the size()
    # method. We can use the reset_index() method to give a reasonable
    # name to the column that was produced.
    complaints_by_state = data.groupby(['State']).size().reset_index()

    merged = pd.merge(by_state, states, on='State').dropna()
    return merged


print(exercise())
