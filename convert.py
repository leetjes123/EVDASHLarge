import pandas as pd

kentekens = pd.read_csv('kentekens.csv',
                        usecols=['Kenteken','Europese voertuigcategorie','Merk','Datum eerste tenaamstelling in Nederland','Catalogusprijs','Type','Variant','Uitvoering','Bruto BPM'])
kentekens=kentekens.rename(columns={
    'Kenteken': 'kenteken',
    'Europese voertuigcategorie': 'europese_voertuigcategorie',
    'Merk': 'merk',
    'Datum eerste tenaamstelling in Nederland': 'datum_eerste_tenaamstelling_in_nederland',
    'Catalogusprijs': 'catalogusprijs',
    'Type': 'type',
    'Variant': 'variant',
    'Uitvoering': 'uitvoering',
    'Bruto BPM': 'bruto_bpm'
})
kentekens = kentekens[kentekens['europese_voertuigcategorie'] == 'M1']
kentekens_brandstof = pd.read_csv('kentekens_brandstof.csv',
                                  usecols=['Klasse hybride elektrisch voertuig', 'Kenteken', 'Brandstof omschrijving', 'Emissie co2 gecombineerd wltp'])
kentekens_brandstof = kentekens_brandstof.rename(columns={
    'Klasse hybride elektrisch voertuig': 'klasse_hybride_elektrisch_voertuig',
    'Kenteken': 'kenteken',
    'Brandstof omschrijving': 'brandstof_omschrijving',
    'Emissie co2 gecombineerd wltp': 'emissie_co2_gecombineerd_wltp'
})
print('Done importing kentekens.csv and kentekens_brandstof.csv')
#cars = pd.read_pickle('cars.pkl')
print('Done importing cars.pkl')

print(kentekens_brandstof.head())


#cars_keep = ['catalogusprijs', 'kenteken', 'datum_eerste_tenaamstelling_in_nederland','merk','uitvoering','variant','type','datum_tenaamstelling_dt','bruto_bpm']

#cars = cars[cars_keep]

rdw = kentekens.merge(kentekens_brandstof, on='kenteken', how='inner')

print(rdw.columns)
print(rdw.head())

rdw.to_csv('rdw.csv')