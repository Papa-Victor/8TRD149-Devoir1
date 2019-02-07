#Requêtes à faire
#c) La liste de tous les titres de livres publiés en 2012.
#e) La liste de tous les exemplaires du livre X qui sont présentement disponibles pour emprunt.
#f) Le nom de tous les membres qui ont présentement un exemplaire du livre X en leur possession.
#g) Le nom de tous les membres ayant un livre présentement en leur possession.

#fonctionalités nécessaires
#Projection: sélectionner UNE colonne d'une table
#Select : sélectionner des lignes d'une table selon une condition
#HalfJoint : Sélectionner les lignes d'une table selon celle d'une autre table

import csv, TableManip


testTable = [['col1', 'col2', 'col3', 'col4'], ['test', 3, 15, 56.35], ['test2', 82, 36, 10], ['boi', 6985, 15, 96]]

resultTable = TableManip.Selection(testTable, 'col4', lambda valeurCol : valeurCol <= 56.35)

for i in range(len(resultTable)):
    print(resultTable[i])