import pandas as pd 
import requests as r
import json
import matplotlib.pyplot as plt

ocm = r.get('https://api.openchargemap.io/v3/poi/?output=json&countrycode=NL&maxresults=100000&compact=true&verbose=false&key=93b912b5-9d70-4b1f-960b-fb80a4c9c017')
df_ocm = pd.DataFrame(json.loads(ocm.text))

def get_charger_type(connections):
        ac = False
        dc = False
        for connection in connections:
            currentId = connection.get('CurrentTypeID')
            if currentId is not None:
                if currentId < 30:
                    ac = True
                elif currentId == 30:
                    dc = True
                if ac and dc:
                    return 'AC/DC'
        if ac:
            return 'AC'
        elif dc:
            return 'DC'
        return 'AC'

df_ocm['Type'] = df_ocm['Connections'].apply(get_charger_type)

print()

print(df_ocm['Type'].info())
print(df_ocm['Type'].value_counts())