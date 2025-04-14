import pandas as pd
import pingouin as pg

#file_path bei allen Dateien zum jeweiligen Filepath anpassen
file_path = r"Auswertung - Tabellenblatt1.csv"
data = pd.read_csv(file_path)

data.rename(columns={'Veröffentlichungsentscheidung (Ja/Nein)': 'Veroeffentlichung',
                     'Empathiebewertung (Likert 1-5) 1= Sehr Unempatisch 5= Sehr Empatisch': 'Empathie'}, inplace=True)


data = data.dropna(subset=['Veroeffentlichung', 'Empathie'])


data['Veroeffentlichung'] = data['Veroeffentlichung'].map({'Ja': 1, 'Nein': 0})
data['Empathie'] = data['Empathie'].astype(int)

#ANOVA
aov = pg.anova(dv='Veroeffentlichung', between='Empathie', data=data, detailed=True)
print(aov)
