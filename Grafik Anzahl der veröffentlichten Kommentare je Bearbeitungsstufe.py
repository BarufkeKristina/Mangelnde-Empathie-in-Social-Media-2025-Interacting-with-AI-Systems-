import matplotlib.pyplot as plt
import pandas as pd


file_path = r"Auswertung - Tabellenblatt1.csv"
data = pd.read_csv(file_path)


print(data.head())


veroeffentlichte_daten = data[data['Veröffentlichungsentscheidung (Ja/Nein)'] == 'Ja']


bearbeitung_counts = veroeffentlichte_daten['Kommentar_Typ (Original/Bearbeitet)'].value_counts()


print("Anzahl der veröffentlichten Kommentare je Bearbeitungsstufe:")
print(bearbeitung_counts)

#Balkendiagramm
plt.figure(figsize=(8, 6))
bearbeitung_counts.plot(kind='bar', color=['skyblue', 'orange', 'green', 'lightcoral'])

plt.title('Anzahl der veröffentlichten Kommentare je Bearbeitungsstufe')
plt.xlabel('Bearbeitungsstufe')
plt.ylabel('Anzahl veröffentlichter Kommentare')
plt.xticks(rotation=45)
plt.show()
