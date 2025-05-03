# import libraries
import requests
import os
import pandas as pd

API_URI = "https://ghoapi.azureedge.net/api/"

# Define function to query WHO GDO, returns pandas dataframe
def query_who(query, API_URI=API_URI):

    # make request
    response = requests.get(f"{API_URI}{query}")
    
    # print status code
    print(f"Response: {response.status_code}")
    
    # create jsob
    response_json = response.json()

    # select value from response_json
    data = response_json['value']
    
    # create dataframe
    df = pd.DataFrame(data)

    # return dataframe
    return df

# Define a global variable to store the dimensions_df DataFrame
_dimensions_df = None

def list_dimensions(refresh=False):
    # Retrieve global variable
    global _dimensions_df

    # Query WHO if variable is none or refresh = True
    if _dimensions_df is None or refresh:
        _dimensions_df = query_who("Dimension")
    return _dimensions_df

# Define global variable
_indicators_df = None

def list_indicators(refresh=False, contains=None):
    # Retrieve global
    global _indicators_df

    if '_indicators_df' not in globals():
        _indicators_df = None

    if _indicators_df is None or refresh:
        _indicators_df = query_who("Indicator")

    if isinstance(contains, str):
        mask = _indicators_df['IndicatorName'].str.contains(contains, case=False, na=False)
        filtered_df = _indicators_df[mask]
        return filtered_df
    else:
        return _indicators_df
