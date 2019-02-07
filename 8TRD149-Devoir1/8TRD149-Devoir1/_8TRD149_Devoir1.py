#Requêtes à faire
#c) La liste de tous les titres de livres publiés en 2012.
#e) La liste de tous les exemplaires du livre X qui sont présentement disponibles pour emprunt.
#f) Le nom de tous les membres qui ont présentement un exemplaire du livre X en leur possession.
#g) Le nom de tous les membres ayant un livre présentement en leur possession.

#fonctionalités nécessaires
#Projection: sélectionner UNE colonne d'une table
#Select : sélectionner des lignes d'une table selon une condition
#HalfJoint : Sélectionner les lignes d'une table selon celle d'une autre table

import csv

def Projection1(table : list, nomColonne : 'string') -> list:
    colIndex = -1

    for i in range(len(table[0])):
        if(table[0][i] == nomColonne):
            colIndex = i
            break
    if (colIndex == -1):
        return []

    newTable = []
    
    for i in range(len(table)):
        newTable.append(table[i][colIndex])

    return newTable

testTable = [['col1', 'col2', 'col3'], ['test', 3, 15], ['test2', 82, 36]]

resultTable = Projection1(testTable, 'col3')

for i in range(len(resultTable)):
    print(resultTable[i])