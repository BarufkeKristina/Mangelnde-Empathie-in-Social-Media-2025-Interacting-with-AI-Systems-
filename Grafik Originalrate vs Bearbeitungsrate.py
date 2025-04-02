import matplotlib.pyplot as plt
import pandas as pd



file_path = r"Auswertung - Tabellenblatt1.csv"
data = pd.read_csv(file_path)


data.columns = [col.strip() for col in data.columns]
data['Veröffentlichungsentscheidung (Ja/Nein)'] = data['Veröffentlichungsentscheidung (Ja/Nein)'].map({'Ja': 1, 'Nein': 0})

original = data[data['Kommentar_Typ (Original/Bearbeitet)'] == 'Original']
bearbeitet = data[data['Kommentar_Typ (Original/Bearbeitet)'].str.contains('Bearbeitet', na=False)]

# durchschnittliche Veröffentlichungsrate
original_rate = original['Veröffentlichungsentscheidung (Ja/Nein)'].mean()
bearbeitet_rate = bearbeitet['Veröffentlichungsentscheidung (Ja/Nein)'].mean()


diff = bearbeitet_rate - original_rate
print(f"Veröffentlichungsrate Originale: {original_rate:.2%}")
print(f"Veröffentlichungsrate Bearbeitete: {bearbeitet_rate:.2%}")
print(f"Differenz: {diff:.2%}")


categories = ['Originale', 'Bearbeitete']
rates = [original_rate, bearbeitet_rate]
plt.figure(figsize=(8, 6))
plt.bar(categories, rates, color=['blue', 'orange'])
plt.ylabel('Veröffentlichungsrate')
plt.title('Vergleich der Veröffentlichungsraten (Original vs. Bearbeitet)')
plt.ylim(0, 1)


for i, rate in enumerate(rates):
    plt.text(i, rate + 0.02, f'{rate:.2%}', ha='center', va='bottom', fontsize=12)

plt.show()
