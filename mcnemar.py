import pandas as pd
from statsmodels.stats.contingency_tables import mcnemar


file_path = r"Auswertung - Tabellenblatt1.csv"
data = pd.read_csv(file_path)

data.columns = [col.strip() for col in data.columns]

#(Ja=1, Nein=0)
data['Veröffentlichungsentscheidung (Ja/Nein)'] = data['Veröffentlichungsentscheidung (Ja/Nein)'].map({'Ja': 1, 'Nein': 0})


original = data[data['Kommentar_Typ (Original/Bearbeitet)'] == 'Original']
bearbeitet = data[data['Kommentar_Typ (Original/Bearbeitet)'].str.contains('Bearbeitet', na=False)]

table = [[
    sum((original['Veröffentlichungsentscheidung (Ja/Nein)'] == 1) & (bearbeitet.groupby('Kommentar_ID')['Veröffentlichungsentscheidung (Ja/Nein)'].max() == 1)),  # Ja → Ja
    sum((original['Veröffentlichungsentscheidung (Ja/Nein)'] == 1) & (bearbeitet.groupby('Kommentar_ID')['Veröffentlichungsentscheidung (Ja/Nein)'].max() == 0))   # Ja → Nein
], [
    sum((original['Veröffentlichungsentscheidung (Ja/Nein)'] == 0) & (bearbeitet.groupby('Kommentar_ID')['Veröffentlichungsentscheidung (Ja/Nein)'].max() == 1)),  # Nein → Ja
    sum((original['Veröffentlichungsentscheidung (Ja/Nein)'] == 0) & (bearbeitet.groupby('Kommentar_ID')['Veröffentlichungsentscheidung (Ja/Nein)'].max() == 0))   # Nein → Nein
]]

result = mcnemar(table, exact=True)

print("McNemar-Test Ergebnis:")
print(f"p-Wert: {result.pvalue}")

