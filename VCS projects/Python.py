import os
os.system('clear')
import matplotlib.pyplot as plt
import seaborn as sns

from csv import DictReader

baze=[]
miestai=[]
saltiniai=[]
atlyginimai=[]
atlyginimai1=[]
atlyginimai2=[]
atlyginimai3=[]
with open('2018.csv', encoding='utf8') as failas:
    csv_reader = DictReader(failas)
    for row in csv_reader:
        baze.append(row)
        
        if row['Miestas']=='Vilniuje' or row['Miestas']=='Vinius' or ('Viln' in row['Miestas']):
            row['Miestas']='Vilnius'

        if ('Kaun' in row['Miestas']):
            row['Miestas']='Kaunas'
        
        miestai.append(row['Miestas'].lower().capitalize())
        saltiniai.append(row['Šaltinis'])
        atlyginimai.append(int(row['Atlyginimas']))
        
        if row['lygis']=='1':
            atlyginimai1.append(int(row['Atlyginimas']))
        elif row['lygis']=='2':
            atlyginimai2.append(int(row['Atlyginimas']))
        else:
            atlyginimai3.append(int(row['Atlyginimas']))


failas.close
#isimti tarpus    
while  " " in miestai:
    miestai.remove(" ")

#Atrinkite visas skirtingas programavimo kalbas su kuo dirba žmonės.
print()
print(f'Programavimo kalbos:')
for saltinis in set(saltiniai):
    print(saltinis)

# - Atrinkite visus skirtingus miestus iš kurių yra šie respondentai.
print()
print(f'Miestai iš kurių yra respondentai:')
for miestas in set(miestai):
    print(miestas)

# - Raskite didžiausią ir mažiausią įvestus atlyginimus.
print()
print(f'Didžiausias ir mažiausias įvesti atlyginimai.:')
print(f'- maksimalus atlyginimas={max(atlyginimai)};')
print(f'- minimalus atlyginimas={min(atlyginimai)}.')

# - Raskite atlyginimų vidurkį.
print()
print(f'Atlyginimų vidurkis: {round(sum(atlyginimai)/len(atlyginimai),2)} eur.')

# - Raskite atlyginimų vidurkius pagal lygį (1 - junior, 2 - mid, 3 - senior).
print()
print(f'Atlyinimų vidurkiai pagal lygį.')
print(f'Atlyginimų vidurkis (JUNIOR): {round(sum(atlyginimai1)/len(atlyginimai1),2)} eur.')
print(f'Atlyginimų vidurkis (MID): {round(sum(atlyginimai2)/len(atlyginimai2),2)} eur.')
print(f'Atlyginimų vidurkis (SENIOR): {round(sum(atlyginimai3)/len(atlyginimai3),2)} eur.')
print()

#Grafikas
with open('2018.csv', encoding='utf8') as failas:
    csv_reader = DictReader(failas)
dictionary={'junior':round(sum(atlyginimai1)/len(atlyginimai1),2), 'mid':round(sum(atlyginimai2)/len(atlyginimai2),2), 'senior':round(sum(atlyginimai3)/len(atlyginimai3),2)}

#be seaborn
# xAxis = [key for key, value in dictionary.items()]
# yAxis = [value for key, value in dictionary.items()]
#plt.bar(xAxis,yAxis, color=['blue','red','yellow'],data=dictionary)
plt.figure(figsize=(8, 8))

plot=sns.barplot(x=[key for key, value in dictionary.items()],y=[value for key, value in dictionary.items()])

for bar in plot.patches:
    plot.annotate(format(bar.get_height(), '.2f'), (bar.get_x() + bar.get_width() / 2, bar.get_height()), ha = 'center', va = 'center', 
                   size=12,xytext = (0, 8), 
                   textcoords = 'offset points')

plt.xlabel('STATUSAS',size=12)
plt.ylabel('VIDURKIS(EUR)',size=12)
plt.title('ATLYGINIMŲ VIDURKIAI PAGAL LYGĮ')
plt.show()

print()
print('testas',list(set(saltiniai)))
#Gautus atsakymus išveskite į txt failiuką.
with open('2018.txt', 'a', encoding="utf8") as failas:
    #Atrinkite visas skirtingas programavimo kalbas su kuo dirba žmonės.
    failas.write('Programavimo kalbos:\n')
    failas.write('-------------------\n')
    saltiniai=list(set(saltiniai))
    for saltinis in saltiniai:
        failas.write(saltinis)
        failas.write('\n')
    failas.write('\n')

    # - Atrinkite visus skirtingus miestus iš kurių yra šie respondentai.
    failas.write('Miestai iš kurių yra respondentai:\n')
    failas.write('---------------------------------\n')
    for miestas in list(set(miestai)):
        failas.write(miestas)
        failas.write('\n')
    failas.write('\n')

    # - Raskite didžiausią ir mažiausią įvestus atlyginimus.
    failas.write('Didžiausias ir mažiausias įvesti atlyginimai:')
    failas.write('\n')
    failas.write('--------------------------------------------\n')
    failas.write('- maksimalus atlyginimas ')
    failas.seek(25)
    failas.write(str(max(atlyginimai))+' EUR')
    failas.write('\n')
    failas.write('- minimalus atlyginimas ')
    failas.seek(25)
    failas.write(str(min(atlyginimai))+' EUR')
    failas.write('\n')
    failas.write('\n')

    # - Raskite atlyginimų vidurkį.
    failas.write('Atlyginimų vidurkis:\n')
    failas.write('-------------------\n')
    failas.write(str(round(sum(atlyginimai)/len(atlyginimai),2))+' EUR')
    failas.write('\n')
    failas.write('\n')

    # - Raskite atlyginimų vidurkius pagal lygį (1 - junior, 2 - mid, 3 - senior).
    failas.write('Atlyinimų vidurkiai pagal lygį:')
    failas.write('\n')
    failas.write('------------------------------\n')
    failas.write('atlyginimų vidurkis (JUNIOR):')
    failas.seek(21)
    failas.write(str(round(sum(atlyginimai1)/len(atlyginimai1),2))+' EUR')
    failas.write('\n')
    failas.write('atlyginimų vidurkis (MID):')
    failas.seek(21)
    failas.write(str(round(sum(atlyginimai2)/len(atlyginimai2),2))+' EUR')
    failas.write('\n')
    failas.write('atlyginimų vidurkis (SENIOR):')
    failas.seek(21)
    failas.write(str(round(sum(atlyginimai3)/len(atlyginimai3),2))+' EUR')
    failas.write('\n')
failas.close()